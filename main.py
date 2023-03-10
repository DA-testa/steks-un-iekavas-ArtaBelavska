# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # enumerate atdod gan kārtas numuru, gan simbolu
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            # Process opening bracket, write your code here
        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[-1].position
    else:
        return "Success"

def main():
    print("F vai I")
    answer = input()

    if "F" in answer:
        nosaukums = input ("Faila nosaukums:")
        file =  open(nosaukums, "r")
        d = file.read()
        lookfor = find_mismatch(d)
        if lookfor =="Success":
          print("Success")
        else:
            print(lookfor)
    elif "I" in answer:
        d= input()
        lookfor = find_mismatch(d)
        print(lookfor)
    else:
        print("Nepareizs burts!")
    

if __name__ == "__main__":
    main()
