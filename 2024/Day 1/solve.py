left_hand_side = []
right_hand_side = []

with open("input", "r") as f:
    for line in f.readlines():
        dataset = line.strip()
        value = dataset.split(" ")
        left_hand_side.append(int(value[0]))
        right_hand_side.append(int(value[3]))
    
sorted_lhs = sorted(left_hand_side)
sorted_rhs = sorted(right_hand_side)

distance1 = 0
distance2 = 0
similarity = 0

for i, j in zip(sorted_rhs, sorted_lhs):
    distance1 += abs(i - j)

print(distance1)

for i in sorted_lhs:
    count = 0
    for j in sorted_rhs:
        if i == j:
            count += 1
    
    similarity += i * count

print(similarity)
