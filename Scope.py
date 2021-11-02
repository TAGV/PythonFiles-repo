# Scope of Variables : Local,Enclosing,Global,builtin

var_x = "Outside"

def myfunc():
    var_x = 'Inside local function'
    print(var_x)

myfunc()        #Inside local function
print(var_x)    #Outside

print("===================")

def newfunc():
    print(var_x)

newfunc()       #Outside
print(var_x)    #Outside

print("===================")

def new_fun(var_z):
    print(var_z)

new_fun(var_x)  #Outside
print(var_x)    #Outside

print("===================")

def nestfun():
    #var_x = 10
    print(var_x)    #Outside
    def func():
        print(var_x)    #Outside

    func()
    # var_x = 10      # local variable 'var_x' referenced before assignment
    print(var_x)    #Outside

nestfun()
# func()          # NameError: name 'func' is not defined
print(var_x)