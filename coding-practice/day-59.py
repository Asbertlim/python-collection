def most_frequent_command(commands):
  freq = {}
  highest = 0
  for  cmd in commands:
    if cmd not in freq:
      freq[cmd] = 1
    else:
      freq[cmd] += 1

  for i in freq:
    if freq[i] > highest:
      highest = freq[i]
      highest_cmd = i
  return highest_cmd
  
def remove_consecutive_duplicates(states):
  if not states:
    return []
    
  lst = [states[0]]
  for i in range(1, len(states)):
    if states[i] != states[i-1]:
      lst.append(states[i])
  return lst

