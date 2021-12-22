big_ship = int(input("Introduce coordinates of the big ship: "))  ### INPUT. Coordinates of the ship are introduced.
for x in range(1,11):
    if x == big_ship:                            ### Verifies whether the coordinates of the central part of the ship are found                        
        print("W", end="" )                      ### Central part of the ship is printed if the condition is respected
    elif x == big_ship - 1 or x== big_ship +1:   
        print("w", end="" )                      ### Margin of the ship is printed if at least one of the conditions is respected
    else:                                        
        print( "~", end="" )                     ### Water symbols are printed in other cases