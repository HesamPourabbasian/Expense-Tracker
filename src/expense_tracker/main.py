import typer
import pandas as pd
from rich.console import Console
from rich.table import Table
from pathlib import Path
from datetime import datetime

app = typer.Typer()
console = Console()

DATA_FILE = Path.home() / ".expense_tracker.csv"


def ensure_data_file_exists():
    if not DATA_FILE.exists():
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(DATA_FILE, index=False)


@app.command()
def add(amount: float, category: str, description: str = "", date: str = typer.Argument(None)):

    ensure_data_file_exists()

    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    new_record = {
        "Date": date,
        "Category": category.title(),
        "Amount": amount,
        "Description": description
    }

    new_df = pd.DataFrame([new_record])
    df = pd.read_csv(DATA_FILE)

    if df.empty:
        updated_df = new_df
    else:
        updated_df = pd.concat([df, new_df], ignore_index=True)

    updated_df.to_csv(DATA_FILE, index=False)
    console.print(f"[bold green]Expense of {amount} added successfully![/bold green]")


@app.command()
def summary():

    ensure_data_file_exists()

    df = pd.read_csv(DATA_FILE)
    if df.empty:
        console.print("[bold red]No expenses recorded yet.[/bold red]")
        return

    summary_df = df.groupby("Category")["Amount"].sum().reset_index()
    summary_df["Amount"] = summary_df["Amount"].round(2)

    table = Table(title="Expense Summary by Category")
    table.add_column("Category", style="cyan")
    table.add_column("Total Amount", style="magenta")

    for _, row in summary_df.iterrows():
        table.add_row(row["Category"], str(row["Amount"]))

    console.print(table)

    total_expenses = summary_df["Amount"].sum().round(2)
    console.print(f"\n[bold]Total Expenses: [green]{total_expenses}[/green][/bold]")


@app.command()
def show(last: int = 10):

    ensure_data_file_exists()

    df = pd.read_csv(DATA_FILE)
    if df.empty:
        console.print("[bold red]No expenses recorded yet.[/bold red]")
        return

    df = df.fillna("")

    last_expenses = df.tail(last).reset_index(drop=True)

    table = Table(title=f"Last {last} Expenses")
    table.add_column("ID", style="dim", justify="center")
    table.add_column("Description", style="white")
    table.add_column("Category", style="magenta")
    table.add_column("Amount", style="green")
    table.add_column("Date", style="cyan")


    for index, row in last_expenses.iterrows():
        original_index = df.index[-last:][index]
        table.add_row(
            str(original_index + 1),
            str(row["Date"]),
            row["Category"],
            str(row["Amount"]),
            row["Description"]
        )

    console.print(table)


@app.command()
def remove(id: int):

    ensure_data_file_exists()

    df = pd.read_csv(DATA_FILE)
    if df.empty:
        console.print("[bold red]No expenses recorded yet.[/bold red]")
        return

    index_to_remove = id - 1

    if index_to_remove not in df.index:
        console.print(f"[bold red]Error: ID {id} not found.[/bold red]")
        return

    df = df.drop(index_to_remove).reset_index(drop=True)
    df.to_csv(DATA_FILE, index=False)

    console.print(f"[bold green]Expense with ID {id} removed successfully.[/bold green]")


@app.command()
def remove_last():

    ensure_data_file_exists()

    df = pd.read_csv(DATA_FILE)
    if df.empty:
        console.print("[bold red]No expenses to remove.[/bold red]")
        return

    df = df.iloc[:-1]
    df.to_csv(DATA_FILE, index=False)

    console.print("[bold green]Last expense removed successfully.[/bold green]")


@app.command()
def budget_check(monthly_budget: float):

    ensure_data_file_exists()

    df = pd.read_csv(DATA_FILE)
    if df.empty:
        console.print("[bold red]No expenses recorded yet.[/bold red]")
        return

    today = datetime.now()
    current_month = today.month

    df['Date'] = pd.to_datetime(df['Date'])
    monthly_expenses = df[df['Date'].dt.month == current_month]['Amount'].sum().round(2)

    remaining_budget = monthly_budget - monthly_expenses

    table = Table(title="Monthly Budget Status")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Monthly Budget", f"{monthly_budget}")
    table.add_row("Total Expenses This Month", f"{monthly_expenses}")

    if remaining_budget >= 0:
        table.add_row("Remaining Budget", f"[bold green]{remaining_budget}[/bold green]")
        console.print(table)
        console.print(f"\n[bold green]You are on track! {remaining_budget} left for this month.[/bold green]")
    else:
        table.add_row("Over Budget by", f"[bold red]{abs(remaining_budget)}[/bold red]")
        console.print(table)
        console.print(f"\n[bold red]Warning: You are over budget by {abs(remaining_budget)} for this month.[/bold red]")


if __name__ == "__main__":
    app()