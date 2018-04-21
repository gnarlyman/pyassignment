import logging
import asyncio
import aiohttp.web as web
import crudapi.jobs as jobs
from crudapi.views import routes


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s=%(lineno)s: %(message)s')
logger = logging.getLogger('crudapi')


async def start_background_tasks(app):
    app['expire_guids'] = app.loop.create_task(jobs.expire_guids())


async def cleanup_background_tasks(app):
    app['expire_guids'].cancel()
    await app['expire_guids']


async def create_app():
    loop = asyncio.get_event_loop()
    loop.create_task(jobs.expire_guids())
    app = web.Application(loop=loop)
    app.add_routes(routes)
    return app

if __name__ == '__main__':
    web.run_app(create_app(), port=8080)
