import math
import numpy as np

def Prufer_to_Tree(seq):
    L = len(seq) + 2
    tree = {i:[] for i in range(1,L+1)}
    for i in range(len(seq)):
        leafs = []
        for i in range(1,L+1):
            if i not in seq:
                leafs.append(i)
        tree[seq[0]].append(leafs[0])
        tree[leafs[0]].append(seq[0])
        seq = seq[1:]
        seq.append(leafs[0])


    leafs = []
    for i in range(1,L+1):
        if i not in seq:
            leafs.append(i)
    tree[leafs[0]].append(leafs[1])
    tree[leafs[1]].append(leafs[0])

    return tree

def Tree_to_Prufer(tree):
    val = True
    seq = []
    while val:
        leafs = []
        for node in tree:
            if len(tree[node]) == 1:
                leafs.append(node)
        if len(leafs) == 0:
            val = False
        else:
            smallest = min(leafs)
            neighbor = tree[smallest][0]
            seq.append(neighbor)
            tree[neighbor].remove(smallest)
            tree[smallest] = []
    seq = seq[:-1]
    return seq


def Create_Tree(con_tree, file_name, normal_mu = 0, normal_sigma2 = 0, exp_rate = 0, poisson_rate = 0, uniform_low = 0, uniform_high = 0, p_normal = 0, p_exp = 0, p_poisson = 0, p_uniform = 0):
    if p_normal + p_exp + p_poisson + p_uniform != 1:
        print("Distribution probabilities do not sum to 1")
        return None
    size = len(con_tree)
    file = open(file_name,"w")
    norm_num = math.ceil(size * p_normal)
    exp_num = math.ceil(size * p_exp)
    poisson_num = math.ceil(size * p_poisson)
    uniform_num = math.ceil(size * p_uniform)
    for key in con_tree:
        size = norm_num+exp_num+poisson_num+uniform_num
        if len(con_tree[key]) != 0:
            val = np.random.randint(1,size+1)
            if val <= norm_num:
                file.write(str(key)+","+str(con_tree[key][0])+",N,"+str(normal_mu)+","+str(normal_sigma2)+"\n")
                norm_num = norm_num - 1
                con_tree[con_tree[key][0]].remove(key)
                con_tree[key].pop(0)
            elif val <= exp_num:
                file.write(str(key)+","+str(con_tree[key][0])+",E,"+str(exp_rate)+"\n")
                exp_num = exp_num - 1
                con_tree[con_tree[key][0]].remove(key)
                con_tree[key].pop(0)
            elif val <= poisson_num:
                file.write(str(key)+","+str(con_tree[key][0])+",P,"+str(poisson_rate)+"\n")
                poisson_num = poisson_num - 1
                con_tree[con_tree[key][0]].remove(key)
                con_tree[key].pop(0)
            else:
                file.write(str(key)+","+str(con_tree[key][0])+",U,"+str(uniform_low)+","+str(uniform_high)+"\n")
                uniform_num = uniform_num - 1
                con_tree[con_tree[key][0]].remove(key)
                con_tree[key].pop(0)
    file.close()
