import subprocess
import shlex
import platform
from pathlib import Path

commmand ={
     "list_files":{
          "windows":"dir {path}",
          "linux":"ls {path}",
          "macos":"ls {path}"
     },
     "create_directory":{
          "windows":"mkdir {path}",
          "linux":"mkdir {path}",
          "macos":"mkdir {path}"
     },
     "current_directory":{
          "windows":"cd",
          "linux":"pwd",
          "macos":"pwd"
     },
     "delete_directory":{
          "windows":"rmdir /S /Q {path}",
          "linux":"rm -rf {path}",
          "macos":"rm -rf {path}"
     }
}

project_path = Path.cwd().resolve()

def _safe_path(dir_name: str) -> Path:
     """
     Ensure directory operations stay inside the project directory
     """
     path = (project_path / dir_name).resolve()
     if not path.startswith(str(project_path)):
          raise ValueError(f" Access outside projects directory is not allowed")
     return path

def run_os_command(command: str,
     confirmed:bool=False,
     dir_name: str | None = None,
     new_dir_name: str | None = None,
     ) -> str:
     """
     Run safe OS commands
     """
     system = platform.system().lower()
     if system.startswith("win"):
          os_keys = "windows"
     elif system.startswith("linux"):
          os_keys = "linux"
     elif system.startswith("darwin"):
          os_keys = "macos"
     else:
          raise RuntimeError(f"Unsupported OS: {system}")

     if command not in command:
          raise ValueError(f"Unsupported command: {command}")
     #delete directory
     if command == "delete_directory" and not confirmed:
          raise ValueError("Delete directory command requires confirmation")
     
     cmd_template = commmand[command][os_keys]
     if command in (list_directory,creaate_directory,delete_directory):
          if dir_name:
               cmd_template = cmd_template.format(path=dir_name)
          else:
               raise ValueError("Directory name is required")
     args= shlex.split(cmd_template)
     result = subprocess.run(
          args,
          capture_output=True,
          text=True,
          check=False)
     return result.stdout or result.stderr


     
