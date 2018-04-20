import requests

server = 'http://localhost:8080'

test_get_404 = requests.get('{}/guid/183d81166f9e47eb8f97c4873259c9d2294de000'.format(server))
print(test_get_404.json())
assert test_get_404.status_code == 404

test_post_bad_json = requests.post('{}/guid'.format(server), data='test')
print(test_post_bad_json.json())
assert test_post_bad_json.status_code == 400

test_post_good_json = requests.post('{}/guid'.format(server), json={
    'guid': '183d81166f9e47eb8f97c4873259c9d2294de006',
    'expiration': '1528013111',
    'data': 'some data'
})
print(test_post_good_json.json())
assert test_post_good_json.status_code == 200

test_post_good_json2 = requests.post('{}/guid/183d81166f9e47eb8f97c4873259c9d2294de010'.format(server), json={
    'expiration': '1528013111',
    'data': 'some data'
})
print(test_post_good_json2.json())
assert test_post_good_json2.status_code == 200

test_put_404 = requests.put('{}/guid/183d81166f9e47eb8f97c4873259c9d2294de000'.format(server), json={
    'expiration': '0000000000'
})
print(test_put_404.json())
assert test_put_404.status_code == 404

test_put_200 = requests.put('{}/guid/183d81166f9e47eb8f97c4873259c9d2294de010'.format(server), json={
    'expiration': '0000000000'
})
response_data = test_put_200.json()
print(response_data)
assert response_data['guid']['expiration'] == '0000000000'
assert test_put_200.status_code == 200

test_delete_200 = requests.delete('{}/guid/183d81166f9e47eb8f97c4873259c9d2294de006'.format(server))
print(test_delete_200.json())
assert test_delete_200.status_code == 200
