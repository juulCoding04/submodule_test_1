def return_calc(n1, n2, operation):
    if operation == 'sum':
        return n1+n2
    elif operation == 'subtract':
        return n1-n2
    elif operation == 'divide':
        return n1/n2
    elif operation == 'multiply':
        return n1*n2
    else:
        return 'invalid operation'