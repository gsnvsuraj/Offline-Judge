def costing(ini,fin,x,y):
    cost = 0
    for i,j in zip(ini,fin):
        if i > j:
            cost += (i-j)*y
        else:
            cost += (j-i)*x
            
    return cost

t = int(raw_input())
output = []

for _ in range(t):
    n,x,y = list(map(int,raw_input().split()))
    #x = int(raw_input())
    #y = int(raw_input()) #list(map(int,raw_input().split()))
    ini = []
    fin = []
    
    for _ in range(n):
        a, b = list(map(int,raw_input().split()))
        ini.append(a)
        fin.append(b)
        
    ini.sort()
    fin.sort()
    
    cost = costing(ini,fin,x,y)
    output.append(cost)
        
for i in output:
    print i
