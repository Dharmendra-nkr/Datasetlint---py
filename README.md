# datasetlint

DatasetLint is a tiny CLI to lint datasets before training. It works on tabular (CSV/JSON) and folder-structured image datasets.

## Install
- User install: `pip install datasetlint`
- Dev install: `pip install -e .`

## Quickstart
```
# Tabular
datasetlint data.csv --label target

# Images (folders per class)
datasetlint path/to/images/
```

### What you get (tabular)
- Row/column counts
- Missing values per column
- Duplicate row count
- Class distribution + imbalance ratio (when `--label` is provided)
- Basic data type inconsistency detection per column

### What you get (images)
- Class counts (per folder)
- Missing label folders flag
- Empty file detection
- Corrupt image detection
- Class imbalance ratio

## CLI
- `datasetlint PATH [--label LABEL_COLUMN]`
- PATH ending with `.csv` or `.json` is treated as tabular; otherwise treated as an image root folder.

## Development
```
python -m venv venv
venv\Scripts\activate  # Windows (or source venv/bin/activate)
pip install -e .
pytest
```

## Publish (summary)
```
pip install build twine
python -m build
twine upload dist/*
```
