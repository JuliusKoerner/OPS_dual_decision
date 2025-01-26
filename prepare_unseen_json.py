import os
import json
from tqdm import tqdm
from detectron2.data.datasets.builtin_meta import COCO_CATEGORIES

def main():
    instance_json = "/nfs/students/koerner/Datasets/Coco2/annotations/instances_{}.json"
    instance_json_longtail = os.path.join(*instance_json.split("/")[:-1],instance_json.split("/")[-1].replace(".json", "_longtail.json"))

    longtail_names = [e.replace('\n', '') for e in open('datasets/unknown/unknown_K20_longtail.txt', 'r').readlines()]
    longtail_ids = [c["id"] for c in COCO_CATEGORIES if c["name"] in longtail_names]
    s = "val2017"
    for s in ["val2017","train2017"]:
        with open(instance_json.format(s), "r") as f:
            data = json.load(f)
        print("read in json: ", instance_json.format(s))
        dannos = data["annotations"]
        dimages = data["images"]

        #create two json files instance_json_longtail with the training information and instance_json_longtail_anomaly_set with the test information,
        # for that create 2 lists for each: annos, categories and images, which are distinct and are later summarized into the json files.
        categories_with_longtail = [c for c in COCO_CATEGORIES if c["name"] in longtail_names]
        categories_without_longtail = [c for c in COCO_CATEGORIES if c["name"] not in longtail_names]

        image_ids_with_longtail = set()
        image_ids_without_longtail = set()
        annos_with_longtail = []
        annos_without_longtail = []
        print("splitting annotations into with and without longtail")
        for ann in tqdm(dannos):
            if ann["category_id"] in longtail_ids:
                annos_with_longtail.append(ann)
                image_ids_with_longtail.add(ann["image_id"])
            else:
                annos_without_longtail.append(ann)
                image_ids_without_longtail.add(ann["image_id"])
        
        images_with_longtail = []
        images_without_longtail = []
        
        print("splitting images")

        #weirdly there are image in the images key frfom the json file that are not in the annotations, but not the other way around
        # hence we need the elif here
        for im in tqdm(dimages):
            if im["id"] in image_ids_with_longtail:
                images_with_longtail.append(im)
            elif im["id"] in image_ids_without_longtail:
                images_without_longtail.append(im)

        with_longtail =  {"info": data["info"], "licenses": data["licenses"], "images": images_with_longtail,
                        "annotations": annos_with_longtail, "categories": categories_with_longtail}
        without_longtail = {"info": data["info"], "licenses": data["licenses"], "images": images_without_longtail,
                        "annotations": annos_without_longtail, "categories": categories_without_longtail}

        print("Dumping into json")
        print("The first...")
        with open(instance_json.format(s).replace(".json", "_with_longtail.json"), "w") as f:
            json.dump(with_longtail,f)
        print("And the second...")
        with open(instance_json.format(s).replace(".json", "_without_longtail.json"), "w") as f:
            json.dump(without_longtail,f)

    print("done")

if __name__ == "__main__":
    main()