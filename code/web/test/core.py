import requests


feat_srv_ip = '127.0.0.1'
img_srv_ip = '127.0.0.1:4869'


def test_core(md5, category):
    url = "http://" + feat_srv_ip + "/api/core/check/"

    img_url = "http://" + img_srv_ip + "/" + md5

    data = {}
    data['pic_url'] = img_url
    data['category'] = 'test'

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
    #test_core('a6b496de1c1329b670dd34386f96dbe3', 'test')
    test_core('5a6f52f08bf901a6aed84778b36c4e9a', 'test')