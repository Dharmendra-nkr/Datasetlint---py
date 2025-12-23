import os
import pandas as pd
from datasetlint.core import analyze


def test_tabular(tmp_path):
    df = pd.DataFrame({"a": [1, 2, 2], "target": ["x", "x", "y"]})
    csv_path = tmp_path / "data.csv"
    df.to_csv(csv_path, index=False)

    report = analyze(str(csv_path), label_column="target")

    assert report["rows"] == 3
    assert report["duplicates"] == 1
    assert "class_distribution" in report


def test_images(tmp_path):
    cls_dir = tmp_path / "cats"
    cls_dir.mkdir()
    img_path = cls_dir / "img1.png"

    # Create a tiny valid image
    import PIL.Image as Image

    Image.new("RGB", (1, 1)).save(img_path)

    report = analyze(str(tmp_path))

    assert report["classes"] == {"cats": 1}
    assert "corrupt_images" in report
    assert report.get("imbalance_ratio", 1) >= 1
