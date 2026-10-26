# Task 1
def most_frequent_commands(commands):
  freq = {}
  lst = []
  mx = 0
  for i in commands:
    if i not in freq:
      freq[i] = 1
    else:
      freq[i] += 1

  for cmd in freq:
    if freq[cmd] > mx:
      mx = freq[cmd]

  for i in freq:
    if freq[i] == mx:
      lst.append(i)
  lst.sort()
  return lst

commands = ["U", "L", "U", "R", "L", "D"]

print(most_frequent_commands(commands))

# Task 2
def longest_increasing_segment(readings):
  if not readings:
    return 0
  count = 1
  mx = 1

  for i in range(1, len(readings)):
    if readings[i] > readings[i - 1]:
      count += 1
    else:
      count = 1
    if count > mx:
      mx = count
  return mx


print(longest_increasing_segment([1, 2, 3, 2, 4, 5, 6]))
# Output: 4
print(longest_increasing_segment([5, 4, 3, 2]))
# Output: 1
print(longest_increasing_segment([]))
# Output: 0

# Task 3
def final_battery(mx, lst):
  start = 0
  for i in lst:
    start += i
    if start > mx:
      start = mx
  return start

print(final_battery(20, [5, 8, 12, 3]))
