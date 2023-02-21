def solution(people, limit):
    people.sort()
    front, end = 0, len(people)-1
    count = 0
    while front < end:
        if people[front] + people[end] <= limit:
            front += 1
        end -= 1
        count += 1
            
    return count + (1 if front == end else 0)