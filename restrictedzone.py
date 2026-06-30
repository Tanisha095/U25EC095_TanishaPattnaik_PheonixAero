planned_zones = {"Z1", "Z2", "Z3", "Z5", "Z7"}
restricted_zones = {"Z3", "Z5", "Z6", "Z8"}
cleared_zones = {"Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8"}

# 1. Planned zones that are restricted (intersection)
restricted_planned = planned_zones & restricted_zones
print("Restricted planned zones:", restricted_planned)

# 2. Planned but NOT restricted (safe zones)
safe_zones = planned_zones - restricted_zones
print("Safe zones:", safe_zones)

# 3. Zones in either but NOT both (symmetric difference)
conflict_zones = planned_zones ^ restricted_zones
print("Symmetric difference zones:", conflict_zones)

# 4. Check subset
if planned_zones.issubset(cleared_zones):
    print("All planned zones are cleared for flight ")
else:
    print("Some planned zones are NOT cleared ")

# 5. Modify planned zones
planned_zones.add("Z9")
planned_zones.discard("Z7")  
print("Updated planned zones:", planned_zones)

# 6. Count unique zones across all sets
all_zones = planned_zones | restricted_zones | cleared_zones
print("Total unique zones:", len(all_zones))