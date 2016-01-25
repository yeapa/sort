# 闭包
```
def func(name):
    def inner_func(age):
        print name,age
    return inner_func

if __name__=="__main__":
    bb=func("lily")
    bb(11)
```
这里inner_func就是一个闭包并且这个闭包持有自由变量name;


# 装饰器
```
def decorater_func(func):
    def wrapper(*args,**kwargs):
        print "wrapper running"
        return func(*args,**kwargs)
        print "wrapper ending"
    return wrapper


@decorater_func
def func():
    print "func running"
    ```
