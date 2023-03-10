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
            if not opening_brackets_stack:
                
                return i + 1
                
            if not are_matching(opening_brackets_stack[-1].char, next):
                
                return i + 1 
            opening_brackets_stack.pop()
            #if opening_brackets_stack:
                
                #return opening_brackets_stack[0].position
        #return "Success"


def main():
    text = input()
    if text[0] == "I":
        text = input()
        mismatch = find_mismatch(text)
        if mismatch:
            print(mismatch)
        else:
            print("Success")
                        
    # Printing answer, write your code here
    


if __name__ == "__main__":
    main()
