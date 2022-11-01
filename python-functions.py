# CHALLENGE 1

def sum_to(n):
  count = 1
  sum = 0
  while count <= n:
    sum += count
    count += 1
  return sum

print(sum_to(6))