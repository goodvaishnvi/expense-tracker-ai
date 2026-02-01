# expense-tracker-ai

AI Personal Finance Assistant (MCP + OpenAI + Supabase)
1. Brief Explanation of the Server
This project implements an AI-powered Personal Finance Assistant using an MCP (Model Context Protocol) server.

🔹 Server (server.py)
Acts as an MCP tool server
Connects to a Supabase (PostgreSQL) database
Exposes multiple finance-related tools such as:
Add expense
Get total expense
Category-wise report
Enables an AI model to call backend tools using natural language
🔹 Client (client.py)
Users interact by typing natural language messages like:
“I spent 200 rupees on food”
The AI understands the intent and automatically calls the correct server tool

2. APIs Used in the Server
🔹 OpenAI API
Used for natural language understanding
Supports tool calling
Model used: gpt-4.1-mini

🔹 Supabase API
Cloud-hosted PostgreSQL database
Stores and retrieves expense data
Connected securely using environment variables
🔹 MCP (Model Context Protocol)
Enables communication between the AI model and backend tools
Handles:
Tool discovery
Tool execution
Response handling

3. Tools Created (Detailed Explanation)
The following MCP tools are implemented in server.py:
🔹 add_expense
Purpose:
Adds a new expense to the database.
How it works:
Takes amount and category as input
Inserts a new row into the expenses table
Automatically stores the timestamp
Example Query:
I spent 150 rupees on groceries
🔹 get_total_expense
Purpose:
Calculates and returns the total amount spent so far.
🔹 category_report
Purpose:
Groups expenses by category
Displays category-wise spending summary
🔹 top_category
Purpose:
Identifies the category with the highest spending
🔹 delete_expense
Purpose:
Deletes an expense record using its expense ID
4. Output Results (Screenshots / GIFs)
<img width="1600" height="409" alt="image" src="https://github.com/user-attachments/assets/7cf0f67b-6e5b-4460-8694-a53215f0d00c" />
<img width="1600" height="145" alt="image" src="https://github.com/user-attachments/assets/2d7bbbbe-4785-4509-b144-817123aab191" />
<img width="1600" height="136" alt="image" src="https://github.com/user-attachments/assets/149e8725-4735-47ce-a8d2-a38a776257a6" />
<img width="1280" height="578" alt="image" src="https://github.com/user-attachments/assets/3220365b-4265-4a78-abda-821d2ab639a9" />

Total expense calculation
These visuals demonstrate the working output of the system

5. Packages Required
Install the required Python packages using:
pip install mcp openai supabase python-dotenv

6. Members of the Group
 Team Members
Vaishnavi Surwase
Sanket Gayakhe
Pratik Kamble

Email IDs
vaishnavisurwase95@gmail.com
gayakhesanket@gmail.com
kamblepratik380@gmail.com
