# Basic Implementation of Stack using LinkedList in python
# Includes a Node and a Stack class
# Stack operations include push, pop, is_empty, is_full


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Parenthesis(object):

    def __init__(self, expression):

        # index of topmost element in the stack
        self.top = -1

        # defines the topmost element of the stack
        self.root = None

        # parenthesis input
        self.expression = expression

        # map open and close parenthesis
        self.parenthesis_map = {'{': '}', '(': ')', '[': ']'}

    def is_empty(self):
        """
        determines if stack is empty or not
        """
        return self.top == -1

    
    def traversal(self):
        """
        prints all elements in the stack
        """
        if self.is_empty():
            print "There are no elements in the stack"
        else:
            temp_node = self.root
            while(temp_node):
                temp_node = temp_node.next

    def peek(self):
        """
        returns the topmost element in the stack
        """
        return self.root


    def push(self, data):
        """
        push element to the stack when stack is not full
        """
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node
        self.top += 1
        print "pushed %s" % data

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
            print "popped %s" % temp.data
            del temp

    def validate_parenthesis(self):
        """
        check if the expression is properly closed or not
        """
        is_valid = True
        for character in self.expression:
            if character in ['(', '[', '{']:
                self.push(character)
            elif self.is_empty():
                is_valid = False
                break
            else:
                stack_top = self.peek().data
                closing_parenthesis = self.parenthesis_map[stack_top]
                if character == closing_parenthesis:
                    self.pop()
        if self.is_empty() and is_valid:
            print "The given expression is \"{}\" valid".format(self.expression)
        else:
            print "The given expression is \"{}\" invalid".format(self.expression)

if __name__ == '__main__':

    # initialize stack
    stack = Parenthesis("[(])")

    stack.validate_parenthesis()


    stack = Parenthesis("[()]{}{[()()]()}")

    stack.validate_parenthesis()


    stack = Parenthesis("[()]]")

    stack.validate_parenthesis()