define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./html/main.js",
    "group": "T__local_image_match_platform_code_web_apidoc_html_main_js",
    "groupTitle": "T__local_image_match_platform_code_web_apidoc_html_main_js",
    "name": ""
  },
  {
    "type": "post",
    "url": "/engine/add/",
    "title": "add",
    "group": "engine",
    "name": "add",
    "description": "<p>导入一张网络图片到样本库中</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "metadata",
            "description": "<p>自定义标识数据(可选参数)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "url",
            "description": "<p>图片的地址</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "{\n    \"metadata\": \n    {\n        \"name\" : \"Jack's life\", \n        \"from\" : \"Jack.mp4\",\n        \"size\" : \"1024 * 768\",\n        \"format\" : \"jpg\"\n    },\n    \"url\" : \"http://www.nervmor.com/storage/0/5643F2AC451D034“\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\n  \"code\": 0,\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>成功时code=0</p>"
          }
        ]
      }
    },
    "error": {
      "examples": [
        {
          "title": "失败:",
          "content": "HTTP/1.1 400 \n{\n  \"code\": -1,\n  \"error\": \"image url is invalid\"\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>失败时code&lt;0</p>"
          },
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "error",
            "description": "<p>失败原因说明</p>"
          }
        ]
      }
    },
    "filename": "./apidoc.py",
    "groupTitle": "engine"
  },
  {
    "type": "result",
    "url": "/engine/result",
    "title": "*code值说明*",
    "group": "engine",
    "name": "code___",
    "description": "<p>返回码code以及对应描述</p>",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "0",
            "description": "<p>成功</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-1",
            "description": "<p>请求的json格式不正确</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-2",
            "description": "<p>请求的参数不正确</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-3",
            "description": "<p>请求的HTTP Method不支持</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-4",
            "description": "<p>请求的图片地址无法访问</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-5",
            "description": "<p>请求参数maxdist不正确</p>"
          }
        ]
      }
    },
    "filename": "./apidoc.py",
    "groupTitle": "engine"
  },
  {
    "type": "post",
    "url": "/engine/match/",
    "title": "match",
    "name": "match",
    "group": "engine",
    "description": "<p>将该图片和库中所有图片进行匹配并返回匹配结果</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "url",
            "description": "<p>图片的地址</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "maxdist",
            "description": "<p>最大差距度(可选参数),必须为浮点数</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "{\n    \"url\" : \" http://www.nervmor.com/storage/0/5643F2AC451D034\",\n    \"maxdist\" : 0.5\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "results",
            "description": "<p>匹配结果</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "results.metadata",
            "description": "<p>自定义信息cmd</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "results.url",
            "description": "<p>图片的url</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "results.dist",
            "description": "<p>匹配差距度得分，分数越低表示匹配度越高</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>成功时code=0</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\n      \"code\": 0,\n      \"results\" : \n      [\n          {\n              \"metadata\": \n              {\n                  \"name\" : \"Jack's life\", \n                  \"from\" : \"Jack.mp4\",\n                  \"size\" : \"1024 * 768\",\n                  \"format\" : \"jpg\"\n              },\n              \"url\" : \"http://www.nervmor.com/storage/0/5643F2AC451D034\",\n              \"dist\" : 0.0\n          },\n          {\n              \"metadata\": \n              {\n                  \"name\" : \"Tom's life\", \n                  \"from\" : \"Tom.mp4\",\n                  \"size\" : \"800 * 600\",\n                  \"format\" : \"png\"\n              },\n              \"url\" : \"http://www.nervmor.com/storage/3/B874C76F7E120016\",\n              \"dist\" : 0.5232368\n          }\n      ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "失败:",
          "content": "HTTP/1.1 400 OK\n{\n  \"code\": -1,\n  \"error\": \"image url is invalid\"\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>失败时code&lt;0</p>"
          },
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "error",
            "description": "<p>失败原因说明</p>"
          }
        ]
      }
    },
    "filename": "./apidoc.py",
    "groupTitle": "engine"
  },
  {
    "type": "post",
    "url": "/engine/remove/",
    "title": "remove",
    "group": "engine",
    "name": "remove",
    "description": "<p>样本库中删除该图片</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "url",
            "description": "<p>图片的地址</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "{\n    \"url\" : \"http://www.nervmor.com/storage/0/5643F2AC451D034“\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "result",
            "description": "<p>匹配结果</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "result.delcnt",
            "description": "<p>删除的图片个数</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>成功时code=0</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\n  \"code\": 0,\n  \"result\":\n  {\n      \"delcnt\": 1\n  }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "失败:",
          "content": "HTTP/1.1 400 \n{\n  \"code\": -1,\n  \"error\": \"image url is invalid\"\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>失败时code&lt;0</p>"
          },
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "error",
            "description": "<p>失败原因说明</p>"
          }
        ]
      }
    },
    "filename": "./apidoc.py",
    "groupTitle": "engine"
  },
  {
    "type": "get",
    "url": "/img/[md5]?t=1",
    "title": "del",
    "name": "del",
    "group": "img",
    "description": "<p>删除图片</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "t",
            "description": "<p>t=1时删除图片</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "/img/f5307fa900eb682e57d22a29c78a4ff5?t=1 删除图片",
          "type": "json"
        }
      ]
    },
    "filename": "./apidoc.py",
    "groupTitle": "img"
  },
  {
    "type": "get",
    "url": "/img/[md5]",
    "title": "get",
    "name": "get",
    "group": "img",
    "description": "<p>根据参数得到相应的图片</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "x",
            "description": "<p>截取局部图片时的x坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "y",
            "description": "<p>截取局部图片时的y坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "l",
            "description": "<p>截取局部图片时的长度</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "w",
            "description": "<p>截取局部图片时的宽度</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "/img/f5307fa900eb682e57d22a29c78a4ff5?x=100&y=80&l=40&w=40 截取坐标为[100,80]尺寸为40*40的局部图片\n/img/f5307fa900eb682e57d22a29c78a4ff5?x=0&y=0&l=60&w=60 截取坐标为[0,0](左上角)尺寸为60*60的局部图片\n/img/f5307fa900eb682e57d22a29c78a4ff5 返回原图",
          "type": "json"
        }
      ]
    },
    "filename": "./apidoc.py",
    "groupTitle": "img"
  },
  {
    "type": "post",
    "url": "/img/",
    "title": "upload",
    "name": "upload",
    "group": "img",
    "description": "<p>上传图片到图片服务器</p>",
    "version": "0.1.0",
    "parameter": {
      "examples": [
        {
          "title": "参数示例:",
          "content": "1. 使用标准的HTTP multitype/form 形式上传\n2. 使用二进制流的形式上传:HTTP头部需要加入Content-Type:jpg/png/[..]，body部分为文件的二进制流",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "ret",
            "description": "<p>是否成功</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "info",
            "description": "<p>图片信息</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "info.md5",
            "description": "<p>图片的MD5</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "info.size",
            "description": "<p>图片的大小</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\n      \"ret\": true,\n      \"info\" : \n      {\n          \"md5\": \"f5307fa900eb682e57d22a29c78a4ff5\",\n          \"size\": 281356\n      }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "Boolean",
            "optional": false,
            "field": "ret",
            "description": "<p>是否成功</p>"
          },
          {
            "group": "Error 4xx",
            "type": "Object",
            "optional": false,
            "field": "error",
            "description": "<p>错误信息</p>"
          },
          {
            "group": "Error 4xx",
            "type": "Number",
            "optional": false,
            "field": "error.code",
            "description": "<p>错误代码</p>"
          },
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "error.message",
            "description": "<p>错误说明</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\"ret\":false,\"error\":{\"code\":0,\"message\":\"Internal error.\"}}\n{\"ret\":false,\"error\":{\"code\":1,\"message\":\"File type not support.\"}}\n{\"ret\":false,\"error\":{\"code\":2,\"message\":\"Request method error.\"}}\n{\"ret\":false,\"error\":{\"code\":3,\"message\":\"Access error.\"}}\n{\"ret\":false,\"error\":{\"code\":4,\"message\":\"Request body parse error.\"}}\n{\"ret\":false,\"error\":{\"code\":5,\"message\":\"Content-Length error.\"}}\n{\"ret\":false,\"error\":{\"code\":6,\"message\":\"Content-Type error.\"}}\n{\"ret\":false,\"error\":{\"code\":7,\"message\":\"File too large.\"}}",
          "type": "json"
        }
      ]
    },
    "filename": "./apidoc.py",
    "groupTitle": "img"
  }
] });
