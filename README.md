# Goose + Ollama Agent Examples 🪿 🤖

This repository contains 4 examples of fully local AI agents built with **Goose** and **Ollama**.

These examples demonstrate how to build privacy-focused, intelligent workflows that run entirely on your machine, with Zero Data Egress.

## 🚀 The Agents

1.  **[Desktop Tidy-Up Agent](goose-tidy-up/)**
    - **Concept**: Scans your messy downloads folder and organizes files into categories (Finance, Work, Personal) by reading their content.
    - **Best Model**: `llama3.2` (Small & Fast)

2.  **[Local SQLite Analyst](goose-sqlite-analyst/)** (COMING SOON!)
    - **Concept**: A natural language interface to your local database. Ask questions in plain English, get answers via automatic SQL generation.
    - **Best Model**: `gpt-oss:20b` or `gemma3:12b` (Requires reasoning)

3.  **[Private Code Archaeologist](goose-code-archaeologist/)** (COMING SOON!)
    - **Concept**: Auto-documents spaghetti code. Reads legacy files and inserts professional DocStrings without uploading your code to the cloud.
    - **Best Model**: `gpt-oss:20b` (Requires reliable coding skills)

4.  **[PII Scrubber](goose-pii-scrubber/)** (COMING SOON!)
    - **Concept**: Scans sensitive CSVs for PII (names, emails) and generates a Python script to hash/mask them safely.
    - **Best Model**: `gpt-oss:20b` (Requires complex planning)

## 🛠 Prerequisites

- **[Ollama](https://ollama.com/)**: For running local LLMs.
- **[Goose](https://github.com/block/goose)**: The AI Agent framework.

## 📦 How to Use

Each folder contains a `README.md` with specific run instructions. Generally:

1.  Navigate to the agent folder (e.g., `cd goose-tidy-up`).
2.  Run the setup script (e.g., `./setup_junk.sh`).
3.  Run Goose with the recipe:
    ```bash
    GOOSE_PROVIDER=ollama \
    OLLAMA_HOST=http://localhost:11434 \
    goose run --recipe recipes/PROJECT_RECIPE.yaml --model MODEL_NAME -s
    ```

## 📚 Blog Series

Check out the `blog_posts/` directory for a detailed 4-part guide on how these were built!

## 🐦 Social

Check `twitter_threads/` for shareable summaries of each agent.
