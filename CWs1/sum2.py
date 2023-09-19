from itertools import combinations
list = [11,25,1,3,5,8,9]
num = 10
comb = combinations(list, 2)
for i in comb:
    if sum(i) == num:
        print(tuple(list.index(j) for j in i))
