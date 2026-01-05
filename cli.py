import typer
from agent import create_agent
from rich.console import Console

console = Console()
app = typer.Typer(add_completion=False)

@app.command()
def main(task: str = typer.Argument(..., help="The task for the agent to perform")):
    """
    Execute a coding task using the autonomous CLI coding agent 
    """
    console.print("[bold cyan] Agent is thinking...[/bold cyan]")
    agent = create_agent()
    result = agent.invoke({"input": task})
    console.print("[bold green]Result:[/bold green]")
    console.print(result["output"])

@app.command()
def os_command(command: str):
    console.print("[bold cyan] Agent is thinking...[/bold cyan]")
    agent = create_agent()
    result = agent.invoke({"input": command})
    console.print("[bold green]Result:[/bold green]")
    console.print(result["output"])

@app.command()

def plan(task:str):
    """
    show what the agent WOULD do , without actually doing it
    """
    console.print("[bold cyan] Agent is planning (no execution)...[/bold cyan]")
    agent = create_agent()
    result = agent.invoke({"input": task})
    console.print("[bold green]Result:[/bold green]")
    console.print(result["output"])

if __name__ == "__main__":
    app()
