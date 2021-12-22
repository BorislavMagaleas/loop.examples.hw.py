start_n = int(input("Introduce first number of the range: "))
end_n   = int(input("Introduce last number of the range: "))

if start_n < end_n:          ### Case 1. When first number of the range is less than the last.
    while start_n <= end_n:  
        print(start_n)       ### prints range in ascending order
        start_n += 1
elif start_n > end_n:        ### Case 2. When last number of the range is greater than the first.
    while start_n >= end_n:
        print(start_n)       ### prints range in descending order
        start_n -= 1
else:
    print("Error! This range does not exist.")