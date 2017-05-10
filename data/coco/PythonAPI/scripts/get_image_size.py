import argparse
from collections import OrderedDict
import json
import os
import sys
sys.path.append(os.path.dirname(sys.path[0]))

from pycocotools.coco import COCO

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Get the image size from an annotation file.")
    parser.add_argument("annofile",
            help = "The file which contains all the annotations for a dataset in json format.")
    parser.add_argument("imgsetfile", default = "",
            help = "A file which contains the image set information.")
    parser.add_argument("namesizefile", default = "",
            help = "A file which stores the name size information.")

    args = parser.parse_args()
    annofile = args.annofile
    imgsetfile = args.imgsetfile
    namesizefile = args.namesizefile

    # initialize COCO api.
    coco = COCO(annofile)

    if namesizefile:
        if not os.path.exists(imgsetfile):
            print "{} does not exist".format(imgsetfile)
            sys.exit()

        name_size_dir = os.path.dirname(namesizefile)
        if not os.path.exists(name_size_dir):
            os.makedirs(name_size_dir)
        # Read image info.
        imgs = dict()
        img_ids = coco.getImgIds()
        for img_id in img_ids:
            # get image info
            img = coco.loadImgs(img_id)[0]
            file_name = img["file_name"]
            name = os.path.splitext(file_name)[0]
            imgs[name] = img

        # Save name size information.
        with open(namesizefile, "w") as nf:
            with open(imgsetfile, "r") as sf:
                for line in sf.readlines():
                    name = line.strip("\n")
                    img = imgs[name]
                    nf.write("{} {} {}\n".format(img["id"], img["height"], img["width"]))
