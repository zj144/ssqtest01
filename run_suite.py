import unittest

from tools.HTMLTestReportCN import HTMLTestRunner
from tools.path import path_hr

suite = unittest.defaultTestLoader.discover("./scripts")

with open(f"{path_hr()}/report/report.html","wb") as f:
    HTMLTestRunner(stream=f,title="登录，添加，修改，查询，删除").run(suite)

# if __name__ == '__main__':
#     with open(f"{path_hr()}/report/report.html", "r",encoding="utf8") as r:
#         print(r.read())