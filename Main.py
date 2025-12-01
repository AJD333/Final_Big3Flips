import Spider as S
import Builder as B
import sys

n = 7

sys.setrecursionlimit(100000000)

bitsy = S.Spider()
path = bitsy.startSpider(n)
if bitsy.success:
    print("\n### PATH SUCCESSFULY FOUND ###")
    print(f"Number of iterations: {bitsy.counter}")
    print(f"Length of path: {len(path)}")
    for i in path:
        print(f"{i.data}, ",end="")
    print()
else:
    print(path)