# Created by ArztKlein (https://github.com/ArztKlein)
# A Python implementation of the Shunting-yard Algorithm.

def convert(expression):
    """ Operators and operands must be split by spaces. """
    
    expression = expression.split(" ")

    operators_precedence = {"^": 4, "/": 3, "*": 3, "+": 2, "-": 2}
    operators_associativity = {"^": "right", "/": "left", "*": "left", "+": "left", "-": "left"}

    output_queue = []
    operator_stack = []

    for x in expression:
        if x not in operators_precedence and x not in ["(", ")"]: # Is number
            output_queue.append(x)
            continue
        elif x in operators_precedence:
            o1 = x
            o1_precedence = operators_precedence[o1]
            o1_associativity = operators_associativity[o1]
            for i,o2 in reversed(list(enumerate(operator_stack))):
                if o2 == "(":
                    break
                o2_precedence = operators_precedence[o2]
                if o2_precedence > o1_precedence or (o1_precedence == o2_precedence and o1_associativity == "left"):
                    output_queue.append(o2)
                    operator_stack.pop(i)
            operator_stack.append(o1)
        elif x == "(":
            operator_stack.append(x)
        elif x == ")":
            while True:
                o2 = operator_stack[-1]
                if o2 == "(":
                    operator_stack.pop(-1)
                    break

                output_queue.append(o2)
                operator_stack.pop(-1)

    for x in list(reversed(operator_stack.copy())):
        # If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses.
        output_queue.append(x)

    return " ".join(output_queue)
