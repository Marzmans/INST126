"""Documentation: run program like python, make sure to have Consolidation_functions in the same directory
 "Consolidation New.py" (encrypt/decrypt) (step) (string1) (string2)"""
import sys
import Consolidation_functions

#main section of code to combine other functions to achieve desired outcome
encrypt = ["encrypt", "decrypt"]
def main():
    try:
        mode = sys.argv[1].lower()
        if mode not in encrypt: #troubleshooting if someone does not provide the correct inputs
            raise ValueError("Input encrypt or decrypt")
        step = int(sys.argv[2])
        strings = sys.argv[3:]
        for i in strings:
            result = Consolidation_functions.caesar(i, step, encrypt=(mode == "encrypt"))
            print("{}ed: {}.".format(sys.argv[1], result))
    except (ValueError, IndexError): #learned how to handle multiple possible errors from https://rollbar.com/blog/python-catching-multiple-exceptions/
        print(r'Run the program like this: python "Consolidation New.py" (encrypt/decrypt) (step) (string1) (string2) ...')

main()
