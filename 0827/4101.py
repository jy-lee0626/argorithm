import sys

while True:
  a, b = map(int, sys.stdin.readline().split())
  if not a and not b:
    break
  
  if a <= b:
    print('No')
  else:
    print('Yes')