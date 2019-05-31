def solution(A,B):
    fib =[0,1]
    Ba=[2]
    R=[]
    L=len(A)
    mA=max(A)
    mB=max(B)
    
    for x in range (0,mB):
        Ba.append(Ba[-1]*2)
    
    for x in range (0,mA):
        fib.append((fib[-1]+fib[-2])%Ba[mB-1])
        
    for x in range(0,L):
        R.append((fib[A[x]+1])%(Ba[B[x]-1]))
                
    return(R)