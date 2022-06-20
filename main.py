sort_1 = [1,3,7,8,5,7,8,9]
for i in range(len(sort_1)-1):
    for j in range(len(sort_1)-i-1):
        if sort_1[j+1]<sort_1[j]:
            sort_1[j],sort_1[j+1]=sort_1[j+1],sort_1[j]
print(sort_1)