x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)






x = "awesome"

def myfunc():
    global x
    x = "fantas"

myfunc()

print("Python is " + x)
