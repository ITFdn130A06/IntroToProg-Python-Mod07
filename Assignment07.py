# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: My script utilizes pickling and exception handling
#              I've also structured this program, so I can practice writing
#              code in a similar fashion to assignment.
# ChangeLog (Who,When,What):
# VTirumalai,11.27.2022,Created started script
# Vikram Tirumalai,11/27/2022,pickling and error handling
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
import pickle
lstTable = []
dicRow = {}
strFile = 'SoccerData.dat'
choiceStr = ''

# Processing and Error Handling --------------------------------------------------------------- #
class Processing:
    @staticmethod
    def read_existing_data(strFile, list_of_rows):
        '''Reads existing data from the SoccerData file into a list.

        :param strFile (string): name of file
        :param lstTable (list): list of dictionaries of soccer data
        :return fileData (list): return object'''

        #step through list, extract each element of list and append it
        list_of_rows.clear()
        file = open('SoccerData.dat', 'rb')
        fileData = pickle.load(file)
        for item in fileData:
            list_of_rows.append(item)
        file.close()
        print(list_of_rows)

    @staticmethod
    def write_to_file(strFile, list_of_rows):
        '''Writes desired data to file
        :param strFile (string): name of file
        :param lstTable (list): list of dictionaries of soccer data
        '''
        file = open('SoccerData.dat', 'wb')
        pickle.dump(list_of_rows, file)
    @staticmethod
    def show_current_data(strFile, list_of_rows):
        '''Shows current data
         :param strFile (string): name of file
        :param lstTable (list): list of dictionaries of soccer data
        '''
        print("This is the current data:")
        print(lstTable)

    @staticmethod
    def remove_data(removalInput, list_of_rows):
        '''Gives the user the option to remove a row from their list
        :param list_of_rows (list) list of soccer players and estimated goals
        '''
        try:
            for row in list_of_rows:
                if removalInput == row["Player"]:
                    list_of_rows.remove(row)
                    print("Here's the updated table: ")
                    print(list_of_rows)
                    return list_of_rows
        except Exception as e:
            print("Non-specific error occurred.")
            print(e, type(e), e.__doc__, sep=', ')



# Presentation (Input/Output)  -------------------------------------------- #

class io:
    @staticmethod
    def output_menu_tasks():
        'Gives the typical output menu that we have been using in assignments.'
        print('''Menu of choices:
        1) View current data
        2) Add to file
        3) Remove a listing
        4) Save and Exit
        ''')

    @staticmethod
    def input_menu_choice():
        'Asks the user for input choice.'
        try:
            choice = input("Enter the number that corresponds to the action you want to perform: ")
            print()
            return choice
            if choice.isalpha():
                raise Exception ("Enter a number, not letter.")
        except Exception as e:
            print("Non-specific error occurred.")
            print(e, type(e), e.__doc__, sep=', ')


    @staticmethod
    def soccer_data_input(list_of_rows):
        'Gets soccer data input'
        try:
            print("Who do you think will be the top scorer(s) in the World Cup?")
            playerInput = input("Name a player: ")
            if playerInput.isnumeric():
                raise Exception ("A player's name should only have letters in it.")
            goalInput = float(input("Tell me how many goals you think will be scored: "))
            print()
            if goalInput < 0:
                raise Exception ("Negative goals cannot be scored.")
            dicRow = {"Player":playerInput.strip(), "Goals":goalInput}
            list_of_rows.append(dicRow)
            return list_of_rows
        except Exception as e:
            print("Non-specific error occurred.")
            print(e, type(e), e.__doc__, sep=', ')

    @staticmethod
    def removal():
        'Asks user for the name of the player they want to remove.'
        removalInput = input("Enter the name of the player whose row you want deleted: ").strip()
        print()
        return removalInput
        pass

# Main Body of Script  ------------------------------------------------------ #
# Step 1 - When the program starts, Load data from the Soccer Data file.
#print(Processing.read_existing_data(strFile = strFile, list_of_rows = lstTable))

# Step 2 - Show the user the menu, and give them the choice to input their selection

Processing.read_existing_data(strFile=strFile, list_of_rows=lstTable)

while (True):
    io.output_menu_tasks()
    choiceStr = io.input_menu_choice()
    if choiceStr.strip() == '1':
        Processing.show_current_data(strFile=strFile, list_of_rows=lstTable)
        continue
    elif choiceStr.strip()== '2':
        io.soccer_data_input(list_of_rows=lstTable)
        Processing.show_current_data(strFile=strFile, list_of_rows=lstTable)
        continue
    elif choiceStr.strip() == '3':
        removalInput = io.removal()
        lstTable = Processing.remove_data(list_of_rows=lstTable, removalInput=removalInput)
        continue
    elif choiceStr.strip() == '4':
        Processing.write_to_file(strFile=strFile, list_of_rows=lstTable)
        print("Check back on 12/18 [World Cup end date] to see how your predictions held up!")
        print("Right now you think it will pan out this way: ")
        try:
            for row in lstTable:
                print(row["Player"], 'with', row["Goals"], 'goals')
            if len(lstTable) == 0:
                raise Exception ('Your table has no values, please enter some. \n')
            break
        except Exception as e:
            print("There was a non-specific error")
            print("Built-in Python error info: ")
            print(e, e.__doc__, type(e), sep=', ')
