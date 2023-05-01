import matplotlib.pyplot as plt

from choose import *
from Cluster import *

def create_clusters(n: int) -> list[Cluster]:
    L = choose(n)
    L_cluster = [Cluster(i) for i in range(10)]
    for i in range(10):
        for image_name in L[i]:
            L_cluster[i].add(from_image_to_array(image_name))
    return L_cluster

def main(n: int, dist: str ="min") -> int:
    L_cluster = create_clusters(n)
    path_img = choose_one()
    img = imread(path_img)
    print(find_cluster(L_cluster, from_image_to_array(path_img), dist=dist).int)
    plt.imshow(img, cmap="gray")
    plt.show()

main(100, dist="mean")