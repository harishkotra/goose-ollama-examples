# PII Scrubber 🧼
*Powered by Goose + Ollama*

Privacy agent that sanitizes datasets without the data ever being exposed to a cloud model.

## How to Run

1.  **Generate Sensitive Data**:
    ```bash
    python3 setup_users.py
    ```
    Creates `users.csv` (the "production dump").

2.  **Run the Scrubber**:
    ```bash
    GOOSE_PROVIDER=ollama \
    OLLAMA_HOST=http://localhost:11434 \
    goose run --recipe recipes/pii_scrubber.yaml --model gpt-oss:20b -s
    ```
    *Tip: This workflow (inspect -> script -> run) requires strong reasoning. Use `gpt-oss:20b` or larger.*
    *(Input: "Clean up users.csv")*

3.  **Check Result**:
    Compare `users.csv` (Raw) vs `users_cleaned.csv` (Sanitized).
