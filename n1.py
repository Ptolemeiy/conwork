class MyException(Exception):
    pass
try:
    def decorator(speedpluss):
        def wrapper():
            a=speedpluss()
            if a == str():
                raise ValueError
            v0=speedpluss()
            if v0 == str():
                raise ValueError
            t=speedpluss()
            if t == str():
                raise ValueError
            elif t == 0:
                raise MyException
            distance = v0 + (a * (t * t))/2
            print('Расстояние ->',distance)
            return distance
        return wrapper

    @decorator
    def speedpluss():
        beginspeed = int(input())
        if beginspeed == str():
                raise ValueError
        endspeed = int(input())
        if endspeed == str():
                raise ValueError
        time = int(input())
        if time == str():
                raise ValueError
        elif time == 0:
            raise MyException
        speedplus = (beginspeed - endspeed)/time
        print('Ускорение ->',speedplus)
        return speedplus
    n = speedpluss()

except MyException:
    print('Убери нули')
except ValueError:
    print('Введи данные нормально')



