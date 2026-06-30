stored_user_id = "tan"
stored_password = "pheonix123"   # Predefined credentials

user_id = input("Enter user ID: ").lower()
password = input("Enter password: ").lower()

if user_id == stored_user_id and password == stored_password:
    print("Drone connected successfully") 
else:
    print("Invalid credentials")