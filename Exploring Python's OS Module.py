#Task 1: Directory Inspector
import os

#define a new function for listing directory contents
def list_directory_contents(path):
    #check to see if the directory path is exists and is accurate
    try:
        #list and print all files and subdirectories in the given path
        print(os.listdir(path))
    #if an error is thrown looking for the path, prompt the user to ensure the input is correct
    except OSError:
        print("Please check to make sure this path exists and is accessible.")
    
#prompt the user for a file path and store it as a variable
user_path = input("Please enter a file that you would like to display the contents of: ")

#call the function to list directory contents
list_directory_contents(user_path)