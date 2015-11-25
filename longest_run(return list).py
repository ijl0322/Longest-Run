def longestrun(L):
    """
    Find the longest run of monotonically increasing numbers in list L 
    and returns a list that contains the longest run. 
    L: A list of integers 
      
    """
    current = L[0:1]
    max_val = current
    for i in range(1,len(L)):
        
        if L[i] >= L[i-1]:
            current.append(L[i])
        elif L[i] < L[i-1]:
            current = []
            current.append(L[i])
            if len(current) > len(max_val):
                max_val = current
                
    if len(current) > len(max_val):
        max_val = current
        
    return max_val

L = [1, 1, 2, 1, 1]
print longestrun(L)