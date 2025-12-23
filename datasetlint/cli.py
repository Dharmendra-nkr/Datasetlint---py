import click
from datasetlint.core import analyze
from datasetlint.report import print_report


@click.command()
@click.argument("path")
@click.option("--label", default=None, help="Label column name")
def main(path, label):
    try:
        report = analyze(path, label)
    except FileNotFoundError:
        raise click.ClickException(f"Path not found: {path}")
    except Exception as exc:  # surface any parsing/IO issues nicely
        raise click.ClickException(str(exc))

    print_report(report)


if __name__ == "__main__":
    main()
