waypoints = (
("WP1", 23.0225, 72.5714, 50),
("WP2", 23.0312, 72.5801, 80),
("WP3", 23.0401, 72.5900, 100),
("WP4", 23.0225, 72.5714, 0),
)

# 1.Print total number of waypoints

count = 0;
for i in waypoints:
    if ("WP" in i[0] ):
        count+=1
print("the total no of waypoints are:", count)

#2. tuple unpacking to print each waypoint's details in a formatted line

for i in waypoints:
    print(f"waypoint {i[0]} is located on the latitude {i[1]} and longitude {i[2]} at an altitude of {i[3]}m ")

#3. Finds the waypoint with the highest altitude using a loop

altitudes=[]
for i in waypoints:
    altitudes.append(i[3])

print(f"the highest altitude is: {max(altitudes)}m ")

#4. Check if ("WP2", 23.0312, 72.5801, 80) exists 
if (("WP2", 23.0312, 72.5801, 80) in waypoints):
    print(True)
else:
    print(False)

#5. Try to modify WP1's altitude to 60. Catch the error and print: "Waypoint data is immutable — mission integrity protected!"
try:
    waypoints[0][3] = 60  
except TypeError:
    print("Waypoint data is immutable — mission integrity protected!")