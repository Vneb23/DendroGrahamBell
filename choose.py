import os
import random as rd
import numpy as np
from imageio import imread

def choose(n: int) -> list[list[str]]:
    """Chosses randomly n images for each numbers"""
    L_dir = []
    for i in range(10):
        l = os.listdir(f"numbers/{i}")
        L_dir.append([])
        for j in range(n):
            L_dir[-1].append(f"numbers/{i}/{l[rd.randint(0,len(l)-1)]}")
    return L_dir


def choose_one() -> str:
    """Takes randomly an image among all"""
    return choose(1)[rd.randint(0, 9)][0]


def from_image_to_array (name):
    """returns an array of greys from an image
    ---------
    name : string
          name of the image
    """
    img = imread(name)
    n,m,t = img.shape
    img_bw = np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            img_bw[i][j] = int(np.mean(img[i][j]))
    return img_bw.ravel()

