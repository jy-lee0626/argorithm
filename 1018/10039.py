import sys

total = 0

for i in range(5):
  score = int(sys.stdin.readline().rstrip())
  if score < 40:
    score = 40
  total += score

print(total//5)