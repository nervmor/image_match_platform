class RESULT(object):
    SUCCESS = {'code' : 0}
    JSON_PARSE_ERROR = {'code' : -1, 'error' : 'json data parse fail'}
    PARAM_INVALID = {'code': -2, 'error': 'param invalid'}
    HTTP_METHOD_NOT_SUPPORT = {'code' : -3, 'error' : 'http method not support'}
    IMAGE_URL_INVALID = {'code' : -4, 'error' : 'image url is invalid'}
    MAXDIST_INVALID = {'code': -5, 'error': 'maxdist is not invalid'}
