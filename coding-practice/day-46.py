# Task 1
def rank_scores(scores):
  result = sorted(scores, key = lambda x :x[1], reverse = True )
  lst = []
  for i in result:
    lst.append(i[0])
  return lst

print(rank_scores(scores = [
    ("Ali", 75),
    ("Ben", 92),
    ("Chen", 84),
    ("Devi", 92)
]))

# Task 2

def top_three_scores(nums):
  new = set(nums)
  result = sorted(new, reverse = True)
  return result[:3]
