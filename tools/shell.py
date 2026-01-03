import subprocess
import shlex

def run_command(command: str,confirmed:bool=False) -> str:
     if not confirmed:
          raise PermissionError("destructive commands are not allowed")

     args = shlex.split(command)
     result=subprocess.run(
          args,
          capture_output=True,
          text=True,
          check=False)     
     
     return result.stdout or result.stderr