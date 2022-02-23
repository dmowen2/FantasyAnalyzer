# file for combining all the functionality
from fantasyanalyzer.pulldata import queries



class commandLine:

    def __init__(self):
        self.runState = True
        

    def processCommand(self, command):
        Commands = ["exit", "query"]
        if command == "exit":
            print("Exiting the program")
            self.runState = False
        elif command == "help":
            print("Available Commands: help, exit, query")
        elif command == "query":
            self.processQuery()
        else:
            print("Invalid Command")
        result = self.runState
        return result

    def processQuery(self):
        queryCommands = ["pos", "name"]
        inQuery = True
        newQuery = queries.query()
        print("Commands = pos, name, team")
        whichquery = input("Please enter what you would like to query?")
        while inQuery:

            # Might need some error handling error and encapsulate it in a try catch statement
            if whichquery == "pos":
                print("Positions: RB, TE, QB, WR")
                whichpos = input("Please enter the position you would like to query: ")
                pos = whichpos.upper()
                newQuery.queryPos(pos)
                newQuery.printByFantPt()
                inQuery = False
            elif whichquery == "name":
                name = input("Please enter the name of the player you would like to query: ")
                newQuery.queryName(name)
                newQuery.printData()
                inQuery = False
            elif whichquery == "team":
                teamname = input("Enter Team Abbreviation (IND, LAR, HOU, etc.): ")
                newQuery.queryTeam(teamname.upper())
                newQuery.printData()
                inQuery = False

            else:
                print("Invalid command")
        saveassheet = input("Would you like to save the queried data in a separate sheet? (Y/N): ")
        if saveassheet.lower() == 'y':
            nameofsheet = input("What would you like to name the sheet?: ")
            newQuery.saveData(nameofsheet)



    def run(self):
        print("Commands = query, exit")
        while self.runState:
            inputstr = input("Please Enter A Command: \n")
            self.processCommand(inputstr.lower())
