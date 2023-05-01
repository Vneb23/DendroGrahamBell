import os
import random as rd
import numpy as np
from imageio.v3 import imread

def choose(n: int) -> list[list[str]]:
    """Chosses randomly n images for each numbers"""
    L_dir = []
    for i in range(10):
        l = os.listdir(f"numbers/{i}")
        L_dir.append([])
        for j in range(n):
            L_dir[-1].append(f"numbers/{i}/{l[rd.randint(0,len(l))]}")
    return L_dir



def from_image_to_array (name):
    """returns an array of greys from an image
    ---------
    name : string
          name of the image
    """
    img = imread(name)
    n = img.shape[0]
    grey_img = np.zeros(n)
    for i in range(n):
        grey_img[i] = np.mean(np.mean(img[i][0], img[i,1]),img[i][2])
    flat_img = np.ravel(grey_img)
