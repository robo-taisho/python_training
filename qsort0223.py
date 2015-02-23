#coding : UTF-8

import random

def generate(n):
  return [random.randint(0,100) for _ in xrange(n)]

def qsort(alist):
  if len(alist) < 2:
    return alist
  else:
    left = []
    right = []
    for i in range(1, len(alist)):
      if alist[i] > alist[0]:
        right.append(alist[i])
      else:
        left.append(alist[i])

  left = qsort(left)
  right = qsort(right)

  ans = []
  ans += left
  ans.append(alist[0])
  ans += right

  return ans

alist = generate(20)
print alist
print qsort(alist)

