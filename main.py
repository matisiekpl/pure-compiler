def scan(expression):
    print(f'Scanning expression: {expression}')
    bracket_counter = 0
    expression = expression.replace(' ', '')
    if expression[0] in '+*/':
        raise Exception(f'[0] Expression cannot start with: {expression[0]}')
    if expression[0] == ')':
        raise Exception('[0] Closing bracket at start')
    if expression[0] == '(':
        bracket_counter += 1

    for i in range(1, len(expression)):
        if expression[i] == ')':
            if bracket_counter < 1:
                raise Exception(f'[{i}] Bad closing bracket')
            if expression[i - 1] == '(':
                raise Exception(f'[{i - 1}] Empty brackets')
            if expression[i - 1] in '+-*/':
                raise Exception(f'[{i - 1}] Sign before closing bracket')
            bracket_counter -= 1
            continue

        if expression[i] == '(':
            bracket_counter += 1
            if expression[i - 1].isdigit():
                raise Exception(f'[{i - 1}] Bracket after digit')
            if expression[i - 1] == ')':
                raise Exception(f'[{i - 1}] Empty brackets')
            continue

        if expression[i] in '+*/':
            if expression[i - 1] == '(':
                raise Exception(f'[{i - 1}] Invalid first character in bracket')

        if expression[i] in '+-*/':
            if expression[i - 1] in '+-*/':
                raise Exception(f'[{i - 1}] Sign after sign')
            continue

        if expression[i] == '0' and not expression[i - 1].isdigit():
            if i != len(expression) - 1:
                if expression[i + 1].isdigit():
                    raise Exception(f'[{i - 1}] Number starts with 0')

        if expression[i].isdigit():
            if expression[i - 1] == ')':
                raise Exception(f'[{i - 1}] Number with closing bracket inside')
            continue

        raise Exception(f'[{i}] Invalid symbol: {expression[i]}')

    if expression[-1] in '+-*/':
        raise Exception(f'[{len(expression) - 1}] Expression cannot end with: {expression[i]}')

    if bracket_counter != 0:
        raise Exception('Brackets inconsistency')

    num = False
    numbers = ''
    beforeNegative = True

    for c in expression:
        if num and not c.isdigit():
            print(f'Integer: {numbers}')
            num = False
            numbers = ''

        if c == '-':
            if beforeNegative:
                numbers += '-'
                beforeNegative = False
                continue
            else:
                beforeNegative = False
                print('Subtraction')
            continue
        beforeNegative = False

        if c == '+':
            print('Addition')
            continue
        if c == '*':
            print('Multiplication')
            continue
        if c == '/':
            print('Division')
            continue
        if c == '(':
            print('OpeningBracket')
            continue
        if c == ')':
            print('ClosingBracket')
            continue
        if c.isdigit():
            numbers += c
            num = True
            continue

        raise Exception(f'Invalid symbol: {c}')

    if numbers != '':
        print(f'Integers: {numbers}')
