def solution(A):
    L=len(A)
    fib =[0,1]
    jumps=[0]+[L+2]*(L+1)
    
    #getting fibonaci numbers
    for x in range (0,L+1):
        tmp=fib[-1]+fib[-2]
        if tmp<=L+1: fib.append(tmp)
        else: break
    fib= fib[2:]
    
    #checking if is possible to reach end by one jump, if yes then other calculations doesnt make sense
    if (fib[-1]==L+1): return (1)
    
    for x in range (0, len(jumps)):
        if jumps[x]<(L+2):
            t=jumps[x]+1
            for y in fib:
                if x+y>L+1: break
                elif x+y==L+1 or A[x+y-1]==1: jumps[x+y]=min(t,jumps[x+y]) 
    
    if jumps[L+1]==L+2: jumps[L+1]=-1
    
    return(jumps[L+1])