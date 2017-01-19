# This needs the installation of pythonds package
# http://www.pythonworks.org/pythonds

from test import testEqual
from pythonds.basic.stack import Stack

def revstring(mystr):
    myStack = Stack()
    for ch in mystr:
        myStack.push(ch)
    revstr = ''
    while not myStack.isEmpty():
        revstr = revstr + myStack.pop()
        
    return revstr
