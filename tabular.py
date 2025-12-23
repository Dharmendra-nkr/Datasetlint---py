# datasetlint/tabular.py
import pandas as pd

def analyze_tabular(path, label_column=None):
    df = pd.read_csv(path) if path.endswith(".csv") else pd.read_json(path)

    report = {}
    report["rows"] = len(df)
    report["columns"] = list(df.columns)
    report["missing_values"] = df.isnull().sum().to_dict()
    report["duplicates"] = int(df.duplicated().sum())

    # Detect mixed data types per column (simple heuristic)
    type_issues = {}
    for col in df.columns:
        non_null = df[col].dropna()
        inferred_types = set(non_null.map(lambda x: type(x).__name__))
        if len(inferred_types) > 1:
            type_issues[col] = sorted(inferred_types)
    if type_issues:
        report["data_type_inconsistencies"] = type_issues

    if label_column and label_column in df.columns:
        counts = df[label_column].value_counts()
        report["class_distribution"] = counts.to_dict()
        if counts.min() > 0:
            report["imbalance_ratio"] = round(counts.max() / counts.min(), 2)

    return report
