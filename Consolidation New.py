#Documentation: run program like python 'Consolidation New.py' (encrypt/decrypt) (step) (string1) (string2)
import sys

#decrypt or encrypt the string(s)
def shift(character, step, encrypt=True):
    if character.isalpha(): #learned from https://www.w3schools.com/python/ref_string_isalpha.asp
        original = ord("A") if character.isupper() else ord("a") #Learned to set alphabet at A from a more experienced friend outside of class and learned from https://www.w3schools.com/python/ref_func_ord.asp
        change = ord(character) - original
        if encrypt:
            shifted_offset = (change + step) % 26
        else:
            shifted_offset = (change - step + 26) % 26 #I had issues making sure my code works for all letters and wrapping around the alphabet, so I talked to one of my friends outside of class and he recommended mod 26
        return chr(shifted_offset + original) #learned from https://www.programiz.com/python-programming/methods/built-in/chr
    return character

#concatenate the encrypted/decrypted characters
def caesar(input, step, encrypt=True):
    return "".join(shift(character, step, encrypt) for character in input) #learned from https://stackoverflow.com/questions/12453580/how-to-concatenate-join-items-in-a-list-to-a-single-string

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
            result = caesar(i, step, encrypt=(mode == "encrypt"))
            print("{}ed: {}.".format(sys.argv[1], result))
    except (ValueError, IndexError): #learned how to handle multiple possible errors from https://rollbar.com/blog/python-catching-multiple-exceptions/
        print("Run the program like this: python 'Consolidation New.py' (encrypt/decrypt) (step) (string1) (string2) ...")

main()
