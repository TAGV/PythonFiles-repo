# Using dictionary as switch cases

#1st Method
def dict_calc(operator=None,var_x=0,var_y=0):
    mydict = {
        'add':var_x+var_y,
        'sub':var_x-var_y,
        'mul':var_x*var_y,
        'div':float(var_x/var_y),
        'mod':float(var_x%var_y)
    }
    #print(mydict)
    return (mydict.get(operator,0))

#2nd Method
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
        'mod': lambda: x%y
    }.get(operator, lambda: None)()

print("=================1st Method===============")
add = dict_calc('add',15,10)
print(add)

sub = dict_calc('sub',15,10)
print(sub)

mul = dict_calc('mul',15,10)
print(mul)

div = dict_calc('div',15,10)
print(div)

mod = dict_calc('mod',15,10)
print(mod)

print("=================2nd Method===============")

add = dispatch_dict('add',15,10)
print(add)

sub = dispatch_dict('sub',15,10)
print(sub)

mul = dispatch_dict('mul',15,10)
print(mul)

div = dispatch_dict('div',15,10)
print(div)

mod = dispatch_dict('mod',15,10)
print(mod)