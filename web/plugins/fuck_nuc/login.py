import json

from sanic.response import json as sanic_json

from config import sessions
from fuck.login import login
from web.plugins.fuck_nuc import api


@api.route('/fuck', methods=({"POST"}))
async def fuck_nuc(request):
    index = json.loads(request.body)
    user = index['user']
    password = index['password']
    if user is None or password is None:
        assert Exception("用户名或密码不能为空")
    session = login(user, password)
    sessions.append(session)
    return sanic_json({
        "code": 200,
        "msg": "success"
    })
