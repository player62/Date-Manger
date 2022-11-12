diclist = []

dic1 = {}
dic2 = {}
dic3 = {}

diclist.append(dic1)
diclist.append(dic2)
diclist.append(dic3)

#요일,시간

dic1[(1, 1)] = 1
dic1[(1, 2)] = -1
dic1[(2, 1)] = 1
dic1[(2, 2)] = 1

dic2[(1, 1)] = 0
dic2[(1, 2)] = -1
dic2[(2, 1)] = 1
dic2[(2, 2)] = 0

dic3[(1, 1)] = 1
dic3[(1, 2)] = 1
dic3[(2, 1)] = -1
dic3[(2, 2)] = 0


newdic = {}

for i in range(2):
    for j in range(2):
        newdic[(i + 1, j + 1)] = 0
        for k in range(len(diclist)):
            newdic[(i + 1, j + 1)] += diclist[k].get((i + 1, j + 1))

print(newdic)
