from time import sleep

from config import course_url, sessions
from fuck.login import fuck_nuc_course, login


def fuck(session):
    course = session.get(course_url).json()['data']
    while True:
        try:
            fuck_nuc_course(session, course)
        except :
            sessions.remove(session)
            sessions.append(login(session.get("username"),session.get("password")))
        sleep(1)