# Basic Implementation of Stack using LinkedList in python
# Includes a Node and a Stack class
# Stack operations include push, pop, is_empty, is_full


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):

    def __init__(self, capacity):
        
        # max number of elements to be entered in the stack
        self.capacity = capacity

        # index of topmost element in the stack
        self.top = -1

        # defines the topmost element of the stack
        self.root = None

    def is_empty(self):
        """
        determines if stack is empty or not
        """
        return self.top == -1

    def is_full(self):
        """
        determines if stack is full or not
        """
        return self.top == self.capacity - 1

    
    def traversal(self):
        """
        prints all elements in the stack
        """
        if self.is_empty():
            print "There are no elements in the stack"
        else:
            temp_node = self.root
            while(temp_node):
                print temp_node.data
                temp_node = temp_node.next

    def push(self, data):
        """
        push element to the stack when stack is not full
        """
        if self.is_full():
            print "stack is full. element cannot be added further"
        else:
            new_node = Node(data)
            new_node.next = self.root
            self.root = new_node
            self.top += 1
            print "stack is pushed with the element %d" % data

    def pop(self):
        """
        remove element from the stack when stack is not empty
        """
        if self.is_empty():
            print "element cannot be popped as stack is empty"
        else:
            temp = self.root
            self.root = self.root.next
            self.top -= 1
            print "element that is deleted from the stack is %d" % temp.data
            del temp


if __name__ == '__main__':

    # initialize stack
    stack = Stack(5)

    # pop when no elements
    stack.pop()

    # add five elements in the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    # print all elements in the stack
    stack.traversal()

    # delete all elements in the stack
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    # print all elements in the stack
    stack.traversal()
