import os, random as rd

def choose(n: int) -> list[list[str]]:
    """Chosses randomly n images for each numbers"""
    L_dir = []
    for i in range(10):
        l = os.listdir(f"numbers/{i}")
        L_dir.append([])
        for i in range(n):
            L_dir[-1].append(l[rd.randint(0,len(l))])
    return L_dir