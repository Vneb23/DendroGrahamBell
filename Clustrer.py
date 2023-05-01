import numpy as np

class Cluster:
    def __init__(self, n:int):
        self.int = n
        """The theorical value of the cluster"""
        self.values = []
        """Set of datas, which are arrays"""
        self.repre = None
        
    def add(self, v) -> None:
        """Adds a new vector"""
        self.values.append(v)
    
    def mean(self):
        """Returns the mean of the cluster if not empty"""
        v_mean = np.zeros(self.values[0].shape)
        for v in self.values:
            v_mean += v
        return v_mean/len(self.values)

    def dist_min(self, v) -> float:
        """Returns the minimal distance between the given vector and a vector of the cluster"""
        d = np.inf
        for v_ in self.values:
            d_ = distance(v, v_)
            d = min(d, d_)
        return d
    
    def dist_min(self, v) -> float:
        """Returns the maximal distance between the given vector and a vector of the cluster"""
        d = 0
        for v_ in self.values:
            d_ = distance(v, v_)
            d = max(d, d_)
        return d
    
    def dist_mean(self, v) -> float:
        """Returns the distance between the given vector and the mean of the cluster"""
        return distance(v, self.mean())
    
    def dist_repre(self, v) -> float:
        """Returns the distance between the given vector and the repre of the cluster"""
        if self.repre == None:
            raise Exception("Cluster.repre not defined")
        return distance(v, self.mean())



def distance(v1, v2) -> float:
    """Returns the square of the distance for ||.||2"""
    return sum((v1-v2)**2)


c = Cluster(2)
print(c.int, c.repre)

c.add(np.array([0,1,2,3]))
c.add(np.array([1,2,3,4]))

print(c.values)
print(f"c.dist_mean(np.array([4,3,2,1]))={c.dist_mean(np.array([4,3,2,1]))}, c.dist_min(np.array([4,3,2,1]))={c.dist_min(np.array([4,3,2,1]))}")