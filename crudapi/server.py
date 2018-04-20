import logging
import aiohttp.web as web
from crudapi.routes import routes

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(name)s=%(lineno)s: %(message)s')
logger = logging.getLogger('crudapi')


async def web_app():
    app = web.Application()
    app.add_routes(routes)
    return app

if __name__ == '__main__':
    test_app = web_app()
    web.run_app(test_app, port=8080)
