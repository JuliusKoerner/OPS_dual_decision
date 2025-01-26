import os
import json
from detectron2.data.datasets.builtin_meta import COCO_CATEGORIES

def main():
    instance_json = "/nfs/students/koerner/Datasets/Coco2/annotations/instances_{}.json"
    instance_json_longtail = os.path.join(*instance_json.split("/")[:-1],instance_json.split("/")[-1].replace(".json", "_longtail.json"))

    unseen_names = [e.replace('\n', '') for e in open('datasets/unknown/unknown_K20_longtail.txt', 'r').readlines()]
    unseen_ids = [c["id"] for c in COCO_CATEGORIES if c["name"] in unseen_names]
    s = "val2017"

    with open(instance_json.format(s), "r") as f:
        data = json.load(f)
    dannos = data["annotation"]
    dcategories = data["categories"]
    dimages = data["images"]


    images_with_unseen_object = []
    unseen_categories = []
    #create two json files instance_json_longtail with the training information and instance_json_longtail_anomaly_set with the test information,
    # for that create 2 lists for each: annos, categories and images, which are distinct and are later summarized into the json files.
    print("done")

if __name__ == "__main__":
    main()