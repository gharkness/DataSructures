# Stack

In a stack, the element deleted from the set is the one most recently inserted: the stack implements a last-in, first-out, or __LIFO__, policy. 

The INSERT operation on a stack is often called __PUSH__, and the DELETE opera- tion, which does not take an element argument, is often called __POP__.

These names are allusions to physical stacks, such as the spring-loaded stacks of plates used in cafeterias. The order in which plates are popped from the stack is the reverse of the order in which they were pushed onto the stack, since only the top plate is accessible.

![](Resources/10.1.png)

As [Figure 10.1](Resources/10.1.png) shows, we can implement a stack of at most n elements with an array S[1 ... S._top_]. The array has an attribute _S.top_ that indexes the most recently inserted element. The stack consists of elements S[1 ... S._top_], where _S[1]_  is the element at the bottom of the stack and S[S._top_] is the element at the top.

When S._top_ = 0, the stack contains no elements and is __empty__. We can test to see whether the stack is empty by query operation _STACK-EMPTY_. If we attempt to pop an empty stack, we say the stack __underflows__, which is normally an error. If S._top_ exceeds n, the stack __overflows__.

### Basic Stack Abstract Data Type Interface

- `Stack()`
    + Creates a new stack that is empty. 
    + It needs no parameters and returns an empty stack.
- `push(item)`
    + Adds a new item to the top of the stack. 
    + It needs the item and returns nothing.
- `pop()`
    + Removes the top item from the stack. 
    + It needs no parameters and returns the item. 
    + The stack is modified.
- `peek()`
    + Returns the top item from the stack but does not remove it. 
    + It needs no parameters. 
    + The stack is not modified.
- `isEmpty()`
    + Tests to see whether the stack is empty. 
    + It needs no parameters and returns a boolean value.
- `size()`
    + Returns the number of items on the stack. 
    + It needs no parameters and returns an integer.

### Basic Pseudocode Implementation

```
STACK-EMPTY(S)
    if S.top == 0
        return True
    else return False

PUSH(S,x)
    S.top = S.top + 1
    S[S.top] = x

POP(S)
    if STACK-EMPTY(S)
        error "Underflow"
    else S.top = S.top - 1
        return S[S.top + 1]
```

## Resources

- [What is a Stack?](http://interactivepython.org/runestone/static/pythonds/BasicDS/WhatisaStack.html)
- [The Stack Abstract Data Type](http://interactivepython.org/runestone/static/pythonds/BasicDS/TheStackAbstractDataType.html)
- [Stack Basics in Java](http://cs.lmu.edu/~ray/notes/stacks/)
- [Implementing a Stack in Java using Arrays and Linked Lists](http://eddmann.com/posts/implementing-a-stack-in-java-using-arrays-and-linked-lists/)
- [Princeton CS: Stacks and Queues](http://introcs.cs.princeton.edu/java/43stack/)
- [Java.util Stack Class Documentation](https://docs.oracle.com/javase/7/docs/api/java/util/Stack.html)
- [Java.util.Stack.java](http://www.docjar.com/html/api/java/util/Stack.java.html)

## Code 

- [Python](stack.py)

#### References

- [Introduction to Algorithms 3rd Edition](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844/ref=sr_1_1?ie=UTF8&qid=1471285317&sr=8-1&keywords=introduction+to+algorithms)
