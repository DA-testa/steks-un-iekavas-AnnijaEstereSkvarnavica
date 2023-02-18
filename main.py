# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text): #enumerate atdod gan kārtas numuru gan simbolu 
        if next in "([{":
            #Struktūrai jāpievieno vērtība 
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
             
                print("ir tukšs")
                return i + 1 
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    


if __name__ == "__main__":
    main()
