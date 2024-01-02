import json

import requests

from tool.logger_ import Log
from tool.redconfig import test_mex_host,test_per_host,test_phl_host


class RrestClient(object):
    conf_url = None

    def __init__(self):
        # 这个域名是配置文件里面的，传信贷的就调信贷的，传中台就调中台的，回头整个开关
        self.conf_url = test_per_host

    def get(self, url_, api_header, data):

        return self.requets_(method="GET", url_=url_, header_=api_header, data=data)

    def post(self, url_, api_header, data):
        return self.requets_(method="POST", url_=url_, header_=api_header, data=data)

    def put(self, url_, api_header, data):
        return self.requets_(method="PUT", url_=url_, header_=api_header, data=data)

    def delete(self, url_, api_header, data):
        return self.requets_(method="DELETE", url_=url_, header_=api_header, data=data)

    def requets_(self, method, url_, header_, data):
        self.logger_(method, url_, data)

        if method == "GET":
            return requests.request("GET", self.conf_url + url_, headers=header_, data=data)

        elif method == "POST":
            return requests.request("POST", self.conf_url + url_, headers=header_, data=data)

        elif method == "PUT":
            requests.request("PUT", self.conf_url + url_, headers=header_, data=data)

        elif method == "DELETE":
            requests.request("DELETE", self.conf_url + url_, headers=header_, data=data)

    @staticmethod
    def logger_(method, url_, parmas):
        Log().debug("接口请求的方式：{}".format(method))
        Log().debug("接口请求的地址: {}".format(test_per_host + url_))
        Log().debug("接口请求的参数: {}".format(json.dumps(parmas, indent=2)))


if __name__ == '__main__':
    url = "https://openapi-san.mongopay.top/gateway/simulation"

    payload = json.dumps({
        "appId": "8111134389",
        "merchantCode": "S820221215021653000000",
        "orderNum": "MEX2304201000203",
        "type": "CASH",
        "status": "1"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
