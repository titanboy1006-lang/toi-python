bowl_count = int(input(""))
count = {}

for i in range(bowl_count):
    plate  = int(input())
    if plate in count:
        count[plate] +=1
    else:
        count[plate] = 1

answer = max(count.values())
print(answer)