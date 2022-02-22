#file or combining together all the functionality

class commandLine:

    def __init__(self):
        self.runState = True
        

    def processCommand(self, command):
        Commands = ["exit", "query"]
        if command == "exit":
            print("Exiting the program")
            self.runState = False
        result = self.runState
        return result

    def run(self):
        print("Commands = query, exit")
        while self.runState:
            inputstr = input("Please Enter A Command: \n")
            self.processCommand(inputstr.lower())
