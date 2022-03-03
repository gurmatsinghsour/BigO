class FCFS:
    def __init__(self, burstTime):
        self.burstTime = burstTime

    def waitingTime(self):
        waitingTimeArray = [0]        

        j = 0 

        for i in range(0, len(self.burstTime)):
            j += 1 
            waitingTimeArray.append(self.burstTime[i] + waitingTimeArray[j-1]) 
        
        waitingTimeArray.pop()

        return waitingTimeArray

    def turnAroundTime(self):
        turnAroundTime = [0]     

        j = 0 

        for i in range(0, len(self.burstTime)):
            j += 1 
            turnAroundTime.append(self.burstTime[i] + turnAroundTime[j-1]) 

        turnAroundTime.pop(0)

        return turnAroundTime

    def averageValue(array):
        averageTime = sum(array)/len(array)
        return averageTime



def run():
    while True:
        try:
            numberOfProcess = int(input("Enter the number of process [Maximum 20]: "))
            if numberOfProcess<=20:               
               burstTime = []
               for i in range(numberOfProcess):
                   burstTime.append(int(input("P "+ str(i+1) + " = ")))
                
               print('''
Given values,
Process            Burst Time''')
               for i in range(len(burstTime)):
                   print(f'''
P{i+1}\t\t\t{burstTime[i]}''')


               classInstantiation = FCFS(burstTime)
               wT = classInstantiation.waitingTime()      


               print('''
Process            Waiting Time''') 
               for i in range(len(wT)):
                   print(f'''
P{i+1}\t\t\t{wT[i]}''')


               tat = classInstantiation.turnAroundTime()   

               print(f'''
Process            Turn around time''')
               for i in range(len(tat)):
                    print(f'''
p{i+1}\t\t\t{tat[i]}''')             

               awt = int(FCFS.averageValue(wT))
               atat = int(FCFS.averageValue(tat))

               print(f"Average waiting time: {awt}. Average turn around time: {atat}")
               break
            
            else:
                print("Hey! Maximum value you can enter is 20. ")
                continue
        except ValueError as err:
            print(err)
            continue
        except ZeroDivisionError as err:
            print("Hey, don't enter \"0\" ", err)
            continue



if __name__ == "__main__":
    run()
         


               
            #    classInstantiation = FCFS(burstTime)
            #    wT = classInstantiation.waitingTime()
            #    tat = classInstantiation.turnAroundTime()


            #    print(wT)
            #    print(tat)
            #    print(awt)
            #    print(atat)
