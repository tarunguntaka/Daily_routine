


def climb_stairs(n):
    #n is one or two 
    # if n ==1:
    #     return 1
    # elif n==2:
    #     return 2
    # else:
    #     return climb_stairs(n-1)+climb_stairs(n-2)
    if 0<n<=2:
        return n
    steps=[0 for i in range(n)]
    steps[0]=1
    steps[1]=2 
    for i in range(2,n):
        steps[i]= steps[i-1]+steps[i-2]
    return steps[-1]


k = int(input("Enter the number:"))
print(climb_stairs(k))
