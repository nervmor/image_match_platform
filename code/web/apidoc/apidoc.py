"""
@api {result} /engine/result *code值说明*
@apiGroup _result
@apiName code值说明
@apiDescription 返回码code以及对应描述
@apiVersion 0.1.0


@apiSuccess {Number} 0 成功
@apiSuccess {Number} -1 请求的json格式不正确
@apiSuccess {Number} -2 请求的参数不正确
@apiSuccess {Number} -3 请求的HTTP Method不支持
@apiSuccess {Number} -4 请求的图片地址无法访问
@apiSuccess {Number} -5 请求参数maxdist不正确

"""


"""
@api {post} /engine/match/ match
@apiGroup engine
@apiName match
@apiDescription 对两组图片进行匹配并输出差距值
@apiVersion 0.1.0

@apiParam {String[]} url_src 对比图片数组
@apiParam {String[]} url_dst 被对比图片数组

@apiParamExample {json} 参数示例:
{
    "url_src" :
    [
        "http://www.nervmor.com/api/img/8c186f92ec604040962b2490a0d2ecfa",
        "http://www.nervmor.com/api/img/a87ff679a2f3e71d9181a67b7542122c"
    ],
    "url_dst" : 
    [
        "http://www.nervmor.com/api/img/622162fa514365fa3867ddce401378a7",
        "http://www.nervmor.com/api/img/67f1bf7400e3834476865298d3c3b179",
        "http://www.nervmor.com/api/img/89b689f47afb5779ecfe8b7e41477e02"
    ]
}

@apiUse api_success
@apiSuccess {Object[]} results 匹配结果
@apiSuccess {Object} results.url_src_value src图片对dst图片组的匹配结果
@apiSuccess {Number} results.url_src_value.url_dst_value src图片对dst图片组匹配的差距值
@apiSuccessExample {json} 成功:
HTTP/1.1 200 OK
{
    "code": 0,
    "results":
    {
        "http://www.nervmor.com/api/img/8c186f92ec604040962b2490a0d2ecfa" : 
        {
            "http://www.nervmor.com/api/img/622162fa514365fa3867ddce401378a7" : 0.332423432,
            "http://www.nervmor.com/api/img/67f1bf7400e3834476865298d3c3b179" : 0.25277,
            "http://www.nervmor.com/api/img/89b689f47afb5779ecfe8b7e41477e02" : 0.68254
        },

        "http://www.nervmor.com/api/img/a87ff679a2f3e71d9181a67b7542122c" : 
        {
            "http://www.nervmor.com/api/img/622162fa514365fa3867ddce401378a7" : 0.51848,
            "http://www.nervmor.com/api/img/67f1bf7400e3834476865298d3c3b179" : 0.025954,
            "http://www.nervmor.com/api/img/89b689f47afb5779ecfe8b7e41477e02" : 0.12179
        }
    }
}

@apiUse api_failure
@apiErrorExample {json} 失败:
    HTTP/1.1 400 
    {
        "code": -1,
        "error": "image url is invalid"
    }
"""



"""
@api {post} /img/ upload
@apiName upload
@apiGroup img
@apiDescription 上传图片到图片服务器
@apiVersion 0.1.0 

@apiParamExample 参数示例:
1. 使用标准的HTTP multitype/form 形式上传
2. 使用二进制流的形式上传:HTTP头部需要加入Content-Type:jpg/png/[..]，body部分为文件的二进制流

@apiSuccess {Boolean} ret 是否成功 
@apiSuccess {Object} info 图片信息
@apiSuccess {String} info.md5 图片的MD5
@apiSuccess {Number} info.size 图片的大小
@apiSuccessExample {json} 成功:
      HTTP/1.1 200 OK
      {
            "ret": true,
            "info" : 
            {
                "md5": "f5307fa900eb682e57d22a29c78a4ff5",
                "size": 281356
            }
      }

@apiError {Boolean} ret 是否成功
@apiError {Object} error 错误信息
@apiError {Number} error.code 错误代码
@apiError {String} error.message 错误说明
@apiErrorExample {json} 成功:
HTTP/1.1 200 OK
{"ret":false,"error":{"code":0,"message":"Internal error."}}
{"ret":false,"error":{"code":1,"message":"File type not support."}}
{"ret":false,"error":{"code":2,"message":"Request method error."}}
{"ret":false,"error":{"code":3,"message":"Access error."}}
{"ret":false,"error":{"code":4,"message":"Request body parse error."}}
{"ret":false,"error":{"code":5,"message":"Content-Length error."}}
{"ret":false,"error":{"code":6,"message":"Content-Type error."}}
{"ret":false,"error":{"code":7,"message":"File too large."}}
"""

"""
@api {get} /img/[md5] get
@apiName get
@apiGroup img
@apiDescription 根据参数得到相应的图片
@apiVersion 0.1.0 

@apiParam {Number} x 截取局部图片时的x坐标
@apiParam {Number} y 截取局部图片时的y坐标
@apiParam {Number} l 截取局部图片时的长度
@apiParam {Number} w 截取局部图片时的宽度

@apiParamExample 参数示例:
http://www.nervmor.com/api/img/f5307fa900eb682e57d22a29c78a4ff5?x=100&y=80&l=40&w=40 截取坐标为[100,80]尺寸为40*40的局部图片
http://www.nervmor.com/api/img/f5307fa900eb682e57d22a29c78a4ff5?x=0&y=0&l=60&w=60 截取坐标为[0,0](左上角)尺寸为60*60的局部图片
http://www.nervmor.com/api/img/f5307fa900eb682e57d22a29c78a4ff5 返回原图

"""

"""
@api {get} /img/[md5]?t=1 del
@apiName del
@apiGroup img
@apiDescription 删除图片
@apiVersion 0.1.0 

@apiParam {Number} t t=1时删除图片

@apiParamExample 参数示例:
http://www.nervmor.com/api/img/f5307fa900eb682e57d22a29c78a4ff5?t=1 删除图片

"""

"""
@apiDefine api_success
@apiSuccess {Number} code 成功时code=0
"""

"""
@apiDefine api_failure
@apiError {Number} code 失败时code<0
@apiError {String} error 失败原因说明
"""

"""
@api {post} /feature/phash/add/ add
@apiGroup feature
@apiName add
@apiDescription 录入特征
@apiVersion 0.1.0

@apiParam {String} pic_url 图片的地址
@apiParam {Number} feat_x 特征区域的X坐标
@apiParam {Number} feat_y 特征区域的Y坐标
@apiParam {Number} feat_w 特征区域的宽度
@apiParam {Number} feat_h 特征区域的高度
@apiParam {Number} feat_x_range 特征区域的X坐标的浮动范围
@apiParam {Number} feat_y_range 特征区域的Y坐标的浮动范围
@apiParam {Number} feat_w_range 特征区域的宽度的浮动范围
@apiParam {Number} feat_h_range 特征区域的高度的浮动范围
@apiParam {String} [metadata] 自定义标识数据(可选参数)

@apiParamExample {json} 参数示例:
{
    "url" : "http://www.nervmor.com/api/img/8c186f92ec604040962b2490a0d2ecfa",
    "feat_x" : 100,
    "feat_y" : 80,
    "feat_x_range" : 5,
    "feat_y_range" : 5,
    "feat_w" : 50,
    "feat_h" : 50,
    "feat_w_range" : 3,
    "feat_h_range" : 3,
        "metadata": 
    {
        "name" : "Jack's life", 
        "from" : "Jack.mp4",
        "size" : "1024 * 768",
        "format" : "jpg"
    }
}

@apiUse api_success
@apiSuccessExample {json} 成功:
    HTTP/1.1 200 OK
    {
        "code": 0,
    }

@apiUse api_failure
@apiErrorExample {json} 失败:
    HTTP/1.1 400 
    {
        "code": -1,
        "error": "image url is invalid"
    }
"""