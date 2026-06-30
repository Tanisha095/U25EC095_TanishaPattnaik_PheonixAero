def drone_movement(option):
    if (option==1):{  #1=roll
        print ("slow down left motors and speed up right motors for left roll or slow down right motors and speed up left motors for right roll")
    }
    elif (option==2):{ #2=pitch
        print ("slow down front motors and speed up rear motors for forward pitch or slow down rear motors and speed up front motors for backward pitch")
    }
    elif (option==3):{ #3=yaw 
        print ("slow down clockwise motors and speed up counter-clockwise motors for clockwise yaw or slow down counter-clockwise motors and speed up clockwise motors for counter-clockwise yaw ")
    }
    else :
        print("INVALID INPUT")

option=int(input("Enter your choice of movement (1.Roll, 2.Pitch, 3.Yaw) : "))
drone_movement(option)