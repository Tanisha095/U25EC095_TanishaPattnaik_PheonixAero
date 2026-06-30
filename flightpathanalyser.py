altitudes = [0, 15, 42, 78, 120, 118, 115, 50, 20, 0]

# 1. Maximum altitude and the second it occurred
max_alt = max(altitudes)
print("the maximum altitude attained is:", max_alt)
alt_len= len(altitudes)
for i in range(alt_len):
    if altitudes [i]==max_alt:
        print(f"max altitude occured at {i}th second")

# 2. Average altitude (round to 2 decimals)
avg_alt = round(float(sum(altitudes) / len(altitudes)), 2)
print("Average altitude:", avg_alt)

# 3. Climb rates list
for i in range(alt_len-1):
    climb_rates = [altitudes[i+1] - altitudes[i]]

print("Climb rates:", climb_rates)

# 4. Steepest climb and descent
steepest_climb = max(climb_rates)
steepest_descent = min(climb_rates)

print("Steepest climb:", steepest_climb)
print("Steepest descent:", steepest_descent)

# 5. Remove zero-altitude entries
for i in range(alt_len-1):
    if altitudes[i]==0:
        altitudes.remove(altitudes[i])

print("Trimmed path:", altitudes)