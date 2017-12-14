import requests


feat_srv_ip = '127.0.0.1'
img_srv_ip = '127.0.0.1:4869'


def test_add_phash_feat(md5, x, y, w, h, r_x, r_y, r_w, r_h, metadata):
    url = "http://" + feat_srv_ip + "/api/feature/phash/add/"

    img_url = "http://" + img_srv_ip + "/" + md5

    data = {}
    data['category'] = 'test'
    data['pic_url'] = img_url
    data['dist'] = 0.3
    data['feat_x'] = x
    data['feat_y'] = y
    data['feat_w'] = w
    data['feat_h'] = h
    data['feat_x_range'] = r_x
    data['feat_y_range'] = r_y
    data['feat_w_range'] = r_w
    data['feat_h_range'] = r_h
    data['metadata'] = metadata

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

def test_get_phash_feat(wid, high):
    url = "http://" + feat_srv_ip + "/api/feature/phash/get/"
    data = {}
    data['category'] = 'test'
    data['pic_wid'] = wid
    data['pic_high'] = high
    try:
        r = requests.post(url, json=data)
    except (requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects):
        print "requests.post exception"
        return
    if r.status_code <> 200:
        print "http status_code not OK"
        return
    print r.json()

if __name__ == '__main__':
    #test_add_phash_feat('426777d2191aa13ca816930a66157b8b', 10, 10, 30, 25, 0, 0, 0, 0, "test jd [jbl]")
    #test_get_phash_feat(220, 220)

    test_add_phash_feat('5a6f52f08bf901a6aed84778b36c4e9a', 19, 4, 33, 38, 0, 0, 0, 0, "test taobao [Kuzi215]")
    test_get_phash_feat(193, 283)