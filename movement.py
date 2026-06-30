x, y = map(int, input("Enter starting coordinates (x,y): ").split(","))   # Take both coordinates together2,

movement = input("Enter movement (horizontal= H or vertical=V): ")
steps = int(input("Enter the number of steps: "))

for _ in range(steps):
    if movement == "H":
        x += 1   # move right
    elif movement == "V":
        y += 1   # move up
    else:
        print("Invalid movement type!")
        break
    
    print(f"({x},{y})")