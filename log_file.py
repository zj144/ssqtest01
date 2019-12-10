import logging
import time

from logging.handlers import TimedRotatingFileHandler

from tools.path import path_hr

# 创建日志输入
logger = logging.getLogger(name="song")
logger.setLevel(logging.INFO)
# 创建日志输出
shl = logging.StreamHandler()
# 时间命名输出到日志
trfh = logging.handlers.TimedRotatingFileHandler(filename=f"{path_hr()}/log/{time.strftime('%Y%m%d%H%M%S')}.log",
                                          when="M",interval=1,backupCount=0,encoding="utf-8")
# 日志格式
num = "%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"
fmt = logging.Formatter(fmt=num)
# 输出设置格式
trfh.setFormatter(fmt)
shl.setFormatter(fmt)
# 输入添加输出
logger.addHandler(shl)
logger.addHandler(trfh)
