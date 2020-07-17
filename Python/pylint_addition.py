'''
1.Adding two numbers
2.Adding list of numbers
'''
def addition(*args):
    if len(args) == 2:
        return args[0] + args[1]
    elif len(args) > 2:
        print("Refer Doc string")
    else:
        A = 0
        for i in args[0]:
            A = A + i
        return A
