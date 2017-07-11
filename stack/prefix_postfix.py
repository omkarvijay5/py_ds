# Implementation to evaluate postfix and prefix expressions using stack
# infix expression 2*3+5*4-9

# postfix equivalent 23*54*+9-
# result is (2*3)+(5*4)-9 = 17

# prefix equivalent -+*23*54
# result is (*23)+ (*54) - 9 = 17


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class EvalPrePostFix(object):
    """
    Stack implementation using linked list for evaluation of the prefix and postfix expressions
    """
    
    def __init__(self, expression):
        self.root = None
        self.top = -1
        self.expression = expression
        self.operators = '+-/*^'
        self.postfix_expression = ''

    def traversal(self):
        """
        print all elements in the stack
        """
        temp_node = self.root
        while(temp_node):
            print temp_node.data
            temp_node = temp_node.next

    def is_empty(self):
        return self.top == -1

    def is_operator(self, character):
        return character in self.operators

    def evaluate_postfix(self):
        """
        postfix expression evaluation
            2*3+5*4-9
            ((2*3) + (5*4)) - 9
            (23*) + (54*) - 9
            (23*)(54*)+ - 9
            23*54*+9-
        """
        for character in self.expression:
            if self.is_operator(character):
                operand1 = self.pop()
                operand2 = self.pop()
                value = eval(str(operand2) + character + str(operand1))
                self.push(value)
            else:
                self.push(character)
        final_result = self.pop()
        print "The postfix result is %s" % final_result

    def evaluate_prefix(self):
        """
        prefix expression evaluation
            2*3+5*4-9
            (2*3)+(5*4)-9
            (*23)+(*54) - 9
            +*23*54-9
            -+*23*549
        """
        i = 0
        expression_length = len(self.expression)
        while(i < expression_length):
            index = expression_length - i -1
            character = self.expression[index]
            if self.is_operator(character):
                operand1 = self.pop()
                operand2 = self.pop()
                value = eval(str(operand1) + character + str(operand2))
                self.push(value)
            else:
                self.push(character)
            i += 1
        final_result = self.pop()
        print "The prefix result is %s" % final_result

        
    def push(self, data):
        """
        push element to the stack when stack is not full
        """
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node
        self.top += 1
        print "stack pushed with the element %d" % int(data)

    def pop(self):
        """
        remove element from the stack when the stack is not empty
        """
        if self.is_empty():
            print "stack is empty and cannot be popped"
        else:
            temp_node = self.root
            self.root = self.root.next
            print "data is deleted %d" % int(temp_node.data)
            self.top -= 1
            return temp_node.data




if __name__ == '__main__':

    # initialize postfix
    postfix_stack = EvalPrePostFix("23*54*+9-")
    
    # evaluate postfix
    postfix_stack.evaluate_postfix()

    # initialize prefix
    prefix_stack = EvalPrePostFix("-+*23*549")
    prefix_stack.evaluate_prefix()
