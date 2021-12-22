#  1   2   3   4   5
# [ ] [ ] [ ] [ ] [ ]

# 0 - free
# 1 - occupied
#         0   1   2   3   4
seats = [ 0 , 0 , 0 , 0 , 0 ]  ### list. Cinema's database of its seats.

while True:

    for n in seats:        ### Demonstrates to the client free and occupied seats at the cinema
        if n == 1:
            n = "| x |"
        else:
            n = "|   |"
        print(n, end=" ")  

    print("\n------------------------------\n")

    s = int(input("Pick a seat (1..5): ")) - 1  ### INPUT. Client introduces number of the seat that he/she want to buy


    if s>=0 and s<=4:             ### Verifies whether the requested seat exists.
        if seats[s] == 0:         ### Verifies whether the requested seat is free
            print("Yes, seat", s+1, "is free!")
            confirm = input("buy (yes/no)? ")
            if confirm == "yes":  ### Verifies the client's confirmation of purchase of the seat
                if s==0 or s==4:  ### Price for the requested seat is printed
                    print("Price of the seat is 50 MDL.")
                elif s==1 or s==3:
                    print("Price of the seat is 75 MDL.")
                else:
                    print("Price of the seat is 100 MDL.")
                seats[s] = 1      ### Change of the seat's status to occupied in the cinema's database
        else:
            print("No, sorry, seat", s+1, "is occupied!")
    else:
        print("Error! Seat number", s+1, "does not exist.")
