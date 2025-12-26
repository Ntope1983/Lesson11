# If we change the reference inside the faction the arg will change arg = [3]. but out the faction when the faction end the reference will be the same as before we call the faction like mutable
def f(arg):
    print(arg)
    print(f"id arg={id(arg)}")
    arg = [3]
    print(arg)
    print(f"id arg={id(arg)}")


l = 1
print(l)
print(f"id l={id(l)}")
f(l)
print(l)
print(f"id l={id(l)}")
