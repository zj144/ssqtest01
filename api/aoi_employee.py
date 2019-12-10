import requests

import api
from api import BASE_URL, BASE_HEADERS


# 封装添加会员，操作会员（查，修，删）
class ApiEmployee:
    # 初始化
    # URL
    def __init__(self):
        self.url_add = BASE_URL + "/api/sys/user"
        self.url_employee = BASE_URL + "/api/sys/user/{}"
    # 增
    def api_post_employee(self,username,mobile,workNumber):
        data = {"username":username,"mobile": mobile,"workNumber":workNumber}
        return requests.post(url=self.url_add,json=data,headers=BASE_HEADERS)
    # 删
    def api_delete_employee(self,user_id):
        return requests.delete(self.url_employee.format(user_id),headers=BASE_HEADERS)
    # 改
    def api_put_employee(self,name):
        date = {"username":name}
        return requests.put(self.url_employee.format(api.user_id), json=date, headers=BASE_HEADERS)
    # 查
    def api_get_employee(self):
        return requests.get(self.url_employee.format(api.user_id), headers=BASE_HEADERS)
