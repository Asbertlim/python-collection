def first_repeated(numbers):
  seen = set()
  for number in numbers:
    if number in seen:
      return number
    else:
      seen.add(number)
  return None

print(first_repeated([4, 2, 7, 2, 4]))  # 2
print(first_repeated([1, 3, 5, 7]))     # None
print(first_repeated([9, 9, 2, 2]))     # 9
print(first_repeated([3, 1, 3, 1]))     # 3

def longest_increasing(numbers):
  if len(numbers) == 0:
    return 0
    
  count = 1
  max = 1
  for i in range(len(numbers)-1):
    if numbers[i+1] > numbers[i]:
      count += 1
    else:
      count = 1

    if count > max:
      max = count
  return max

print(longest_increasing([1, 2, 3, 1, 2, 5, 6]))  # 4
print(longest_increasing([5, 4, 3, 2]))           # 1
print(longest_increasing([1, 2, 2, 3]))           # 2
print(longest_increasing([]))                     # 0

def complete_jobs(budget, jobs):
  completed_jobs = 0
  remaining_energy = budget

  for job in jobs:
    if remaining_energy >= job:
      remaining_energy -= job
      completed_jobs += 1
  return (completed_jobs, remaining_energy)

print(complete_jobs(10, [3, 4, 5, 2]))  # (3, 1)
print(complete_jobs(8, [9, 2, 3]))      # (2, 3)
print(complete_jobs(5, []))             # (0, 5)
