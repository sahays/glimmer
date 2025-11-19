import json

import requests
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
users_app = typer.Typer()
projects_app = typer.Typer()

app.add_typer(users_app, name="users", help="Manage users")
app.add_typer(projects_app, name="projects", help="Manage projects")

API_URL = "http://127.0.0.1:8000"
console = Console()


@app.command()
def hello():
    """
    Check connectivity to the Glimmer API.
    """
    try:
        response = requests.get(f"{API_URL}/")
        if response.status_code == 200:
            data = response.json()
            console.print("[bold green]Connected to Glimmer API![/bold green]")
            console.print(f"Message: {data.get('message')}")
            console.print(f"DB Test: {data.get('db_connection_test')}")
        else:
            console.print(f"[bold red]Failed to connect. Status: {response.status_code}[/bold red]")
    except requests.exceptions.ConnectionError:
        console.print(f"[bold red]Could not connect to {API_URL}. Is the API server running?[/bold red]")


# --- Users Commands ---


@users_app.command("list")
def list_users():
    """List all users."""
    try:
        response = requests.get(f"{API_URL}/users/")
        if response.status_code == 200:
            users = response.json()
            if not users:
                console.print("No users found.")
                return

            table = Table(title="Glimmer Users")
            table.add_column("ID", style="cyan")
            table.add_column("Email", style="magenta")
            table.add_column("Name", style="green")
            table.add_column("Google ID")

            for user in users:
                table.add_row(str(user["user_id"]), user["email"], user.get("full_name") or "", user["google_id"])
            console.print(table)
        else:
            console.print(f"[bold red]Error: {response.status_code}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")


@users_app.command("create")
def create_user(email: str, google_id: str, full_name: str = None):
    """Create a new user."""
    payload = {"email": email, "google_id": google_id, "full_name": full_name}
    try:
        response = requests.post(f"{API_URL}/users/", json=payload)
        if response.status_code == 201:
            console.print("[bold green]User created successfully![/bold green]")
            console.print(json.dumps(response.json(), indent=2))
        else:
            console.print(f"[bold red]Failed to create user: {response.text}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")


# --- Projects Commands ---


@projects_app.command("list")
def list_projects(owner_id: int = None):
    """List all projects, optionally filtered by owner_id."""
    params = {}
    if owner_id:
        params["owner_id"] = owner_id

    try:
        response = requests.get(f"{API_URL}/projects/", params=params)
        if response.status_code == 200:
            projects = response.json()
            if not projects:
                console.print("No projects found.")
                return

            table = Table(title="Glimmer Projects")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="magenta")
            table.add_column("Owner ID", style="green")
            table.add_column("Created At")

            for proj in projects:
                table.add_row(str(proj["project_id"]), proj["project_name"], str(proj["owner_id"]), proj["created_at"])
            console.print(table)
        else:
            console.print(f"[bold red]Error: {response.status_code}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")


@projects_app.command("create")
def create_project(name: str, owner_id: int):
    """Create a new project."""
    payload = {"project_name": name, "owner_id": owner_id}
    try:
        response = requests.post(f"{API_URL}/projects/", json=payload)
        if response.status_code == 201:
            console.print("[bold green]Project created successfully![/bold green]")
            console.print(json.dumps(response.json(), indent=2))
        else:
            console.print(f"[bold red]Failed to create project: {response.text}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")


if __name__ == "__main__":
    app()
