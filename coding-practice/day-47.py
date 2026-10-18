# Task 1
def max_activities(activities):
    result = sorted(activities, key=lambda x:x[1])
    end = result[0][1]
    count = 1
    for item in result:
        if end <= item[0]:
            end = item[1]
            count += 1
    return count

# Task 2
def get_times(meetings):
    sorted_start = sorted(meetings, key=lambda x:x[0])
    starts = []
    for item in sorted_start:
        starts.append(item[0])
        
    sorted_end = sorted(meetings, key=lambda x:x[1])
    ends = []
    for item in sorted_end:
        ends.append(item[1])

    return starts, ends

def min_room(meetings):
    starts, ends = get_times(meetings)
    i = 0
    j = 0
    rooms = 0
    max = 0

    while i < len(starts):
        if starts[i] < ends[j]:
            rooms += 1
            if rooms > max:
                max = rooms
            i += 1
        else:
            rooms -= 1
            j += 1
        
    return max
          
