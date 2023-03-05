# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    height = numpy.zeros(n)

    def what_is_the_height(node):
        if height[node] != 0:
            return height[node]
        
        if parents[node] == -1:
            height[node] = 1

        else:
            height[node] = 1 + what_is_the_height(parents[node])    

        return height[node]
    
    max_height = 0
    
    # Your code here
    for i in range(n):
        max_height = max(max_height, what_is_the_height(i))
    
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
            with open('folder/' + file, 'r') as f:
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
        pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))