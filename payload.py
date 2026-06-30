def drone_weight():
        # float inputs for body weight and payload weight
        body_weight = float(input("Body weight (in kg): "))
        payload_weight = float(input("Payload weight (in kg): "))
        
        # total weight calc
        total_weight = body_weight + payload_weight
        
        # Output the total weight 
        print("total weight=", total_weight, "kg")
        
        # Check if the total weight limit
        if total_weight > 2.0:
            print("Total weight is greater than 2 kg")
        else:
            print("Total weight is less than 2 kg")
     

drone_weight()