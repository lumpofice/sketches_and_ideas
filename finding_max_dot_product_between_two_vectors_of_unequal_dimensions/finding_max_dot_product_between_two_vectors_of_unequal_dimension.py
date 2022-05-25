import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -'
    ' %(message)s')

# The vectors u and v below will be used in a demonstration of how the
# following function finds the maximum of possible dot products of vector v
# and all possible index-truncated vector u

logging.debug('Start of program' + f'\n')

u = [1,-1,1,1,1,-1,1,1,1]
v = [1,-1,1,1,-1,1]

# The value of the return statement, for the two given vectors u and v above,
# should be 2

def max_output(u,v):
    """This function finds the maximum of the following set, written in
LaTeX typeset:

\{\sum_{i = 1}^{6}(u[j+i]*v[i]) such that j belongs to {0, 1, 2, 3}\}

-------------------------------------------------------------
-------------------------------------------------------------
The summation statement \sum_{i = 1}^{6}(u[j+i]*v[i]) means:
The sum from 1 to 6 of the coordinate products of u and v.

The coordinates of v run from 1 through 6 for each member of the set,
while the coordinates of u run from
1 to 6 for the first member of the set
2 to 7 for the second member of the set
3 to 8 for the third member of the set
4 to 9 for the fourth member of the set.

Of course, python rolls every index back one unit, starting at
0 as opposed to 1. In the above, indices are used to
communicate what is happening mathematically.

Thus, python-wise:
The coordinates of v run from 0 through 5 for each member of the set,
while the coordinates of u run from
0 to 5 for the first member of the set
1 to 6 for the second member of the set
2 to 7 for the third member of the set
3 to 8 for the fourth member of the set."""
    
    sum_list = []
    
    for j in range(len(u)+1):
        if j >= 4:
            break
        product_list = []
        
        # For the given j, we run through each index of vector v
        
        for i in range(len(v)):
            product = u[j]*v[i]
            product_list.append(product)
            j += 1
        
        # We append the resulting sum, generated for this given j, to the
        # sum_list above.
        
        sum_list.append(sum(product_list))
    return max(sum_list)

# The value of the return statement, for the two given vectors u and v above,
# should be 2

output = max_output(u,v)
print(output)