# coding=utf-8
import requests
from utils.logger import logger
class Send_Request:
    def api_run(self,url,method,data=None,headers=None,cookies=None):
        res = None
        logger.info("请求的url为{},类型为{}".format(url,type(url)))
        logger.info("请求的method为{},类型为{}".format(method, type(method)))
        logger.info("请求的data为{},类型为{}".format(data, type(data)))
        logger.info("请求的headers为{},类型为{}".format(headers, type(headers)))
        logger.info("请求的cookies为{},类型为{}".format(cookies, type(cookies)))
        if method == "get":
            res = requests.get(url,data=data,headers=headers,cookies=cookies)
        elif method == "post":
            if headers == {"Content-Type": "application/json"}:
                res = requests.post(url,json=data,headers=headers,cookies=cookies)
            elif headers == {"Content-Type": "application/x-www-form-urlencoded"}:
                res = requests.post(url,data=data,headers=headers,cookies=cookies)
        code = res.status_code
        cookies = res.cookies.get_dict()
        dict1 = dict()
        try:
            body = res.json()
        except:
            body = res.text
        dict1['code'] = code
        dict1['body'] = body
        dict1['cookies'] = cookies
        return dict1

    def send(self,url,method,**kwargs):
        return self.api_run(url=url,method=method,**kwargs)

if __name__ == '__main__':
    url = "http://192.168.91.1"
    data = {"userName":"admin","password":"2e091d726df4fc627c0a691650bd796a","https":False,"key":1606792942688}
    method = "post"
    headers = {"Content-Type": "application/json"}
    print(Send_Request().send(url=url,method=method,headers=headers,data=data))