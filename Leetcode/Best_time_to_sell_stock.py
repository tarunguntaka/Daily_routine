

def max_profit(p):
    diff={}
    for i in range (len(p)):
        diff[i] = 0
    for i in range(len(p)-1):
        for j in range(i+1,len(p)):
            k = diff[i]
            diff[i] = max((p[j]-p[i]),k)
            if diff[i]<0:
                diff[i] = 0
    d = [i for i in diff.values()]      
    print(d)
    print(diff)
    max_v = max(d)
    max_index = d.index(max_v)
    return diff[max_index]

print (max_profit([7,1,5,3,6,4]))

         