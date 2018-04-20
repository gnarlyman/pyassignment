class KVStore(object):
    __store__ = dict()

    @staticmethod
    def create(key, data):
        KVStore.__store__.update({
            key: data
        })
        return KVStore.__store__[key]

    @staticmethod
    def update(key, data):
        if key in KVStore.__store__:
            KVStore.__store__[key].update(data)
            return KVStore.__store__[key]
        else:
            return None

    @staticmethod
    def get(key):
        if key in KVStore.__store__:
            return KVStore.__store__[key]
        else:
            return None

    @staticmethod
    def delete(key):
        if key in KVStore.__store__:
            return KVStore.__store__.pop(key)
        else:
            return None

    @staticmethod
    def list():
        return list(KVStore.__store__.values())
