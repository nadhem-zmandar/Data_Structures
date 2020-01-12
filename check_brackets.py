# python3

from collections import namedtuple


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    k=0
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            k=i+1
            if len(opening_brackets_stack)==1:
                br=Bracket(next,i+1)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)==0:
                return i+1
            else:

                top=opening_brackets_stack.pop()
                k=i+1

                if not are_matching(top,next):
                    return i+1
            pass

    if len(opening_brackets_stack)==0:
        return -1
    elif len(opening_brackets_stack)==1:
        return br.position
    else:
        return k



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch==-1:
        print("Success")
    else:
        print(mismatch)



if __name__ == "__main__":
    main()
