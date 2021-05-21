mangA=[2,3,4,5,6,2,0,1]
mangB=[]
for i in range(len(mangA)):
    i = mangA.index(min(mangA))
    mangB.append(mangA[i])
    mangA.remove(mangA[i])
print(mangB)