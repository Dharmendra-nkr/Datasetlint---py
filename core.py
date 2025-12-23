# datasetlint/core.py
from datasetlint.tabular import analyze_tabular
from datasetlint.images import analyze_images

def analyze(path, label_column=None):
    if path.endswith((".csv", ".json")):
        return analyze_tabular(path, label_column)
    else:
        return analyze_images(path)
