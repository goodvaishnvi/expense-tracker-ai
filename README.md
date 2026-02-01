# expense-tracker-ai

#AI Personal Finance Assistant (MCP + OpenAI + Supabase)


1. Brief Explanation of the Server

This project implements an **AI-powered Personal Finance Assistant** using an **MCP (Model Context Protocol) server**.

The **server (`server.py`)**:
- Acts as an MCP tool server
- Connects to a Supabase (PostgreSQL) database
- Exposes finance-related tools (add expense, reports, etc.)
- Allows an AI model to call these tools based on natural language input

Users interact via a **client (`client.py`)**, typing messages like:
> “I spent 200 rupees on food”

The AI understands the intent and automatically calls the appropriate server tool.

2. APIs Used in the Server
 🔹 OpenAI API
- Used for natural language understanding
- Supports **tool calling**
- Model used: `gpt-4.1-mini`
🔹 Supabase API
- Cloud-hosted PostgreSQL database
- Used to store and retrieve expense data
- Connected securely using environment variables
🔹 MCP (Model Context Protocol)
- Enables communication between the AI model and backend tools
- Handles tool discovery, execution, and responses

3.Tools Created (Detailed Explanation)

The following MCP tools are implemented in `server.py`:
add_expense:Adds a new expense (amount + category) to the Supabase database.
get_total_expense:Calculates and returns the total amount spent.
category_report:Groups expenses by category and shows category-wise spending.
top_category:Identifies the category with the highest spending.
delete_expense:Deletes an expense entry using its ID.

-`add_expense`
**Purpose:**  
Stores a new expense in the database.

**How it works:**  
- Takes `amount` and `category` as input
- Inserts a new row into the `expenses` table
- Automatically records the timestamp

-Example Query: 
I spent 150 rupees on groceries

4.Pictures or gif files for the results of the queries ran by you.

5.Packages Required
Install the following Python packages:

 pip install mcp openai supabase python-dotenv

6.Members of the Group

-Vaishnavi Surwase 
-Sanket Gayakhe 
- Pratik Kamble
