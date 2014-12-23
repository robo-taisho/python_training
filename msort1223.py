#coding: UTF-8

def merge_sort(alist):
  if len(alist) < 2:
    return alist
  else:

    mid = len(alist)//2
    left = alist[:mid]
    right = alist[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)


def merge(left,right):
  l = r = 0
  ans = []
  while l < len(left) and r < len(right):
    if left[l] < right[r]:
      ans.append( left[l])
      l = l + 1
    else:
      ans.append(right[r])
      r = r + 1

  while l < len(left):
    ans.append(left[l])
    l = l + 1

  while r < len(right):
    ans.append(right[r])
    r = r + 1

  return ans


import random

def generate(n):
  return [random.randint(0,100) for _ in xrange(n)]

a = generate(20)
print a
print merge_sort(a)
