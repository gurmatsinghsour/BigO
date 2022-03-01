def insertionSort(array):
    for j in range(1, len(array)):
        key = array[j]

        i = j-1

        while i>=0 and array[i]>key:
            array[i+1] = array[i]
            i = i-1
        array[i+1] = key

        
    return array

inputArray = [int(i) for i in input("Enter the values : ").split()]
print(insertionSort(inputArray))