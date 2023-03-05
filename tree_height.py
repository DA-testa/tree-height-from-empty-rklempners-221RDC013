# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    height = numpy.zeros(n, dtype = numpy.int32)
    max_height = 0
    
    # Your code here
    for i in range(n):
        startingheight = 0
        while i != -1:
            if height[i] !=0:
                startingheight = startingheight + height[i]
                break
            else:
                startingheight = startingheight + 1
            i = parents[i]
            height[i] = startingheight
            max_height = max(max_height, startingheight)
    return max_height


def main():
    # implement input form keyboard and from files
    input_type = input()
    
    if input_type == "F":
    # let user input file name to use, don't allow file names with letter a
        file = input()
        if 'a' in file:
            print("wrong file name")
            return
    # account for github input inprecision
        try:
            with open('test/' + file, 'r', encoding = "utf8") as f:
                n = int(f.readline())
                parents = numpy.array(list(map(int, f.readline().split())))
        except FileNotFoundError:
            print("Wrong file")
            return

        print(compute_height(n, parents))

    elif input_type == "I":            
    # input number of elements
        n = int(input())
    # input values in one variable, separate with space, split these values in an array
        parents = numpy.array(list(map(int, input().split())))
    # call the function and output it's result
        print(compute_height(n,parents))
        #pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
