# Autonomous CLI Coding Agent

An advanced, autonomous CLI agent designed for safe and efficient coding tasks. Built with Python, LangChain, and Groq, this agent can understand complex instructions, plan its actions, and execute them while strictly adhering to safety guidelines.

## 🚀 Features

- **Autonomous Problem Solving**: Understands intent and outlines steps before execution.
- **Safety First**: Implements strict planning and review cycles.
- **Filesystem Operations**: Can read from and write to the local filesystem within the project scope.
- **Shell Execution**: Runs shell commands safely with explicit confirmation logic.
- **OS-Specific Commands**: Standardized commands for directory management (list, create, delete) across Windows, Linux, and macOS.
- **Planning Mode**: Validate what the agent *would* do without performing any actions.

## 🛠️ Tech Stack

- **LLM**: Llama 3.3 70B (via Groq)
- **Framework**: LangChain
- **CLI Utilities**: Typer, Rich
- **Environment Management**: Python Dotenv

## 📋 Prerequisites

- Python 3.10+
- Groq API Key

## ⚙️ Configuration

Create a `.env` file in the root directory with the following variables:

```env
GROQ_API_KEY=your_groq_api_key_here
AGENT_OS=windows # or linux/macos
AGENT_LANGUAGE=python
AGENT_RUNTIME=3.11
```

## 🚀 Usage

The agent provides several commands via the CLI:

### 1. Execute a Task
Runs the agent to perform a specific coding task.
```bash
python cli.py main "Create a simple python script that calculates fibonacci numbers"
```

### 2. OS Commands
Runs specific OS-level operations through the agent's safe toolset.
```bash
python cli.py os-command "list_files tools"
```

### 3. Planning Mode
See the agent's plan without execution.
```bash
python cli.py plan "Refactor the current codebase to use async/await"
```

## 🛡️ Safety & Security

- **Path Isolation**: Filesystem tools are restricted to the project root directory.
- **Explicit Confirmation**: Shell commands require explicit user consent (via tool configuration).
- **Standardized Commands**: OS commands are mapped to a safe, predefined list of operations.

---
*Developed for Advanced Agentic Coding.*
