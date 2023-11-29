"""Documentation: run program like python, make sure to have Consolidation_functions in the same directory
 Consolidation New.py" (encrypt/decrypt) (step) (string1) (string2)"""
import sys
import os
import Consolidation_functions


#main section of code to combine other functions to achieve desired outcome

def main():
    #troubleshooting if someone does not provide the correct inputs
    try:
        type = []
        type.append(sys.argv[1].lower())
        if type[0] not in ["encrypt", "decrypt"]: #learned not in from https://www.askpython.com/python/examples/in-and-not-in-operators-in-python
            raise ValueError("Input encrypt or decrypt")

        final_type = type.pop(0)

        step = int(sys.argv[2])

        strings = sys.argv[3:]
        both = {}

        for input in strings:
            result = Consolidation_functions.caesar(input, step, encrypt=(final_type == "encrypt"))
            #storing original and changed strings
            both[input] = { #Learned how to index/search a value in dictionary from Google GenAI when you search topics
                #"Original String: ": input,
                "{}ed String: ".format(sys.argv[1].title()): result 
            }
            #store data in txt file
            file_path = str(os.getcwd) + "\\" + "stored_data.txt"
        
            print((both))

        if os.path.exists(file_path):
                with open("stored_data.txt", "a") as data:
                    data.write(both)
        else:
            with open("stored_data.txt","w") as data:
                data.write(str(both))

    except (ValueError, IndexError): #learned how to handle multiple possible errors from https://rollbar.com/blog/python-catching-multiple-exceptions/
        print(r'Run the program like this: python "Consolidation New.py" (encrypt/decrypt) (step) (string1) (string2) ...')

main()
