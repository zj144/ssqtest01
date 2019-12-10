import json
import unittest

from parameterized import parameterized

from api import BASE_HEADERS
from api.api_login import ApiLogin
from tools.assert_common import assert_common
from tools.path import path_hr


def read_data_json_login():
    with open(f"{path_hr()}/data/data_json_login.json", "rb")as f:
        return [(tuple(json.load(f).values()))]


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取登录对象
        cls.apilogin = ApiLogin()

    # 结束
    @classmethod
    def tearDownClass(cls):
        pass

    # 测试用例
    @parameterized.expand(read_data_json_login())
    def test_login(self, mobile, password):
        f = self.apilogin.api_login(mobile, password)
        print(f.json())
        # 提取token
        BASE_HEADERS["Authorization"] = "Bearer " + f.json().get("data")
        print(BASE_HEADERS)
        assert_common(s=self, response=f)
