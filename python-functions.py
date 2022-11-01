# ----------------------------------- CHALLENGE 1 -----------------------------------

def sum_to(n):
  count = 1
  sum = 0
  while count <= n:
    sum += count
    count += 1
  return sum

# print(sum_to(6))

# ----------------------------------- CHALLENGE 2 -----------------------------------

def largest(list):
  num = 0
  for i in list:
    if i > num:
      num = i
  return num

# print(largest([10, 4, 2, 231, 91, 54]))

# ----------------------------------- CHALLENGE 3 -----------------------------------

def occurrences(str1, str2):
  return str1.count(str2)

# print(occurrences('fleep floop', 'e'))

# ----------------------------------- CHALLENGE 4 -----------------------------------

def product(*args):
  product = 1
  for arg in args:
    product = arg*product
  return product

# print(product(4, 0.5, 5))