class PancakeStack:
    def __init__(self,startingNode):
        self.head = startingNode

    def findNode(self,pointer,string):
        if pointer != "" and pointer != None:
            if pointer.data == string:
                return pointer
            else:
                pointer.visited = False
                if pointer.nFlip != None and pointer.nFlip!= "" and pointer.nFlip.visited == True:
                    self.findNode(pointer.nFlip,string)
                if pointer.n1Flip != None and pointer.nFlip!= ""  and pointer.n1Flip.visited == True:
                    self.findNode(pointer.n1Flip,string)
                if pointer.n2Flip != None and pointer.nFlip!= ""  and pointer.n2Flip.visited == True:
                    self.findNode(pointer.n2Flip,string)

class Node:
    def __init__(self,string,nodeN,nodeN1,nodeN2):
        self.data = string
        self.nFlip = nodeN
        self.nVisited = False
        self.n1Flip = nodeN1
        self.n1Visited = False
        self.n2Flip = nodeN2
        self.n2Visited = False
        self.visited = False

    def hasValidMoves(self):
        if self.nFlip.visited == False and self.nVisited == False:
            return True
        if self.n1Flip.visited == False and self.n1Visited == False:
            return True
        if self.n2Flip.visited == False and self.n2Visited == False:
            return True
        return False

    def resetNVisited(self):
        self.nVisited = False
        self.n1Visited = False
        self.n2Visited = False
        self.visited = False
