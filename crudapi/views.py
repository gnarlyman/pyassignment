import logging
import json
import aiohttp.web as web

from datetime import datetime
from crudapi.kvstore import KVStore


logger = logging.getLogger(__name__)

routes = web.RouteTableDef()


@routes.get('/')
async def index_handler(_):
    return web.json_response({"title": "Crowdstrike Python Assignment Server"})


@routes.get('/guid')
async def guid_get_all(_):
    guids = KVStore.list()
    return web.json_response({'result': guids})


@routes.post('/guid')
async def guid_post(request):
    try:
        data = await request.json()
    except json.decoder.JSONDecodeError:
        return web.json_response({'result': 'decode json failed'}, status=400)

    if 'guid' not in data:
        return web.json_response({'result': 'data missing guid'}, status=400)

    # tack on some other data
    data.update({
        'expiration': datetime.utcnow().timestamp()
    })

    result = KVStore.create(data['guid'], data)

    if result:
        return web.json_response({'guid': result, 'result': 'post successful'})
    else:
        return web.json_response({'result': 'failed to post guid {}'.format(data['guid'])}, status=400)


@routes.view("/guid/{guid}")
class GUID(web.View):

    async def get(self):
        guid = self.request.match_info['guid']
        logger.debug("GET request for guid: {}".format(guid))

        result = KVStore.get(guid)

        if result:
            return web.json_response(result)
        else:
            logger.error("GET failed: {}".format(guid))
            return web.json_response({'result': 'failed to get guid {}'.format(guid)}, status=404)

    async def post(self):
        guid = self.request.match_info['guid']
        try:
            data = await self.request.json()
        except json.decoder.JSONDecodeError:
            return web.json_response({'result': 'decode json failed'}, status=400)

        logger.debug("POST request for guid: {}. Data: {}".format(guid, data))

        # tack on some other data
        data.update({
            'guid': guid,
            'expiration': datetime.utcnow().timestamp()
        })

        result = KVStore.create(guid, data)

        if result:
            return web.json_response({'guid': result, 'result': 'post successful'})
        else:
            return web.json_response({'result': 'failed to post guid {}'.format(guid)}, status=400)

    async def put(self):
        guid = self.request.match_info['guid']
        try:
            data = await self.request.json()
        except json.decoder.JSONDecodeError:
            return web.json_response({'result': 'decode json failed'}, status=400)

        logger.debug("PUT request for guid: {}".format(guid))

        result = KVStore.update(guid, data)

        if result:
            return web.json_response({'guid': result, 'result': 'put successful'})
        else:
            logger.error("PUT failed: {}".format(guid))
            return web.json_response({'result': 'failed to put guid {}'.format(guid)}, status=404)

    async def delete(self):
        guid = self.request.match_info['guid']
        logger.debug("DELETE request for guid: {}".format(guid))

        result = KVStore.delete(guid)

        if result:
            return web.json_response({'guid': result, 'result': 'delete successful'})
        else:
            logger.error("DELETE failed: {}".format(guid))
            return web.json_response({'result': 'failed to delete guid {}'.format(guid)}, status=404)
