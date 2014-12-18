#coding : UTF-8

def merge_sort(alist):
  if len(alist) > 1:
    mid = len(alist) // 2

    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    merge_sort(lefthalf)
    merge_sort(righthalf)

    i = l = r = 0

    while len(lefthalf) > l and len(righthalf)>r:
      print i
      if lefthalf[l] < righthalf[r]:
        alist[i]=lefthalf[l]
        l = l + 1
      else:
        alist[i] = righthalf[r]
        r = r + 1
      i = i + 1 

    while len(lefthalf) > l:
      alist[i] = lefthalf[l]
      i = i + 1
      l = l + 1

    while len(righthalf) > r:
      alist[i] = righthalf[r]
      i = i + 1
      r = r + 1
    
array_a = [2,4,7,5,3,2]
merge_sort(array_a)
print array_a
