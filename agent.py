from langchain_core.tools import Tool
from langchain.agents import initialize_agent,AgentType
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from prompts import system_prompt
from config import load_environment
from tools.filesystem import read_file, write_file
from tools.shell import run_command
from tools.os_command import run_os_command


def create_agent():
    # Enforce environment validation (NO assumptions)
    load_environment()

    llm = ChatGroq(model_name="llama-3.3-70b-versatile",temperature=0)

    tools = [
        Tool(
            name="read_file",
            func=read_file,
            description="Read a file from disk"
        ),
        Tool(
            name="write_file",
            func=write_file,
            description="Write content to a file"
        ),
        Tool(
            name="run_command",
            func=lambda cmd: run_command(cmd, confirmed=True),
            description="Run a shell command safely with explicit confirmation"
        ),
        Tool(
            name="run_os_command",
            func=lambda cmd: run_os_command(cmd, confirmed=True),
            description="Run an OS command safely. Valid command keys: list_files, create_directory, current_directory, delete_directory. Input format: 'key' or 'key path' (e.g., 'create_directory my_dir')."
        ),
    ]

    prompt = PromptTemplate.from_template(system_prompt)

    agent = initialize_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

    return agent

