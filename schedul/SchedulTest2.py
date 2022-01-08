# from datetime import datetime
#
# from apscheduler.schedulers.blocking import BlockingScheduler
#
#
# def job():
#     print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# if __name__ == '__main__':
#     # forth
#     scheduler = BlockingScheduler()
#     scheduler.add_job(job, 'interval', seconds=5)
#     scheduler.start()
