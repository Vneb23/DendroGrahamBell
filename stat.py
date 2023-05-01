from main import *
from tqdm import tqdm

def stat(n_min: int, n_max: int, size:int, dist="min"):
    os.system('cls' if os.name == 'nt' else 'clear')
    Lx = []
    Ly = []
    for i in tqdm(range(n_min, n_max+1), desc=f"Calcul en cours"):
        L_cluster = create_clusters(i)
        p = 0
        for j in range(size):
            l = choose(1)
            N = rd.randint(0, 9)
            if find_cluster(L_cluster, from_image_to_array(l[N][0]), dist=dist).int == N:
                p += 1
        Lx.append(i)
        Ly.append(p/(size))
    plt.plot(Lx, Ly)
    plt.show()

stat(2, 100, 20, dist="mean")
#main(100, dist="mean")