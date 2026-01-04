# Desktop Tidy-Up Agent 🧹
*Powered by Goose + Ollama (llama3.2)*

This agent organizes your messy folders by reading the **content** of files and categorizing them locally. No data leaves your machine.

## How to Run

1.  **Generate Test Data**:
    ```bash
    ./setup_junk.sh
    ```
    This creates a `test_downloads/` folder with mixed files.

2.  **Run the Agent**:
    # Point Goose to your local Ollama instance (llama3.2 works great for this!)
    
    GOOSE_PROVIDER=ollama \
    OLLAMA_HOST=http://localhost:11434 \
    goose run --recipe recipes/tidy_up.yaml --model llama3.2 -s
    ```

3.  **Witness the Magic**:
    Watch as `test_downloads/` is organized into `Finance/`, `Work/`, etc.
