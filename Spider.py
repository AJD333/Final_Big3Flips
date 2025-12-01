import OtherClasses as C
import Builder as B
class Spider:
    def __init__(self):
        self.counter=0
        self.current = None
        self.done = False
        self.lastMove = ""
        self.longestFound = 0
        self.n = 0
        self.path = []
        self.starting = None
        self.success = False
        self.threshold = 0
        self.triggered = False
        self.web = None

    def startSpider(self,n):
        string = ""
        for i in range(0,n):
            string = string+f"{i+1}"
        self.makeWeb(string)
        self.threshold = self.factorial(n)
        self.current = self.web.head
        self.starting = self.web.head
        self.path = [self.web.head]
        self.n = n
        return self.spider()

    def makeWeb(self, string):
        header = C.Node(string, "", "", "")
        web = C.PancakeStack(header)
        B.linkNodes(header, [], web)
        self.web = web

    def spider(self):
        while not self.done:
            self.counter+=1

            if len(self.path) > self.longestFound:
                self.longestFound = len(self.path)
                print(f"\nIteration: {self.counter}")
                print(f"Length of path: {len(self.path)-1}")
                if self.n<8:
                    for i in self.path:
                        print(f"{i.data}, ",end="")
                    print()
                with open(f"flipSeq{self.n}.txt","w") as f:
                    for j in range(0,len(self.path)-1):
                        if self.path[j].nFlip == self.path[j+1]:
                            f.write(f"{self.n} ")
                        elif self.path[j].n1Flip == self.path[j+1]:
                            f.write(f"{self.n - 1} ")
                        elif self.path[j].n2Flip == self.path[j+1]:
                            f.write(f"{self.n - 2} ")

            if len(self.path) == 1 and self.hasValidMoves() == False:
                self.done = True
                return False

            if len(self.path) == self.threshold and self.checkWrapAround():
                self.done = True
                self.success = True
                self.outputToFile()
                return self.path.copy()

            self.current.visited = True
            if self.hasValidMoves():
                if not self.current.n2Flip.visited and not self.current.n2Visited and not self.done:
                    self.current.n2Visited = True
                    self.current = self.current.n2Flip
                    self.current.visited = True
                    self.path.append(self.current)
                    self.lastMove = "n2"

                elif not self.current.nFlip.visited and not self.current.nVisited and not self.done:
                    self.current.nVisited = True
                    self.current = self.current.nFlip
                    self.current.visited = True
                    self.path.append(self.current)
                    self.lastMove = "n"

                elif not self.current.n1Flip.visited and not self.current.n1Visited and not self.done:
                    self.current.n1Visited = True
                    self.current = self.current.n1Flip
                    self.current.visited = True
                    self.path.append(self.current)
                    self.lastMove = "n1"

                if len(self.path) == self.threshold and self.checkWrapAround():
                    self.done = True
                    self.success = True
                    self.outputToFile()
                    return self.path.copy()
            else:
                if self.hasValidMoves()==False and len(self.path) > 1:
                    self.current.resetNVisited()
                    self.path = self.path[:len(self.path) - 1]
                    self.current = self.path[-1]
                    if len(self.path)>1 and ((len(self.path)<=self.n*12 and self.triggered == False) or self.lastMove=="n1"):
                        self.triggered = True
                        self.current.resetNVisited()
                        self.path = self.path[:len(self.path) - 1]
                        self.current = self.path[-1]
                    self.resetLastMove()



### HELPER FUNCTIONS ###

    def hasValidMoves(self):
        return self.current.hasValidMoves() and not self.checkStartingNeighbours()

    def checkStartingNeighbours(self):
        return (self.starting.nFlip.visited) and (self.starting.n1Flip.visited) and (self.starting.n2Flip.visited)

    def checkWrapAround(self):
        return (self.current.nFlip == self.starting) or (self.current.n1Flip == self.starting) or (self.current.n2Flip == self.starting)

    def factorial(self,n):
        if n == 1:
            return n
        else:
            return n * self.factorial(n - 1)

    def resetLastMove(self):
        second = self.path[-2]
        if second.nFlip == self.current:
            self.lastMove = "n"
        elif second.n1Flip == self.current:
            self.lastMove = "n1"
        elif second.n2Flip == self.current:
            self.lastMove = "n2"

    def outputToFile(self):
        with open(f"flipSeq{self.n}.txt", "w") as f:
            for j in range(0, len(self.path) - 1):
                if self.path[j].nFlip == self.path[j + 1]:
                    f.write(f"{self.n} ")
                elif self.path[j].n1Flip == self.path[j + 1]:
                    f.write(f"{self.n - 1} ")
                elif self.path[j].n2Flip == self.path[j + 1]:
                    f.write(f"{self.n - 2} ")
            j = len(self.path) - 1
            if self.path[j].nFlip == self.path[0]:
                f.write(f"{self.n} ")
            elif self.path[j].n1Flip == self.path[0]:
                f.write(f"{self.n - 1} ")
            elif self.path[j].n2Flip == self.path[0]:
                f.write(f"{self.n - 2} ")