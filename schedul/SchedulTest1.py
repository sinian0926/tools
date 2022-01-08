import sched
import time
from datetime import datetime

# 初始化 sched 模块的 scheduler 类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)


# 被周期性调度触发的函数
def print_time(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    schedule.enter(inc, 0, print_time, (inc,))


# 默认参数 60 s
def start(inc=60):
    # enter四个参数分别为：间隔事件、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数、给触发函数的参数（tuple形式）
    schedule.enter(0, 0, print_time, (inc,))
    schedule.run()


class Schedule(object):
    def sch_first(self, n):
        from datetime import datetime
        import time
        # 每n秒执行一次
        while True:
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(n)

    def sch_second(self, inc):
        from datetime import datetime
        from threading import Timer
        # 打印时间函数
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        """
        Timer的参数说明
        inc:表示时间间隔
        print_time:执行的函数
        (inc,):传递给执行函数的参数
        """
        t = Timer(inc, self.sch_second, (inc,))
        t.start()


if __name__ == '__main__':
    schedule = Schedule()
    # first
    schedule.sch_first(5)
    # second
    schedule.sch_second(2)
    # third
    start(10)
