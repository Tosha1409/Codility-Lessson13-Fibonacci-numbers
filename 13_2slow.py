def search (d,f,r,be,bea,j):
    if (r<be-1) or (be==-1):
        a=sum(d)
        l=len(d)-1
        lj=len(j)
        for x in range(l,-1,-1):
            if (x!=l): a-=d[x+1]
            if a in f:
                b=d[x+1:]
                r +=1
                bea.append(a)
                tmp=sum(bea)
                if j[tmp]>r: 
                    j[tmp]=r
                    if b != []: be=search (b,f,r,be,bea,j)
                    elif (be == -1) or (r<be): be=r     
                r -= 1
                bea.pop()
    return(be)
                    
def solution(A):
    L=len(A)
    fib =[0,1]
    distances=[]
    count=0
    jumps=[L+2]*(L+2)
    
    #getting fibonaci numbers
    for x in range (0,L+1):
        tmp=fib[-1]+fib[-2]
        if tmp<=L+1: fib.append(tmp)
        else: break
    fib= fib[2:]
    
    #getting distances for possible jumps
    i=0
    for x in A:
        i += 1
        if x==1:
            distances.append(i)
            i=0
    distances.append(i+1)
    
    tmp = search (distances,fib, 0, -1, [],jumps)
    return(tmp)