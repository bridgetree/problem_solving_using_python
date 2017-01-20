def string_reverse(mystr):
    if len(mystr) == 1:
        return mystr[0]
    else:
        return mystr[-1] + recursion(mystr[:-1])
    
def palindrome_check(mystr):
    if recursion(mystr) == mystr:
        return True
    else:
        return False
