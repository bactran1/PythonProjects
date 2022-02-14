import threading
import time


def func1(x):
    print(f'func1-start{x}')
    time.sleep(3)
    print('func1-end')

def func2(x):
    print(f'func2-start{x}')
    time.sleep(1)
    print('func2-end')


t1 = threading.Thread(target=func1, args=(14,))
t2 = threading.Thread(target=func2, args=(22,))
t1.start()
t2.start()
print(threading.activeCount())


