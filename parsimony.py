import copy

class Node:
    def __init__(self , value ,number, parnum ,isleaf = False, parent=None):
        self.number = number
        self.parnum = parnum
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.isleaf = isleaf
        if self.isleaf:
            self.leaves = [self]
        else:
            self.leaves = []

    def SubLeaves(self):
        if self.isleaf:
            return [copy.deepcopy(self)]
        if self.leaves:
            return copy.deepcopy(self.leaves)
        check = []
        c = copy.deepcopy(self)
        current = [c]
        while len(current)!=0:
            c = current.pop(0)
        #    print('in loop   ',c.value , c.isleaf ,c.number)
            check.append(c)
            if c.right:
                if not (c.right in check):
                    current.append(c.right)
            if c.left:

                if not(c.left in check):
                    current.append(c.left)
        for item in check:
        #    print(item.value , item.number , item.isleaf)
            if not item.isleaf:
            #    print('will remove',item.value , depth(item) ,item.order, item.isleaf )
                check.remove(item)
        self.leaves = check
        return copy.deepcopy(check)








def GetTree():
    nn = int(input('Number of nodes: '))
    nodes = []
    print('Please Enter the nodes')
    for i in range(nn - 1):
        x = input().split()
        n = Node('' , int(x[1]) , int(x[0]))
        nodes.append(copy.deepcopy(n))
    m = int(input('Number of leaves:  '))
    subtree = 1
    print('Please Enter the id and value of each leaf')
    for i in range(m):
        mx = input().split()
        for nd in nodes:
            if nd.number == int(mx[0]):
                nd.value = mx[1:][0]
                nd.isleaf = True
                break
    subtree = len(mx[1:][0])


    root = Node('' ,0,  0)
    nodes.insert(0 ,root)
    ind = 0
    while ind < nn:
        for nds in nodes:
            if nds.number == ind:
                cd = nds
                break
        check = 0
        for nd in nodes[1:]:
            if nd.parnum == ind:
                if not check:
                    cd.left = nd
                    check = 1
                else:
                    cd.right = nd
                nd.parent = cd

        ind = ind + 1


    return root ,nodes , subtree



def MiniTree(nx , stx):
    Trees = []
    for i in range(stx):
        tree = copy.deepcopy(nx)
        lvs = tree.SubLeaves()
        lvs = tree.leaves
        for lf in lvs:
            if lf.isleaf:
                lf.value = lf.value[i]
                tree = ROOT(lf)
        Trees.append(copy.deepcopy(tree))

        del tree
    return Trees

def DownTop(tree):
    lf = tree.SubLeaves()
    lf = tree.leaves
    for item in lf:
        if not item.isleaf:
            lf.remove(item)
    check = lf
    l2 = None
    while True:
        if len(check) ==1:
            root = check[0]
            break
        l1 = check.pop(0)
        #print('l1',l1.value , l1.number)
        if l1.number > 0:
            for item in check:
                if item.parent == l1.parent:
                    l2 = item
            #        check.remove(item)
                    break
            if l2:
                check.remove(l2)
            #    print('l2',l2.value , l2.number)
                if l1.value == l2.value:
                    l2.parent.value = l1.value
                else:
                    if l1.parent.left == l1:
                        l2.parent.value = l1.value + l2.value
                    else:
                        l2.parent.value = l2.value + l1.value
                    l2.parent.value = RedundancyRemover(l2.parent.value)
                #print('total',l2.value , l1.value, l2.parent.value)
                check.append(l2.parent)
            else:
                check.append(l1)
        else:
            root = l1
            break
    #tree.value =
    #print(root.value)
    return root

def TopDowm(tree):
    nd = copy.deepcopy(tree)
    lx = len(nd.SubLeaves())
    i = 0
    track = [nd]
    finalnode = copy.deepcopy(nd)
    point = pow(2 , lx)

    while len(track)!= 0:
        i = i + 1
        n = track.pop(0)
    #    PrintTree(n)
    #    print(i , '---------------------')
        r , x = IsUnique(n)
        if r:
            p = ParCal(n)
            if p < point :
                finalnode = copy.deepcopy(n)
    #            PrintTree(finalnode)
    #            print(1000+i , point)
                point = p
        else:
            #nn =copy.deepcopy(n)
            if x.number == 0:
                nn =copy.deepcopy(n)
                nn.value = n.value[0]
                n.value = n.value[1:]
                track.append(n)
                track.append(nn)
            else:
                nn = copy.deepcopy(x)
                nn.value = x.value[0]
                x.value = x.value[1:]
                track.append(ROOT(x))
                track.append(ROOT(nn))
    #print('result: ' , point)
    #PrintTree(finalnode)
    #print('the end')
    return finalnode , point

def IsUnique(rt):
    track = [copy.deepcopy(rt)]
    while len(track) != 0:
        n = track.pop(0)
        if len(n.value)> 1:
            return False ,n
        if n.left:
            if not n.left.isleaf:
                track.append(n.left)
        if n.right:
            if not n.right.isleaf:
                track.append(n.right)
    return True ,1

def constraint(rt):
    track = [rt]
    point =  0
    while len(track) != 0:
        n = track.pop(0)
        if n.left:
            if not n.left.isleaf:
                track.append(n.left)
            if n.value in n.left.value:
                n.left.value = n.value
        if n.right:
            if not n.right.isleaf:
                track.append(n.right)
            if n.value in n.right.value:
                n.right.value = n.value
    return rt



def PrintTree(rt):
    track = [rt]
    point =  0
    while len(track) != 0:
        n = track.pop(0)
        print(n.number , n.value)
        if n.left:
            track.append(n.left)
        if n.right:
            track.append(n.right)


def ParCal(rt):
    track = [copy.deepcopy(rt)]
    point =  0
    while len(track) != 0:
    #    print('point in par cal',point)
        n = track.pop(0)
        if n.left:
            track.append(n.left)
            if n.value != n.left.value:
                point =  point + 1
        if n.right:
            track.append(n.right)
            if n.value != n.right.value:
                point =  point + 1
    #print('final point' , point)
    return point


def ROOT(n):
    if n.number == 0:
        return n
    while n.parent:
        n = n.parent
    return n


def RedundancyRemover(s):
    uniqes = ''
    for i in s:
        if i not in uniqes:
            uniqes = uniqes + i
    return uniqes







nx , nodes , st = GetTree()


trees = MiniTree(nx , st)
theend = []
finalpoint = 0
for k in range(st):
    x =DownTop(trees[k])
    y , p = TopDowm(x)
    finalpoint = finalpoint + p
print('Minimum number of mutations is ',finalpoint)
