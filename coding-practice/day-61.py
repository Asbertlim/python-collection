# Task 1
def calculate_totals(results):
  scores = {}
  for result in results:
    if result[0] not in scores:
      scores[result[0]] = result[1]
    else:
      scores[result[0]] += result[1]
  return scores

results = [
    ("Alex", 10),
    ("Ben", 15),
    ("Alex", 20),
    ("Cara", 12),
    ("Ben", 5),
    ("Cara", 18)
]
print(calculate_totals(results))

# Task 2
def longest_unique_segment(readings):
  seen = set()
  count = 1
  best = 0
  
  if len(set(readings)) == 1:
      return 1
  if readings == []:
    return 0
  for reading in readings:
    if reading not in seen:
      seen.add(reading)
      count += 1
    else:
      count = 1
    if count > best:
      best = count
  return best
readings = [1, 2, 3, 2, 4, 5]
print(longest_unique_segment(readings))

# Task 3
def minimum_coins(amount):
  coins = [1, 5, 10, 25]
  total = 0
  count = 0
  i = 3

  if amount == 0:
    return 0
  while True:
    if amount > total:
      total += coins[i]
      count += 1
    elif total > amount:
      total -= coins[i]
      i -= 1
      count -= 1
    if amount == total:
      break
  return count

print(minimum_coins(36))
