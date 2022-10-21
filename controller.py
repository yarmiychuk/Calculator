import logger
import model
import view

def ask_calculate_way(enter):
    while True:
        try:
            a = int(input(enter))
            if a == 1:
                return True
            elif a == 2:
                return False
            else:
                view.error_choise()
        except:
            view.error_choise()

def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()

def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            view.error_value()

def operation():
    match (model.ops):
        case '+':
            model.total = model.first + model.second
        case '-':
            model.total = model.first - model.second
        case '*':
            model.total = model.first * model.second
        case '/':
            while model.second == 0:
                print('На ноль делить нельзя!')
                model.init_second()
            model.total = int(model.first / model.second)

        case _:
            view.error_value()
    logger.logger(f'{model.first} {model.ops} {model.second} = {model.total}')

def normalization(exp: str):
    exp = exp.replace(' ', '').strip()
    exp = exp.replace('+', ' + ').replace('-', ' - ')\
        .replace('*', ' * ').replace('/', ' / ').split()
    if exp[0] in ['+', '-', '*', '/']:
        exp.insert(0, '0')
    return exp

def get_string(exp: list):
    text = ''
    for item in exp:
        text += str(item) + ' '
    return text + '= '

def make_primary(exp: list):
    try:
        for i in range(len(exp)):
            if exp[i] == '/':
                exp[i - 1] = float(exp[i - 1]) / float(exp[i + 1])
                exp.pop(i)
                exp.pop(i)
                break
            elif exp[i] == '*':
                exp[i - 1] = float(exp[i - 1]) * float(exp[i + 1])
                exp.pop(i)
                exp.pop(i)
                break
    except:
        exp = ['0', '0']
    return exp

def make_secondary(exp: list):
    try:
        for i in range(len(exp)):
            if exp[i] == '+':
                exp[i - 1] = float(exp[i - 1]) + float(exp[i + 1])
                exp.pop(i)
                exp.pop(i)
                break
            elif exp[i] == '-':
                exp[i - 1] = float(exp[i - 1]) - float(exp[i + 1])
                exp.pop(i)
                exp.pop(i)
                break
    except:
        exp = ['0', '0']
    return exp

def input_expression(enter):
    while True:
        exp = normalization(input(enter))
        string_exp = get_string(exp)
        while len(exp) > 1:
            if '*' in exp or '/' in exp:
                exp = make_primary(exp)
            elif '+' in exp or '-' in exp:
                exp = make_secondary(exp)
            else:
                exp[0] = None
                break
        if exp[0] != None:
            r = exp[0]
            r = int(r) if float(r) == int(r) else float(r)
            logger.logger(f'{string_exp}{r}')
            return r
        else:
            view.error_value()