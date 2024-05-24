# def func1():
#     param = 4
#     def inner():
#         param += 1
#     return param

# print(func1())
#ошибок не выдаёт, выводит 4

def func2():
    param = 4 
    
    def inner(var):
        var += 1 
        
    inner(param)
    return param
    
#ошибок не находит, выводит 4

def func3():
    param = 4
    
    def inner(var):
        var += 1
        return var
        
    param = inner(param)
    
#ошибок не находит, выводит none