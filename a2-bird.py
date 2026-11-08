tree_count = int(input())
tree_tall = input().split(" ")
print(tree_count,tree_tall)
high = []
bird = 0
for a in tree_tall:
    high.append(int(a))
for i in range(tree_count):
    if i == 0:
        if high[0] > high[i + 1]:
            bird += 1
    elif i == tree_count - 1:
        if high[i] > high[i - 1]:
            bird += 1
    else:
        if high[i] >high[i - 1] and high[i] >high[i + 1]:
            bird += 1

print(bird)

    