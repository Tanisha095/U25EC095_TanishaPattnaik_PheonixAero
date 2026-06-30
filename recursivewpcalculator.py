def distance(x1, y1, x2, y2): # Distance formula 
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def total_distance(waypoints, i=0):   # Total recursive distance
    # Base case
    if i >= len(waypoints) - 1:
        return 0
    
    x1, y1 = waypoints[i]
    x2, y2 = waypoints[i + 1]
    
    return distance(x1, y1, x2, y2) + \
           total_distance(waypoints, i + 1)


# Longest leg
def find_longest_leg(waypoints, i=0, max_dist=0):
    # Base case
    if i >= len(waypoints) - 1:
        return max_dist
    
    x1, y1 = waypoints[i]
    x2, y2 = waypoints[i + 1]
    
    current = distance(x1, y1, x2, y2)
    max_dist = max(max_dist, current)
    
    return find_longest_leg(waypoints, i + 1, max_dist)

waypoints = [(0,0), (3,4), (6,8), (10,8), (10,0)]

print("Total Distance:", total_distance(waypoints))
print("Longest Leg:", find_longest_leg(waypoints))