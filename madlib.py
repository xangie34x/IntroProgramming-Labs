# Mad Lib Program
# Author: Angeli Pinol

print("Welcome to Angie's Mad Lib Story!")
print("MadLibs Story : 'A Walk Through the Park'")
    
def promptForWords():
    global noun, verb, adjective, place
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (ending in 'ing': ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    
promptForWords()

def makeAndPrintSentence():
    
    print("It is so nice to be with your " + noun + verb + " at the " + place + " on such a " + adjective + " day! ")

makeAndPrintSentence()

def main():
    promptForWords()
    makeAndPrintSentence()

main()

    
    
