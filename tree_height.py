# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    #height = numpy.zeros(n, dtype = numpy.int32)
    #max_height = 0
    children = {}
    for i in range(n):
        children[i] = []
    for i in range(n):
        if parents[i] != -1:
            children[parents[i]].append(i)
    
    depths = [-1] * n
    stack = [(i, 1) for i in range(n) if parents[i] == -1]
    while stack:
        node, depth = stack.pop()
        depths[node] = depth
        for child in children[node]:
            stack.append((child, depth + 1))

    return max(depths)    
    # Your code here
    #for i in range(n):
        #starting_height = 0
        #current_node = i
        #while current_node != -1:
            #if height[current_node] != 0:
                #starting_height = starting_height + height[current_node]
                #break
            #else:
                #starting_height = starting_height + 1
            #current_node = parents[current_node]
            #if current_node == -1:
                #starting_height = 1
            #height[i] = starting_height
        #max_height = max(max_height, starting_height)
    #return max_height


def main():
    # implement input form keyboard and from files
    input_type = input()
    
    if input_type == "F":
    # let user input file name to use, don't allow file names with letter a
        file = input()
        #if "a" in file:
            #print("wrong file name")
            #return
    # account for github input inprecision
        #try:
        #else:
        with open("test/" + file, mode = 'r', encoding = "utf8") as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().split().strip()))
            height = compute_height(n, parents)
            print(height)
        #except FileNotFoundError:
            #print("Wrong file")

        #print(compute_height(n, parents))

    elif input_type == "I":            
    # input number of elements
        n = int(input())
    # input values in one variable, separate with space, split these values in an array
        parents = list(map(int, input().split()))
    # call the function and output it's result
        height = compute_height(n, parents)
        print(height)
        #print(compute_height(n,parents))
        #pass
    #else:
        #print("Nepareiza")

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
