def linearSearch(array, v):
    for i in range(0, len(array)):
        while i>=0 and array[i] == v:
            print("found at", i, "th index")
            exit()
        
        print("NIL")

    
print(linearSearch(       
    [int(i) for i in input("Enter the values of array : ").split()], int(input("Enter the value that you want to find in the array : "))
))