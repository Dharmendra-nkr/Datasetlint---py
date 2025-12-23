from rich.console import Console
from rich.table import Table

console = Console()


def print_report(report):
    table = Table(title="DatasetLint Report")
    table.add_column("Metric")
    table.add_column("Value")

    for k, v in report.items():
        table.add_row(str(k), str(v))

    console.print(table)
