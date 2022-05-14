'''from turtle import right


def mayorelem(l: list):
    if len(l) == 1:
        return l[0]
    else:
        primera = mayorelem(l[:len(l)//2])
        segunda = mayorelem(l[len(l)//2:])
        if primera > segunda:
            return primera
        else:
            return segunda


l = [1, 2, 4, 6, 3, 9, 1, 65, 235, 45, 467, 23, 12, 0, 12, 1000]
print(mayorelem(l))'''


'''def mergesort(l: list):
    if len(l) == 1:
        return l
    else:
        primera = l[:len(l)//2]
        segunda = l[len(l)//2:]

        return merge(primera, segunda)


def merge(l1, l2):
    i = 0
    j = 0
    aux=[]
    while i < len(l1) and j < len(l2):
        if l1[i]<l2[j]:
            aux.append(l1[i])
            i+=1
        elif l1[i]>l2[j]:
            aux.append(l2[j])
            j+=1
        else:
            aux.append(l2[j])
            aux.append(l1[i])
            i+=1
            j+=1
    return aux
print(mergesort(l))'''

def quicksort(l):
    if len(l) <= 1:
        return l
    else:
        pivote = l[0]
        menores = [x for x in l[1:] if x < pivote]
        mayores = [x for x in l[1:] if x >= pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

l=[1,2,435,2,465,78,782,34,68623,487652,38,73,59,234,873,49]
print(quicksort(l))