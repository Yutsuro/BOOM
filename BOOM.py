import os
import cv2
import json

import numpy as np

from pycocotools.coco import COCO
from utils.load_config import load_config


# function to get blured image
def blur_outside_of_mask(coco:COCO,img,annots,kernel_size=25):

     base_mask = np.zeros((img.shape[0],img.shape[1])).astype("bool")

     for annot in annots:
         segpoint = [(len(seg)<5) for seg in annot["segmentation"]]
         if any(segpoint):
             annot["segmentation"] = [annot["segmentation"][i] for i, x in enumerate(segpoint) if not x]
         for mask in annot["segmentation"]:
             mask = coco.annToMask(annot).astype("bool")
             base_mask = base_mask | mask

     kernel = np.ones((kernel_size,kernel_size),np.uint8)
     dilation = cv2.dilate(base_mask.astype("uint8"),kernel,iterations=1)

     img_blur = cv2.blur(img,(kernel_size,kernel_size))
     img_blur[dilation[:,:,]==1] = img[dilation[:,:,]==1]

     return img_blur


def main():

     config = load_config()

     coco = COCO(config.annotationPath)

     person_id = coco.getCatIds(catNms=config.picCategory)
     image_ids = sorted(coco.getImgIds(catIds=person_id))

     # blur directory path
     image_save_dir = os.path.join(os.path.dirname(os.path.dirname(config.imageDir)),
                                   "blur",
                                   os.path.basename(config.imageDir))
     os.makedirs(image_save_dir, exist_ok=True)

     # get and save blured images for each images
     for i in range(len(image_ids)):

         image_id = image_ids[i]
         anno_ids = coco.getAnnIds(image_id)
         annots = coco.loadAnns(anno_ids)
         image_name = coco.loadImgs([image_id])[0]['file_name']
    
         img_path = os.path.join(config.imageDir, image_name)
         img = cv2.imread(img_path)

         # get blured image
         img_blur = blur_outside_of_mask(coco, img, annots, config.karnelSize)

         # save to blur directory
         cv2.imwrite(os.path.join(image_save_dir, image_name), img_blur)
     
     print("blur finished!!")


if __name__=="__main__":
     main()