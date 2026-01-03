import subprocess
import shlex
import platform
from pathlib import Path

COMMANDS = {
     "list_files": {
          "windows": "dir {path}",
          "linux": "ls {path}",
          "macos": "ls {path}"
     },
     "create_directory": {
          "windows": "mkdir {path}",
          "linux": "mkdir {path}",
          "macos": "mkdir {path}"
     },
     "current_directory": {
          "windows": "cd",
          "linux": "pwd",
          "macos": "pwd"
     },
     "delete_directory": {
          "windows": "rmdir /S /Q {path}",
          "linux": "rm -rf {path}",
          "macos": "rm -rf {path}"
     }
}

project_path = Path.cwd().resolve()

def _safe_path(dir_name: str) -> Path:
     """
     Ensure directory operations stay inside the project directory
     """
     path = (project_path / dir_name).resolve()
     if not str(path).startswith(str(project_path)):
          raise ValueError(f" Access outside projects directory is not allowed")
     return path

def run_os_command(command_input: str,
     confirmed:bool=False,
     dir_name: str | None = None,
     new_dir_name: str | None = None,
     ) -> str:
     """
     Run safe OS commands. input can be "command" or "command path"
     """
     parts = command_input.split(maxsplit=1)
     command = parts[0]
     if len(parts) > 1 and not dir_name:
          dir_name = parts[1]
     system = platform.system().lower()
     if system.startswith("win"):
          os_keys = "windows"
     elif system.startswith("linux"):
          os_keys = "linux"
     elif system.startswith("darwin"):
          os_keys = "macos"
     else:
          raise RuntimeError(f"Unsupported OS: {system}")

     if command not in COMMANDS:
          raise ValueError(f"Unsupported command: {command}")
     
     # delete directory
     if command == "delete_directory" and not confirmed:
          raise ValueError("Delete directory command requires confirmation")
     
     cmd_template = COMMANDS[command][os_keys]
     if command in ("list_files", "create_directory", "delete_directory"):
          if dir_name:
               cmd_template = cmd_template.format(path=dir_name)
          elif command == "list_files":
               cmd_template = cmd_template.format(path=".")
          else:
               raise ValueError("Directory name is required")
     
     args = shlex.split(cmd_template)
     # On Windows, commands like 'dir' and 'mkdir' are shell builtins
     use_shell = platform.system().lower().startswith("win")
     
     result = subprocess.run(
          cmd_template if use_shell else args,
          capture_output=True,
          text=True,
          check=False,
          shell=use_shell)
     return result.stdout or result.stderr


     
