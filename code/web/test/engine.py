import requests
import cv2
import numpy as np
import urllib

engine_srv_ip = '127.0.0.1:9090'
img_srv_ip = '127.0.0.1:4869'


def test_phash_engine(s_md5, d_md5):
    url = "http://" + engine_srv_ip + "/api/engine/phash/match/"

    url_s = "http://" + img_srv_ip + "/" + s_md5
    url_d = "http://" + img_srv_ip + "/" + s_md5 + "?x=10&y=10&w=10&h=10"

    req_data = {}
    req_data['url_src'] = []
    req_data['url_src'].append(url_s)
    req_data['url_dst'] = []
    req_data['url_dst'].append(url_d)
    try:
        r = requests.post(url, json = req_data)
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


def test_template_engine(s_md5, d_md5):
    url = "http://" + engine_srv_ip + "/api/engine/template/match/"

    url_s = "http://" + img_srv_ip + "/" + s_md5
    url_d = "http://" + img_srv_ip + "/" + d_md5

    req_data = {}
    req_data['url_src'] = []
    req_data['url_src'].append(url_s)
    req_data['url_dst'] = []
    req_data['url_dst'].append(url_d)
    try:
        r = requests.post(url, json = req_data)
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



def url_to_im(url, mode = 0):
    r = urllib.urlopen(url)
    im = np.asarray(bytearray(r.read()))
    im.astype(np.uint8)
    im = cv2.imdecode(im, mode)
    return im

def test_template_local():
    img = url_to_im('http://127.0.0.1:4869/a6b496de1c1329b670dd34386f96dbe3', 0)
    #img = cv2.imread("test.jpg", 0)
    img2 = img.copy()
    template = cv2.imread("tmp.jpg", 0)
    w, h = template.shape[::-1]

    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        img = img2.copy()

        method = eval(meth)

        res = cv2.matchTemplate(img, template, method)
        loc = np.where(res >= 0.7)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print min_val, max_val, min_loc, max_loc
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc




if __name__ == '__main__':
    #test_template_engine('5a6f52f08bf901a6aed84778b36c4e9a', '5a6f52f08bf901a6aed84778b36c4e9a?x=10&y=10&w=10&h=10')
    #test_template_engine('426777d2191aa13ca816930a66157b8b', '426777d2191aa13ca816930a66157b8b?x=10&y=10&w=30&h=25')
    test_phash_engine('5a6f52f08bf901a6aed84778b36c4e9a', 'a6b496de1c1329b670dd34386f96dbe3')
    #test_template_local()