class Worstfit:
    def __init__(self, processSize, blockSize):
        self.processSize = processSize
        self.blockSize = blockSize
    
    def block(self):
        try: 
            finalBlock = {}
            for i in self.blockSize:
                finalBlock[i] = []

            return finalBlock
        
        except ValueError as error:
            print(error)

    def allocation(self,block):
        try:
            for i in range(len(self.processSize)):
                currentProcess = self.processSize[i]
                currentMax = max(block.keys())

                if currentProcess <= max(block.keys()):
                    block[currentMax].append(currentProcess)
                    block[currentMax-currentProcess] = block.pop(currentMax)
                else:
                    continue



            
            return block

        except ValueError as error:
            print(error)
        
        except KeyError as error:
            print(error)

        


name = Worstfit([212, 417, 112, 426],[100, 500, 200, 300, 600])
block = name.block()
print(name.allocation(block))