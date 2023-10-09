dict = { 
    "Bug" : " a bug is a coding error that interferes with a website's normal operation ", 
    "Code monkey" : "someone who sits and programs all day",
    "OOP" : "is a programming model that categorizes software design by data (objects) instead of logic and functions",
    "Framework" : "A framework is a program, code library or another component for developing software application",
    "Attribute" : "An attribute is a specification that provides extra information about an element"
    }

print("=" * 10, "IT dictionary v-1.0","=" * 10) 
help = """ 
s - Searching for a word in the dictionary
a - Add a new word to the dictionary
r - Delete a word from the dictionary
k - Output all keys in the dictionary
d - Output the whole dictionary
h - Menu
q - Exit
"""

choice = ""
while choice != "q":
    choice = input("(h- Info >>)")
    if choice == "s":
        word = input("Enter a word:")
        res = dict.get(word, "Sorry, no such word is regestered in the dictionary:(")
        print(res)
    elif choice == "a":
        word = input("Add a word:")
        value = input("Enter the meaning of the word:")
        dict[word] = value
        print("The word is added, thank you!")   
    elif choice == "r":
        word = input("Enter a word you want to delete:")
        del dict[word]
        print("The word", word, "is deleted")
    elif choice == "k":
        print(dict.keys())
    elif choice == "d":
        for i in dict:
            print(i, ": ", dict[i])
    elif choice == "h":   
        print(help)
    elif choice == "q":
        continue
    else:
        print("There's no such command, press h to view the menu")  
    