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
