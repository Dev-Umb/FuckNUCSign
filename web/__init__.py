from multiprocessing import Pool

from sanic import Sanic

from config import sessions
from web.Until.getCourse import fuck
from web.plugins import content

app = Sanic(__name__)

app.blueprint(content)

if __name__ == '__main__':
    pool = Pool(4)
    pool.map(fuck, sessions)
    app.run(host='127.0.0.1', port=8080)
