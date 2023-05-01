from choose import *
from Cluster import *

def create_clusters(n: int) -> list[Cluster]:
    L = choose(n)
    L_cluster = [Cluster(i) for i in range(10)]
    for i in range(10):
        for image_name in L[i]:
            L_cluster[i].add(from_image_to_array(image_name))
    return L_cluster

