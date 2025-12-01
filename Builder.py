import OtherClasses as C

TotalPath = []

def createWeb(string):
    header = C.Node(string,"","","")
    web = C.PancakeStack(header)
    used = []
    linkNodes(header,used,web)
    return web

def linkNodes(node,used,web):
    if (nodeInUsed(used,node.data) == False and node != "" and node != None):
        used.append(node)
        tempN = flip(node.data, len(node.data))
        tempN1 = flip(node.data, len(node.data) - 1)
        tempN2 = flip(node.data, len(node.data) - 2)
        n = findNode(used,tempN)
        node.nFlip = n
        n.nFlip = node
        n1 = findNode(used, tempN1)
        node.n1Flip = n1
        n1.n1Flip = node
        n2 = findNode(used, tempN2)
        node.n2Flip = n2
        n2.n2Flip = node
        linkNodes(n,used,web)
        linkNodes(n1,used,web)
        linkNodes(n2,used,web)

def flip(string,n):
    newString = string[n-1::-1] + string[n:]
    return newString

def findNode(used,string):
    for i in range(0,len(used)):
        if used[i].data == string:
            return used[i]
    return C.Node(string,"","","")

def nodeInUsed(used,string):
    for i in range(0, len(used)):
        if used[i].data == string:
            return True
    return False

def depthFirstSearch(pointer,count,path):
    global TotalPath
    if pointer.visited == True:
        pointer.visited = False
        path.append(pointer)
        depthFirstSearch(pointer.nFlip,count,path)
        depthFirstSearch(pointer.n1Flip,count,path)
        depthFirstSearch(pointer.n2Flip,count,path)
    if len(path) == factorial(len(path[0].data)):
        TotalPath = path

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


