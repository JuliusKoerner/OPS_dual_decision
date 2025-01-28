import json
import os
from detectron2.data.datasets.builtin_meta import COCO_CATEGORIES

instance_json_path = "/nfs/students/koerner/Datasets/Coco2/annotations/instances_{}_with_longtail.json"
gt_json_path = "/nfs/students/koerner/Datasets/Coco2/annotations/panoptic_{}.json"

longtail_names = [e.replace('\n', '') for e in open('datasets/unknown/unknown_K20_longtail.txt', 'r').readlines()]
#"val2017",
prefix = ["val2017","val2017_100"]
for s in prefix:
    print("reading from ", instance_json_path.format(s))
    with open(instance_json_path.format(s), "r") as f:
        instance_json = json.load(f)
    with open(gt_json_path.format("val2017"), "r") as f:
        gt_json = json.load(f)
    instance_images = sorted(set([ann["image_id"] for ann in instance_json["annotations"]]))


    longtail_ids = [c["id"] for c in COCO_CATEGORIES if c["name"] in longtail_names]
    assert longtail_ids.__len__() == longtail_names.__len__()
    gt_json.keys()
    longtail_id = 254
    counter = 0
    longtail_annotations = []
    for anno in gt_json["annotations"]:
        if anno["image_id"] not in instance_images:
            continue
        segments = anno["segments_info"]
    

    
        for seg in segments:
            if seg["category_id"] in longtail_ids:
                seg["category_id"] = longtail_id
                counter += 1
        longtail_annotations.append(anno)
    
    longtail_panoptic = instance_json.copy()
    longtail_panoptic["annotations"] = longtail_annotations
    longtail_panoptic["categories"] = gt_json["categories"]
    longtail_panoptic["categories"].append({'supercategory': 'unseen', 'isthing': 1, 'id': 254, 'name': 'unseen'})
    store = s+"_with_longtail"
    print("dumping into ", gt_json_path.format(store))
    with open(gt_json_path.format(store), "w") as f:
        json.dump(longtail_panoptic, f)

