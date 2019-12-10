import requests

from api import BASE_HEADERS, BASE_URL


class ApiLogin:
    # URL
    def __init__(self):
        self.url = BASE_URL + "/api/sys/login"
    # 登录
    def api_login(self,mobile,password):
        data = {"mobile":mobile, "password":password}
        return requests.post(url=self.url,json=data,headers=BASE_HEADERS)