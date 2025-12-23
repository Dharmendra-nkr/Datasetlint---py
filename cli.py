# datasetlint/cli.py
import click
from datasetlint.core import analyze
from datasetlint.report import print_report

@click.command()
@click.argument("path")
@click.option("--label", default=None, help="Label column name")
def main(path, label):
    report = analyze(path, label)
    print_report(report)

if __name__ == "__main__":
    main()
