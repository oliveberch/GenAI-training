# decclare a var outside and use inside the func

age = 23
def func():
    print("I am ",age," years old.")
func()

# decclare a var inside as well and use var inside the func
age = 64
def func():
    age = 87
    print("I am ",age," years old.")
func()

# decclare a var outside and use inside the func

age = 23
def func():
    global 
    print("I am ",age," years old.")
func()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("i'm",x)
myfunc()
print("i'm",x)