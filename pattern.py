def printing(n):
    
    print(" ",end="")
    for i in range(n-2):
        
        print("*",end="")
    print()
    n=n+1
    
    for i in range(n//2):
        for j in range(i):
            print(" ",end="")
        for k in range(n-1-2*i):
            print("*",end="")
        print()
printing(15)
        