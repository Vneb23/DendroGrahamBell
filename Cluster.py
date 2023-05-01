import numpy as np

class Cluster:
    def __init__(self, n:int, values=[]):
        self.int = n
        """The theorical value of the cluster"""
        self.values = values
        """Set of datas, which are arrays"""
        self.center = None
        self.mean = None
        self.update_mean()
        
    def add(self, v) -> None:
        """Adds a new vector"""
        self.values.append(v)
        self.update_mean()
    
    def update_mean(self):
        """Update the mean of the cluster if not empty"""
        if self.values != []:
            v_mean = np.zeros(self.values[0].shape)
            for v in self.values:
                v_mean += v
            self.mean = v_mean/len(self.values)

    def dist_min(self, v) -> float:
        """Returns the minimal distance between the given vector and a vector of the cluster"""
        d = np.inf
        for v_ in self.values:
            d_ = distance(v, v_)
            d = min(d, d_)
        return d
    
    def dist_max(self, v) -> float:
        """Returns the maximal distance between the given vector and a vector of the cluster"""
        d = 0
        for v_ in self.values:
            d_ = distance(v, v_)
            d = max(d, d_)
        return d
    
    def dist_mean(self, v) -> float:
        """Returns the distance between the given vector and the mean of the cluster"""
        return distance(v, self.mean)
    
    def dist_center(self, v) -> float:
        """Returns the distance between the given vector and the repre of the cluster"""
        if self.center == None:
            raise Exception("Cluster.center not defined")
        return distance(v, self.center)



def distance(v1, v2) -> float:
    """Returns the square of the distance for ||.||2"""
    return sum((v1-v2)**2)


def find_cluster(L: list[Cluster], v, dist: str ="min") -> Cluster:
    """returns the nearest cluster for the choosen distance between:
    -'min'
    -'max'
    -'mean'
    -'center'"""
    if L == []:
        raise Exception("Empty list of Clusters")
    C = L[0]
    for c in L:
        
        if dist=="min":
            delta_d = C.dist_min(v) - c.dist_min(v)
        elif dist=="max":
            delta_d = C.dist_max(v) - c.dist_max(v)
        elif dist=="mean":
            delta_d = C.dist_mean(v) - c.dist_mean(v)
        elif dist=="center":
            delta_d = C.dist_center(v) - c.dist_center(v)
        else:
            raise Exception(f"unknown parameter: {dist}")
            
        if delta_d > 0:
            C = c
    
    return C