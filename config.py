from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class EnvironmentConfig:
     target_os:str
     target_language:str
     target_runtime:str
    

def load_environment()->EnvironmentConfig:
     target_os = os.getenv("AGENT_OS")
     target_language = os.getenv("AGENT_LANGUAGE")
     target_runtime = os.getenv("AGENT_RUNTIME")

     missing = [name for name ,value in {
          "AGENT_OS":target_os,
          "AGENT_LANGUAGE":target_language,
          "AGENT_RUNTIME":target_runtime
     }.items() if value is None]

     if missing:
          raise RuntimeError(f"Missing environment variables: {', '.join(missing)}")

     return EnvironmentConfig(
          target_os=target_os,
          target_language=target_language,
          target_runtime=target_runtime,
     )