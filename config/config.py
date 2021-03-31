users = {
    "test": {
        'password': '123456'
    },

}
sessions = []
term = 1
year = 2020
year1 = 2021
base_url = 'http://zjhx.nuc.edu.cn/'
url = f'{base_url}api/auth/jwt/token'
login_url = f'{base_url}api/user/user/front/info?'
course_url = f'{base_url}api/teach/teachCourse/listStuCourse' \
             f'?id={term}&year={year}&year1={year1}&term={term}'
sign_url = f'{base_url}api/teach/teachCourseSign/getStuCurSign?courseId='
