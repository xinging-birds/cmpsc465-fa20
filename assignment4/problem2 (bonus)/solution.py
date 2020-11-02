"""
PA4 Prob 2
Justin Huang (jfh5730)
Divyesh Johri (dkj5225)
Eddie Ubri (evu5018)
"""

# Dynamic programming solution to LIS for palindromes.
# Inputs: seq = sequence of letters, n = |seq|
# Outputs: length of longest subsequent palindrome
# Runtime: O(n * n)
def lis_palindrome(seq, n): 
  
    # Create DP table for l(i,j), where i and j are beginning and end pointers 
    # to a subtring of the sequence (i.e. seq[i:j]).
    l = [[0 for _ in range(n)] for _ in range(n)] 
  
    # Initialize the diagonal of the DP table to 1. The rest will remain 0.
    for x in range(n): 
        l[x][x] = 1
  
    # Recursively solve subproblems l[i][j]
    # sub is the current length of the substring seq[i] to seq[j]
    for sub in range(2, n + 1): 
        for i in range(n-sub + 1): 
            j = i + sub - 1
            if seq[i] == seq[j] and sub == 2:   
                # if only two characters that are the same, length is just 2
                l[i][j] = 2
            elif seq[i] == seq[j]:  
                # new palindrome -> l[inner seq] + 2 is the new max length
                l[i][j] = l[i+1][j-1] + 2
            else: 
                # No palindrome, meaning longest palindrome is max of l[inner seq]
                l[i][j] = l[i][j-1] if l[i][j-1] > l[i+1][j] else l[i+1][j]
    
    # return the solution
    return l[0][n-1]


# Initialize variables
sequence = input()
n = len(sequence)

# Find longest subsequent palindrome
print(lis_palindrome(sequence, n))
