# LangGraph Practice Labs

A collection of hands-on practice projects exploring stateful AI workflows, sequential pipelines, and multi-agent architectures using **LangGraph**, **LangChain**, and **Python**.

---

## Projects Index

| #   | Script File                                                                          | Pattern             | Description                                                                                    |
| :-- | :----------------------------------------------------------------------------------- | :------------------ | :--------------------------------------------------------------------------------------------- |
| 01  | [`01_scriptwriter_sequential_workflow.py`](./01_scriptwriter_sequential_workflow.py) | Sequential Workflow | Automated script generation pipeline passing state linearly through multiple processing nodes. |

---

## Tech Stack

- **Orchestration:** LangGraph, LangChain
- **Language:** Python 3.10+
- **Environment Management:** Single Root Virtual Environment (`.venv`)

---

## Quick Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/bhupendra700/LangGraph.git
cd LangGraph
```

### 2. Create and activate a virtual environment in the root folder

```bash
python -m venv .venv
```

- **Windows PowerShell:**

  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```

- **Git Bash (Windows):**

  ```bash
  source .venv/Scripts/activate
  ```

- **macOS / Linux:**

  ```bash
  source .venv/bin/activate
  ```

### 3. Configure environment variables

Create a `.env` file in the root folder and add your API keys:

```env
GROQ_API_KEY=your_api_key_here
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run any practice script directly

```bash
python 01_scriptwriter_sequential_workflow.py
```
