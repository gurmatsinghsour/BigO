class SJF:
    def __init__(self, burstTimeArray):
        self.burstTimeArray = burstTimeArray

    def sorted(self):

        def custom_key(array):
            return array[1]

        self.burstTimeArray.sort(key=custom_key)

        return self.burstTimeArray

        # for i in range(1, len(self.burstTimeArray)):
        #     currentNestedList = self.burstTimeArray[i]
        #     j = i - 1 
        #     while ((j>= 0) and (self.burstTimeArray[j][1] > self.burstTimeArray[i][1])):
        #         self.burstTimeArray[j+1] = self.burstTimeArray[j]
        #         j -= 1
        #     self.burstTimeArray[j+1] = currentNestedList

        # return self.burstTimeArray

    def waitingTime(self, array):
        waitingTimeArray = [0]
        j = 0
        for i in range(len(array)):
            waitingTimeArray.append(waitingTimeArray[i] + array[j][1])
            j += 1
        waitingTimeArray.pop()
        
        return waitingTimeArray


    def turnAroundTime(self, array):
        turnAroundTimeArray = [0]
        j = 0
        for i in range(len(array)):
            turnAroundTimeArray.append(turnAroundTimeArray[i] + array[j][1])
            j += 1
            
        turnAroundTimeArray.pop(0)
        
        return turnAroundTimeArray
    
    def averageTime(self, array):
        return sum(array)/len(array)
        
def arraySplitting(array):
    for i in range(0, len(array), 2):
        yield array[i:i + 2]

def run():
    while True:
        try:
            numberOfProcess = int(input("Enter the number of process [Maximum 20]: "))
            if numberOfProcess <= 20:

                

                sjfArray = []

                for i in range (numberOfProcess):
                    i = []
                    sjfArray.append(i)

                for i in range(numberOfProcess):

                    n = "P"+str(i+1)
                    sjfArray[i].append(n)
                    sjfArray[i].append(int(input("P "+ str(i+1) + " = ")))    
                
                # print(sjfSortedArray) 
                # print(sjfSortedArrayWaitingTime)                
                # print(sjfSortedArrayTurnAroundtime)

                # print(averageTurnAroundTime)
                # print(averageWaitingTime)

                print(f''''

Given Values, 

Process            Burst Time''')                
                for i in range(len(sjfArray)):
                    print(f'''
{sjfArray[i][0]}\t\t\t{sjfArray[i][1]}''')


                sjf = SJF(sjfArray)
                sjfSortedArray = sjf.sorted() 
                print(sjfSortedArray)         
                sjfSortedArrayWaitingTime = sjf.waitingTime(sjfSortedArray)
                sjfSortedArrayTurnAroundtime = sjf.turnAroundTime(sjfSortedArray)         
                             
                print(f'''
Process            Waiting Time''')

                for i in range(len(sjfSortedArray)):
                    print(f'''
{sjfSortedArray[i][0]}\t\t\t{sjfSortedArrayWaitingTime[i]}''')

                print(f'''
Process            Turn Around Time''')

                for i in range(len(sjfSortedArray)):
                    print(f'''
{sjfSortedArray[i][0]}\t\t\t{sjfSortedArrayTurnAroundtime[i]}''')

                averageTurnAroundTime = sjf.averageTime(sjfSortedArrayTurnAroundtime)
                averageWaitingTime = sjf.averageTime(sjfSortedArrayWaitingTime)

                print(f'Average time for waiting time: {averageWaitingTime} and Average waiting time for turn around time: {averageTurnAroundTime}')

                break


             

            else:
                continue

            
        
        except ValueError as error:
            print(error)
        
        except ZeroDivisionError as error:
            print("ERROR: ", error, "\n Hey! input value more than 0")

if __name__ == "__main__":
    run()