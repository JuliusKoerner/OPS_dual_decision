import json
import os
from detectron2.data.datasets.builtin_meta import COCO_CATEGORIES

path = "/nfs/students/koerner/Datasets/Coco2/annotations/instances_val2017_{}_longtail.json"

for prefix in ["with", "without"]:
    with open(path.format(prefix), "r") as f:
        data = json.load(f)

    images = data["images"]
    if prefix == "without":
        images = images[:100]
    else:
        images = images[:100]

    image_ids = [im["id"] for im in images]
    annotations = []
    for ann in data["annotations"]:
        if ann["image_id"] in image_ids:
            annotations.append(ann)

    data["images"] = images
    data["annotations"] = annotations
    print("dumping")
    print(path.format(f"100_all_categories_{prefix}"))
    with open(path.format("100_all_categories_"+prefix),"w") as f:
        json.dump(data, f)