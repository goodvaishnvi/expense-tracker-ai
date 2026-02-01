import os
from dotenv import load_dotenv
from supabase import create_client
from mcp.server.fastmcp import FastMCP

# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Supabase credentials not found in .env file")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# -----------------------------------
# Create MCP Server
# -----------------------------------
server = FastMCP("AI-Personal-Finance-Assistant")

# -----------------------------------
# MCP TOOLS
# -----------------------------------

@server.tool(name="add_expense", description="Add an expense")
async def add_expense(amount: float, category: str) -> str:
    supabase.table("expenses").insert({
        "amount": amount,
        "category": category
    }).execute()

    return f"Expense of ₹{amount} added under '{category}'."

@server.tool(name="get_total_expense", description="Get total spending")
async def get_total_expense() -> str:
    res = supabase.table("expenses").select("amount").execute()
    total = sum(row["amount"] for row in (res.data or []))
    return f"Your total spending is ₹{total}"


@server.tool(name="monthly_report", description="Category-wise report")
async def monthly_report() -> dict:
    res = supabase.table("expenses").select("*").execute()
    report = {}

    for row in (res.data or []):
        report[row["category"]] = report.get(row["category"], 0) + row["amount"]

    return report

@server.tool(name="top_category", description="Highest spending category")
async def top_category() -> str:
    res = supabase.table("expenses").select("*").execute()
    summary = {}

    for row in (res.data or []):
        summary[row["category"]] = summary.get(row["category"], 0) + row["amount"]

    if not summary:
        return "No expenses found."

    top = max(summary, key=summary.get)
    return f"Top spending category: {top}"


@server.tool(name="delete_expense", description="Delete expense by ID")
async def delete_expense(expense_id: str) -> str:
    supabase.table("expenses").delete().eq("id", expense_id).execute()
    return f"Expense {expense_id} deleted."


# -----------------------------------
# Run MCP Server (STDIO)
# -----------------------------------
if __name__ == "__main__":
    server.run(transport="stdio")
