# Using sort
def smallest_missing(numbers):
  numbers = list(set(numbers))
  numbers.sort()

  smallest = 1
  for i in numbers:
    if i < smallest:
      continue
    elif i == smallest:
      smallest += 1
    else:
      return smallest
      
  return smallest

print(smallest_missing([-2,1,2,2,9,8,8]))

# Using O(n) without sort

def smallest_missing(numbers):
  numbers = set(numbers)
  smallest = 1

  while True:
    if smallest in numbers:
      smallest += 1
    else:
      return smallest

print(smallest_missing([-2,1,2,2,9,8,8]))
