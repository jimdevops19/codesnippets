import time

import typer
import csv
import datetime
from rich.progress import track

app = typer.Typer()
orders_file = "orders.csv"
fieldnames = ["customer", "size", "order_time"]

def write_order(data: dict):
    with open(orders_file, "a", newline="") as f:
        csvwriter = csv.DictWriter(f, fieldnames=fieldnames)
        csvwriter.writerow(data)


@app.command(no_args_is_help=True)
def create(customer: str, size: str = "Medium"):
    """

    Create a pizza order

    Examples:

    python order.py create <name>

    python order.py create <name> --size=<yoursize>
    """
    current = datetime.datetime.now()
    current_time = f"{current:%H:%M}"
    print(f"Hello {customer}")
    for _ in track(range(100), description="🍕 Adding your order"):
        time.sleep(0.001)
    write_order(data={
        "customer": customer,
        "size": size,
        "order_time": current_time
    })
    print("Your order has been written!")


@app.command()
def cancel(customer: str):
    confirm = typer.confirm("Are you sure you'd like to cancel ?")
    if not confirm:
        print("Action aborted")
        raise typer.Abort()

    print("Preparing the cancellation")

if __name__ == "__main__":
    app()
