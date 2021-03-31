# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from multiprocessing import Pool
from time import sleep

from fuck.login import *
from config.config import *


def fuck(session):
    course = session.get(course_url).json()['data']
    while True:
        try:
            fuck_nuc_course(session, course)
        except:
            sessions.remove(session)
            sessions.append(login(session.get("username"), session.get("password")))
        sleep(3)


if __name__ == '__main__':
    pool = Pool(4)
    for acc, passwd in users.items():
        try:
            sessions.append(login(account=acc, password=passwd['password']))
        except Exception as e:
            print(e)
    pool.map(fuck, sessions)

    # for i in range(0, 4):
    #     Thread(target=fuck, args=(session, course,)).start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
