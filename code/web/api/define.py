
class RESULT(object):
    SUCCESS = {'code' : 0, 'msg' : 'success'}
    JSON_PARSE_ERROR = {'code' : -1, 'msg' : 'json data parse fail'}
    PARAM_INVALID = {'code': -2, 'msg': 'param invalid'}
    HTTP_METHOD_NOT_SUPPORT = {'code' : -3, 'msg' : 'http method not support'}
    IMAGE_URL_INVALID = {'code' : -4, 'msg' : 'image url is invalid'}
