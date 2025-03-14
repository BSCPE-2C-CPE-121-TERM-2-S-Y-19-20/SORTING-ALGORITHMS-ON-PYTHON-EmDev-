def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)

    #  print("After increments of size",sublistcount, "The list is",nlist)

      sublistcount = sublistcount // 2

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap

        nlist[position]=current_value


user_input = input("Input numbers separated a coma:\t").strip()
nlist = [int(item) for item in user_input.split(',')]
print("Array before sorting: \t", nlist)
shellSort(nlist)
print("Array After sorting: \t", nlist)

