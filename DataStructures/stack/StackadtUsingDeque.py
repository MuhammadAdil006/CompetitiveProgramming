from collections import deque
# deque is double ended queue
# this adt is faster then list adt as list elements are not stored consectively sometimes
# however we can use deque as lifo and fifo stack as well as queue
stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')

print(stack.pop())
print(stack.pop())
print(stack.pop())

# functions of deque

stack.appendleft("d")  # append at start
stack.popleft()  # removing from start

# index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
# insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
# remove():- This function removes the first occurrence of the value mentioned in arguments.
# count():- This function counts the number of occurrences of value mentioned in arguments.


# extend(iterable):- This function is used to add multiple values at the right end of the deque. The argument passed is iterable.
# extendleft(iterable):- This function is used to add multiple values at the left end of the deque. The argument passed is iterable. Order is reversed as a result of left appends.
# reverse():- This function is used to reverse the order of deque elements.
# rotate():- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to the left. Else rotation is to right.
# using rotate() to rotate the deque
# rotates by 3 to left
print(stack)
# stack.rotate(-3)
stack.extendleft([7, 8, 9])
print(stack)
