import asyncio
import sys
import os
import json
from pathlib import Path
from contextlib import AsyncExitStack

from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from openai import AsyncOpenAI

# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()

OPENAI_MODEL = "gpt-3.5-turbo"

class MCPClient:
    def __init__(self):
        self.session = None
        self.exit_stack = AsyncExitStack()
        self.openai = AsyncOpenAI()

    async def connect_to_server(self, server_script_path: str):
        path = Path(server_script_path).resolve()

        server_params = StdioServerParameters(
            command=sys.executable,
            args=["-u", str(path)],   # 🔥 unbuffered for Windows
            env=os.environ.copy()
        )

        stdio_transport = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )

        self.stdio, self.write = stdio_transport

        self.session = await self.exit_stack.enter_async_context(
            ClientSession(self.stdio, self.write)
        )

        # ✅ THIS WAS MISSING
        await self.session.initialize()
        print("MCP session initialized", flush=True)

    async def process_query(self, query: str) -> str:
        messages = [{"role": "user", "content": query}]
        tools = (await self.session.list_tools()).tools

        openai_tools = [
            {
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description,
                    "parameters": t.inputSchema,
                },
            }
            for t in tools
        ]

        while True:
            response = await self.openai.chat.completions.create(
                model=OPENAI_MODEL,
                messages=messages,
                tools=openai_tools,
            )

            message = response.choices[0].message

            if not message.tool_calls:
                return message.content

            messages.append(message)

            for call in message.tool_calls:
                args = json.loads(call.function.arguments)
                result = await self.session.call_tool(
                    call.function.name, args
                )

                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": result.content
                })

    async def chat_loop(self):
        while True:
            query = input("\nQuery (type 'quit' to exit): ").strip()
            if query.lower() == "quit":
                break

            reply = await self.process_query(query)
            print("\n" + reply)

    async def cleanup(self):
        await self.exit_stack.aclose()


async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py server.py")
        return

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        print("MCP Client Ready", flush=True)   # ✅ THIS WAS MISSING
        await client.chat_loop()
    finally:
        await client.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
