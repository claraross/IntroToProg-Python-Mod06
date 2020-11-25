# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# <Your Name>,<Date>,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            file_task, file_priority = line.split(",")
            row = {"Task": file_task.strip(), "Priority": file_priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(user_task, user_priority, list_of_rows):
        """ Add new data from user input to list
        :param user_task: (string) name of task to be added
        :param user_priority: (string) priority of task to be added
        :param list_of_rows: (list) of rows the new task should be added to

        :return: list
        """
        row = {"Task": user_task, "Priority": user_priority}
        list_of_rows.append(row)

        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(user_task, list_of_rows):
        """ Remove row with user task from input
        :param user_task: (string) name of task the user wants to remove
        :param list_of_rows: (list) that data should be removed from

        :return: list
        """
        for row in list_of_rows:
            if user_task.lower() in row["Task"].lower():
                list_of_rows.remove(row)

        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Write contents of list to file
        :param file_name: (string) name of the file the data should write to
        :param list_of_rows: (list) of data that should be written to the file

        :return: list
        """
        file = open(f"{file_name}", "w")
        for row in list_of_rows:
            file.write(f"{row['Task']},{row['Priority']}\n")
        file.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Get user input for new task and priority

        :return: string, string
        """
        user_task = input("Please input task: ")
        user_priority = input("Please input priority: ")
        return user_task, user_priority

    @staticmethod
    def input_task_to_remove():
        """ Get user input for task they want to remove

        :return: string
        """
        user_task = input("Which task would you like to remove? ")
        return user_task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()  # get user input and assign to task and priority variables
        Processor.add_data_to_list(task, priority, lstTable)  # add new task and priority to list
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()  # get user input on task to remove
        Processor.remove_data_from_list(task, lstTable)  # remove from lit

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
