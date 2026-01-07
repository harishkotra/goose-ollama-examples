# Private Code Archaeologist 🔦
*Powered by Goose + Ollama*

An agent that documents your legacy/spaghetti code entirely locally.

## How to Run

1.  **Generate Legacy Code**:
    ```bash
    python3 setup_legacy.py
    ```
    Creates `legacy_math.py` (ugly, no comments).

2.  **Run the Archaeologist**:
    ```bash
    GOOSE_PROVIDER=ollama \
    OLLAMA_HOST=http://localhost:11434 \
    goose run --recipe recipes/code_archaeologist.yaml --model gpt-oss:20b -s
    ```
    *Tip: For reliable file editing, use a larger model like `gpt-oss:20b` or `qwen2.5-coder`.*
    *(Input: "Please document legacy_math.py")*

3.  **Check Result**:
    Open `legacy_math.py` to see the newly added DocStrings!
