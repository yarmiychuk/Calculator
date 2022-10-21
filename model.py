import controller
import view

first = 0
second = 0
ops = ''
total = 0
result = 0
exp = 0

def is_immediately():
    return controller.ask_calculate_way('Выберите способ вычисления:\
        \n1 - Вычислить выражение целиком\
        \n2 - Вычислить пошагово\n')

def init_first():
    global first
    first = controller.input_integer('Введите число: ')

def init_second():
    global second
    second = controller.input_integer('Введите число: ')

def init_ops():
    global ops
    ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total()
        return True

def init_expression():
    global total
    total = controller.input_expression('Введите выражение: ')
    if total != None:
        view.print_total()
        return True
