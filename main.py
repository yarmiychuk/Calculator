import controller
import model
import view

def calculate_all():
    while True:
        if model.init_expression():
            break

def step_by_step():
    model.init_first()
    while True:
        if model.init_ops():
            break
        model.init_second()
        controller.operation()
        view.print_total()
        model.first = model.total

if (model.is_immediately()):
    calculate_all()
else:
    step_by_step()


