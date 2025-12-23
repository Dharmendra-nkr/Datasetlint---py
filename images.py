# datasetlint/images.py
import os
from PIL import Image

def analyze_images(root_dir):
    report = {
        "classes": {},
        "corrupt_images": [],
        "empty_images": [],
        "missing_label_dirs": False,
    }

    label_dirs = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
    if not label_dirs:
        report["missing_label_dirs"] = True
        return report

    for cls in label_dirs:
        cls_path = os.path.join(root_dir, cls)

        images = os.listdir(cls_path)
        report["classes"][cls] = len(images)

        for img in images:
            try:
                img_path = os.path.join(cls_path, img)
                if os.path.getsize(img_path) == 0:
                    report["empty_images"].append(img)
                    continue

                Image.open(img_path).verify()
            except:
                report["corrupt_images"].append(img)

    if report["classes"]:
        counts = list(report["classes"].values())
        min_count, max_count = min(counts), max(counts)
        if min_count > 0 and max_count > min_count:
            report["imbalance_ratio"] = round(max_count / min_count, 2)

    return report
