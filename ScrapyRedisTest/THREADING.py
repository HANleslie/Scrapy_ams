# coding=utf-8

import threading

# num = 100
#
# def test(n):
#     global num
#     for i in range(10000000):
#         num = num -n
#         num = num +n
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=test,args=(6,))
#     t2 = threading.Thread(target=test,args=(9,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(num)


# ThreadLocal

# num = 0
# local = threading.local()
#
# def test(n):
#     local.x = num
#     for i in range(10000000):
#         local.x = local.x + n
#         local.x = local.x - n
#     print(threading.current_thread(),'---',local.x)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=test,args=(6,))
#     t2 = threading.Thread(target=test,args=(9,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(num)

# 全局锁
# from time import sleep
#
# lock = threading.Lock()
# num = 100
# t_list = []
#
# def fun():
#     global num
#     lock.acquire()
#     temp = num
#     sleep(0.00001)
#     temp -= 1
#     lock.release()
#
# for i in range(100):
#     t = threading.Thread(target=fun)
#     t_list.append(t)
#     t.start()
#
# for t in t_list:
#     t.join()
# print(num)

#控制线程数量semaphore

# sem = threading.Semaphore(3)
#
# def run():
#     with sem:
#         for i in range(5):
#             print(threading.current_thread())
# for i in range(5):
#     threading.Thread(target=run).start()


# 凑足一定数量才可以执行Barrier
# from time import sleep
#
# bar = threading.Barrier(3)
#
# def run():
#     print('start--',threading.current_thread())
#     sleep(2)
#     bar.wait()
#     print('end---',threading.current_thread())
#
# for i in range(5):
#     threading.Thread(target=run).start()


# 线程计时器
# def run():
#     print('start---',threading.current_thread())
#
# t = threading.Timer(2,run)
# t.start()
#
# t.join()
# print('stop---', threading.current_thread())
