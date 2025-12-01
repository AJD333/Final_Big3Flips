How to use:
  1. Open main.py
  2. Edit the variable "n" to be the desired length of your starting sequence. (Ex: n = 5 would yield the starting sequence "12345")
  3. Run the file.

This algorithm will print to the console every time a new longest flip sequence is found. 
It includes the number of recursions, the length of the longest currently found path, and the path itself, as represented by the string values of the sequence.

As well as that, whenever a new longest flip sequence is found, it will write the flip sequence, as represented by the n-value of the flip, to an output file corresponding to the value of n.
(Ex: n = 5, the function will output the longest sequence to "flipSeq5.txt")

The algorithm itself can be found within "Spider.py" under the function name "spider()" initialized by calling "startSpider(n)"
