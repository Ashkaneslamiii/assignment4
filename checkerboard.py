import numpy as np
def checkerboard():
    print("what is your preference:")
    n = int(input())
    m = int(input())
    # creat a n*n Matrix
    x = np.zeros((n,m), dtype = int)
    # fill with 1 the alternate row 
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1

    #print the pattern
     
    for i in range (n):
        for j in range(m):
            print(x[i][j], end = "")
        print()
        
checkerboard()


