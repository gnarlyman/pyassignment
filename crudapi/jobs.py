import asyncio
import logging
from datetime import datetime, timedelta
from crudapi.kvstore import KVStore

logger = logging.getLogger(__name__)


async def expire_guids():
    while True:
        logger.debug('expiring guids job started')
        for guid in KVStore.list():
            expiration = datetime.fromtimestamp(float(guid['expiration']))
            if datetime.utcnow() - timedelta(seconds=10) >= expiration:
                logger.info('guid expired: {}'.format(guid))
                KVStore.delete(guid['guid'])

        await asyncio.sleep(10)
