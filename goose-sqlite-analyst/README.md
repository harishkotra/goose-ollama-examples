# Local SQLite Analyst 📊
*Powered by Goose + Ollama*

Chat with your local database without writing SQL.

## How to Run

1.  **Generate Dummy DB**:
    ```bash
    python3 setup_db.py
    ```
    Creates `app_logs.db` in the current folder.

2.  **Run the Analyst**:
    ```bash
    GOOSE_PROVIDER=ollama \
    OLLAMA_HOST=http://localhost:11434 \
    goose run --recipe recipes/sqlite_analyst.yaml --model gpt-oss:20b -s
    ```
    *Tip: This agent requires a model capable of multi-step logic. We recommend `gpt-oss:20b` or `gemma3:12b`.*
    *(Remember: Interactive mode needs you to type the first question).*

3.  **Example Questions**:
    - "What are the tables in this DB?"
    - "Show me the top 3 users with the most ERROR logs."
    - "Count the logs by level for the last 24 hours."
