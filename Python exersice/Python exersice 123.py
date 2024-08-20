def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def is_operator(c):
    return c in ('+', '-', '*', '/', '^')

def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(num)
        elif expression[i] in '()+-*/^':
            tokens.append(expression[i])
            i += 1
        elif expression[i] == ' ':
            i += 1  
        else:
            raise ValueError(f"Unexpected character: {expression[i]}")
    return tokens

def infix_to_postfix(tokens):
    operators = []
    postfix = []

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif is_operator(token):
            while (operators and operators[-1] != '(' and
                   precedence(token) <= precedence(operators[-1])):
                postfix.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                postfix.append(operators.pop())
            operators.pop()  

    while operators:
        postfix.append(operators.pop())

    return postfix

def main():
    infix_expr = input("Enter an infix expression: ")
    tokens = tokenize(infix_expr)
    postfix_tokens = infix_to_postfix(tokens)
    postfix_expr = ' '.join(postfix_tokens)
    print("Postfix expression:", postfix_expr)

main()
