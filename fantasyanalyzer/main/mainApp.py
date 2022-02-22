#file or combining together all the functionality
from fantasyanalyzer.pulldata import queries



class commandLine:

    def __init__(self):
        self.runState = True
        

    def processCommand(self, command):
        Commands = ["exit", "query"]
        if command == "exit":
            print("Exiting the program")
            self.runState = False
        elif command == "query":
            self.processQuery()
        result = self.runState
        return result

    def processQuery(self):
        queryCommands = ["pos", "team"]
        inQuery = True
        newQuery = queries.query()
        print("Commands = pos, team")
        whichquery = input("Please enter what you would like to query?")
        while inQuery:
            if whichquery == "pos":
                print("Positions: RB, TE, QB, WR")
                whichpos = input("Please enter the position you would like to query: ")
                pos = whichpos.upper()
                newQuery.queryPos(pos)
                newQuery.printByFantPt()
                inQuery = False
            else:
                print("Nothing else ready yet")



    def run(self):
        print("Commands = query, exit")
        while self.runState:
            inputstr = input("Please Enter A Command: \n")
            self.processCommand(inputstr.lower())
