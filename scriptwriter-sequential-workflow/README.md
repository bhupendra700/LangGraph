# LangGraph Practice Labs

A collection of hands-on practice projects exploring stateful AI workflows, sequential pipelines, and multi-agent architectures using **LangGraph**, **LangChain**, and **Python**.

---

## Projects Index

| # | Project Folder | Pattern | Description |
| :--- | :--- | :--- | :--- |
| 01 | [\`scriptwriter-sequential-workflow\`]('./scriptwriter-sequential-workflow') | Sequential Workflow | Automated script generation pipeline passing state linearly through multiple processing nodes. |

---

## Tech Stack
* **Orchestration:** LangGraph, LangChain
* **Language:** Python 3.10+
* **Environment Management:** Independent Virtual Environments (\`.venv\`) per project folder

---

## Quick Setup & Run

1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/bhupendra700/LangGraph.git
   cd LangGraph
   \`\`\`

2. **Navigate to your desired project folder:**
   \`\`\`bash
   cd scriptwriter-sequential-workflow
   \`\`\`

3. **Create and activate a virtual environment inside the folder:**
   \`\`\`bash
   python -m venv .venv
   # Windows PowerShell:
   .\\.venv\\Scripts\\Activate.ps1
   \`\`\`

4. **Configure Environment Variables:**
   Create a \`.env\` file in the project folder and add your API keys:
   \`\`\`env
   OPENAI_API_KEY=your_api_key_here
   GOOGLE_API_KEY=your_api_key_here
   \`\`\`

5. **Install dependencies and run:**
   \`\`\`bash
   pip install -r requirements.txt
   python main.py
   \`\`\`