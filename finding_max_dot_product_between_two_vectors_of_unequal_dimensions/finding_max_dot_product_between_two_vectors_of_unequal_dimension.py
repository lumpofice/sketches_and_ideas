u = [1,-1,1,1,1,-1,1,1,1]
v = [1,-1,1,1,-1,1]
def max_output(u,v):
    """This function finds the maximum of the following set:
{\sum_{i = 1}^{6}(u[j+i]*v[i]) such that j belongs to {0, 1, 2, 3}}.
The summation statement \sum_{i = 1}^{6}(u[j+i]*v[i])
has been written in LaTeX notation. It means:
The sum from 1 to 6 of the coordinate products of u and v.
The coordinates of v run from 1 through 6 for each member of the set,
while the coordinates of u run from
1 to 6 for the first member of the set
2 to 7 for the second member of the set
3 to 8 for the third member of the set
4 to 9 for the fourth member of the set.
Of course, python rolls every index back one unit, starting at
0 as opposed to 1. The above indices, which start at 1, are used to
communicate what is happening mathematically. Thus, python-wise:
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
        for i in range(len(v)):
            product = u[j]*v[i]
            product_list.append(product)
            j += 1
        sum_list.append(sum(product_list))
    return max(sum_list)

output = max_output(u,v)
print(output)