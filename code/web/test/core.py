import requests


core_srv_ip = '127.0.0.1:9090'
img_srv_ip = '127.0.0.1:4869'


def test_core(md5, category):
    url = "http://" + core_srv_ip + "/api/core/check/"

    img_url = "http://" + img_srv_ip + "/" + md5

    data = {}
    data['pic_url'] = img_url
    data['class'] = {
        'category' : ['test']
    }

    try:
        r = requests.post(url, json = data)
    except (requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects):
        print "requests.post exception"
        return
    if  r.status_code <> 200:
        print "http status_code not OK"
        return
    print r.json()


if __name__ == '__main__':
    test_core('e3c2c4b85ccd96d16eee6b5882d52b3d', 'test')