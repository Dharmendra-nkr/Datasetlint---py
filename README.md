# datasetlint

DatasetLint is a lightweight checker to validate tabular (CSV/JSON) and image folder datasets before model training.

## Install
```
pip install datasetlint
```

For local development:
```
pip install -e .
```

## Usage
```
datasetlint data.csv --label target
datasetlint images/
```

## Features
- Tabular: missing values, duplicates, class distribution and imbalance, data type inconsistencies.
- Images: class counts, corrupt images, empty files, missing label folders, imbalance ratio.

## Development
Run tests:
```
pytest
```
