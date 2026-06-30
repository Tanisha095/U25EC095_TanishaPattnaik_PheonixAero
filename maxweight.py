max_takeoff_weight = 4.5  # kg float 
frame_weight = 1.2        # kg float
battery_weight = 0.8      # kg float
num_propellers = 4        # int
motor_weight = 0.075      # kg per motor float
is_gps_enabled = True     # bool
gps_module_weight = 0.05  # kg float

total_motor_weight = num_propellers * motor_weight

if (is_gps_enabled):
    gps_weight = gps_module_weight   #gps module weight is taken into consideration only if it is enabled

else:
    gps_weight = 0

# Calculate maximum payload
max_payload = max_takeoff_weight - (frame_weight + battery_weight + total_motor_weight + gps_weight)
print("Maximum payload (kg):", max_payload)

# 2. Print type of each variable
print(type(max_takeoff_weight))
print(type(frame_weight))
print(type(battery_weight))
print(type(num_propellers))
print(type(motor_weight))
print(type(is_gps_enabled))
print(type(gps_module_weight))

# 3. Check if payload can carry 1.8 kg camera 
if (max_payload>= 1.8):
    print("Can carry 1.8 kg camera:", True)
else:
    print("Can carry 1.8kg camera: ", False) 

# 4. Convert max_takeoff_weight to grams (int)
max_takeoff_weight_grams = int(max_takeoff_weight * 1000)
print("Max takeoff weight (grams):", max_takeoff_weight_grams)