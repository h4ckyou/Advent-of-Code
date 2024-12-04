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

for i, j in zip(sorted_rhs, sorted_lhs):

    max_val = max(i, j)
    min_val = min(i, j)
    distance1 += max_val - min_val

print(distance1)

for i in range(len(sorted_lhs)):
    distance2 += sorted_rhs[i] - sorted_lhs[i]
    if sorted_rhs[i] - sorted_lhs[i] < 0:
        print("negative")
        break

print(distance2) 
