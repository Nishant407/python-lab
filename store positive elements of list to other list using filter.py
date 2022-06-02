def pos(x):
    if(x>0):
        return True
    else:
        return False
l=list(map(int,input().split()))
l1=list(filter(pos,l))
print(l1) 
