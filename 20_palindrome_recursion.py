def string_reverse(mystr):
    if len(mystr) == 1:
        return mystr[0]
    else:
        return mystr[-1] + string_reverse(mystr[:-1])
    
def palindrome_check(mystr):
    if string_reverse(mystr) == mystr:
        return True
    else:
        return False
