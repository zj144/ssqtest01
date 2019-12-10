# 导包
import logging
import unittest

from parameterized import parameterized

import api, log_file
from api.aoi_employee import ApiEmployee
from tools.assert_common import assert_common
from tools.path import path_hr


def read_data_txt():
    with open(f"{path_hr()}/data/data_txt.txt","r",encoding="utf-8") as f:
        num = []
        for data in f.readlines():
            num.append(data.strip().split(","))
        return num[1::]


# 创建测试类 并继承unittest.TestCase
class TestEmployee(unittest.TestCase):
    # 初始化  获取对象
    @classmethod
    def setUpClass(cls):
        cls.apiemplyee = ApiEmployee()

    # 测试用例
    @parameterized.expand(read_data_txt())
    def test01_add(self,username,mobile,workNumber):
        logging.info(f"{username}，{mobile}，{workNumber}")
        r = self.apiemplyee.api_post_employee(username,mobile,workNumber)
        logging.info(f"HR系统添加会员响应json信息{r.json()}")
        print(r.json())
        api.user_id = r.json().get("data").get("id")
        assert_common(self,r)

    def test04_delete(self):
        f = self.apiemplyee.api_delete_employee(api.user_id)
        logging.info(f"HR系统删除会员响应json信息{f.json()}")
        print(f.json())
        assert_common(self, f)
    def test03_update(self,name="sssyi"):
        g = self.apiemplyee.api_put_employee(name=name)
        print(g.json())
        assert_common(self,g)
    def test02_get(self):
        h = self.apiemplyee.api_get_employee()
        print(h.json())
        assert_common(self,h)
