import requests

url = 'test.io/test'
msisdn = 79999999999
session = {"access_token": "test", "refresh_token": "test"}
headers = {'Content-Type': 'application/json'}


def start():
    for j in range(10, 24):
        for i in range(10, 60):
            params = {'msisdn': msisdn, 'time': f'YYYY-MM-DDT{j}:{i}'}
            r = requests.get(url=url + f'/var_1/var_2', cookies=session, headers=headers, params=params)
            print(r.text)
            assert r.status_code == 200
            assert r.json()["status"] == "ok"

    for j in range(10, 24):
        for i in range(10, 60):
            params = {'msisdn': msisdn, 'time': f'YYYY-MM-DDT{j}:{i}'}
            r = requests.get(url=url + f'/var_1/var_2?', params=params,
                             cookies=session, headers=headers)
            print(r.text)
            assert r.status_code == 200
            assert r.json()["status"] == "ok"


start()
