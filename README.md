# 🚀 AI Code Agent with Gemini  

[![Demo](https://img.shields.io/badge/LinkedIn-Post-blue)](https://www.linkedin.com/posts/prince-khunt-linked-in_ai-gemini-bootdev-activity-7370409476878766080-0OVq?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEJXpcgBb3xziG9Z0MWkOgCAkNf4DfYoc0E)  

This project integrates **Gemini’s AI capabilities** to act as an **interactive coding agent**.  
It goes beyond just answering coding questions — the agent can **create, update, delete, and run code** directly, making development **faster, smarter, and more hands-on**.  

---

## ✨ Features  

The `functions` directory provides essential developer tools:  

- 🗑️ **`delete_file.py`** → Deletes a specified file.  
- 📄 **`get_file_content.py`** → Gets the content of a given file.  
- 🗑️ **`delete_folder.py`** → Deletes a specified folder.  
- 🐍 **`run_python_files.py`** → Runs a specified Python file.  
- 📂 **`get_files_info.py`** → Lists files in the specified directory.  
- 📦 **`create_folder.py`** → Creates a specified folder.  
- ✍️ **`write_file.py`** → Writes content to a specified file.  

Together, these tools enable the AI agent to **interact with your project structure** just like a real coding assistant.  

---

## ⚡ How It Works  

- **`main.py`** → The entry point for the coding agent.  
  - Handles user input.  
  - Orchestrates function calls.  
  - Manages the workflow.  

- **`call_function.py`** → Dispatches tasks to the correct function inside `functions`.  
  - Acts as a **router** between user requests and functionality.  

---

## 🛠️ Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/PrinceKhunt16/AI-Code-Agent-with-Gemini.git
cd AI-Code-Agent-with-Gemini
