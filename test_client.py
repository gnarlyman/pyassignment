import requests
import unittest


class TestCRUDApi(unittest.TestCase):
    server = 'http://localhost:8080'

    def test010_get_404(self):
        guid = '183d81166f9e47eb8f97c4873259c9d2294de000'
        req = requests.get('{}/guid/{}'.format(self.server, guid))
        self.assertEqual(req.status_code, 404)

    def test020_post_bad_json(self):
        req = requests.post('{}/guid'.format(self.server), data='test')
        self.assertEqual(req.status_code, 400)

    def test030_post_good_json(self):
        guid = '183d81166f9e47eb8f97c4873259c9d2294de006'
        req = requests.post('{}/guid'.format(self.server), json={
            'guid': guid,
            'expiration': '1528013111',
            'data': 'some data'
        })
        self.assertEqual(req.status_code, 200)

    def test040_post_good_json2(self):
        guid = '183d81166f9e47eb8f97c4873259c9d2294de010'
        req = requests.post('{}/guid/{}'.format(self.server, guid), json={
            'expiration': '1528013111',
            'data': 'some data'
        })
        self.assertEqual(req.status_code, 200)

    def test050_put_404(self):
        guid = '183d81166f9e47eb8f97c4873259c9d2294de000'
        req = requests.put('{}/guid/{}'.format(self.server, guid), json={
            'expiration': '0000000000'
        })
        self.assertEqual(req.status_code, 404)

    def test060_put_200(self):
        guid = '183d81166f9e47eb8f97c4873259c9d2294de010'
        req = requests.put('{}/guid/{}'.format(self.server, guid), json={
            'arbitrarykey': '0000000000'
        })
        response_data = req.json()
        self.assertEqual(response_data['guid']['arbitrarykey'], '0000000000')
        self.assertEqual(req.status_code, 200)

    def test070_delete_200(self):
        guid = '183d81166f9e47eb8f97c4873259c9d2294de006'
        req = requests.delete('{}/guid/{}'.format(self.server, guid))
        self.assertEqual(req.status_code, 200)


if __name__ == '__main__':
    unittest.main()
