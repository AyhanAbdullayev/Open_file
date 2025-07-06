from datetime import date 
from os.path import exists


if not exists("table.txt"):
    with open("table.txt","w") as f:
        f.write("Function name   |Worked Time|Arguments|Keyword Arguments|Result\n")

def calculation(a):
    def inner(*args,**kwargs):
        try:
            result = a(*args,**kwargs)
            result = str(result)
        except ZeroDivisionError as Z:
            result = str(Z)
        a_name = f"{a.__name__:<16}"
        Worked_time = f"{date.today()}"
        Args = ",".join(map(str,args))
        Kwargs = ",".join([f"{key}={value}" for key,value in kwargs.items()])
        with open("table.txt","a") as f:
            f.write(f"{a_name}| {Worked_time}|  {Args}   |       {Kwargs}          |{result}\n")
    return inner

@calculation

def sum(a,b):
    return a+b

@calculation

def divide(a,b):
    return a/b

@calculation

def diff(a,b):
    return a-b

@calculation

def multiple(a,b):
    return a*b


sum(10,1)
diff(10,1)
multiple(10,1)
divide(10,1)