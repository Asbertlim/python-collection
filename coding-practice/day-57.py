# Task 1
def count_frequency(numbers):
  freq = {}
  for number in numbers:
    if number not in freq:
      freq[number] = 1
    else:
      freq[number] += 1
  return freq

# Task 2
def remove_duplicates(numbers):
  filter = []
  for number in numbers:
    if number not in filter:
      filter.append(number)
  return filter
