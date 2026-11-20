# Zadanie 3-31
arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_val = arr[0][0]
min_pos = (0, 0)
max_val = arr[0][0]
max_pos = (0, 0)

for r_idx, row in enumerate(arr):
    for c_idx, val in enumerate(row):
        if val < min_val:
            min_val = val
            min_pos = (r_idx, c_idx)
        if val > max_val:
            max_val = val
            max_pos = (r_idx, c_idx)

print(f"Smallest value: {min_val} at row {min_pos[0]}, column {min_pos[1]}")
print(f"Largest value: {max_val} at row {max_pos[0]}, column {max_pos[1]}")