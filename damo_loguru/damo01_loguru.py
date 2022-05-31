# loguru ，模块
"""
日志格式化
输出不同级别的日志
日志输出到文件
日志显示不同颜色  （着色）
直接生成对象，有且仅有一个对象(loguru)

"""

#1 安装 pip install loguru

#2 导入

from loguru import logger


#3 打印
logger.info("hello world")

# 输出不同日志级别:
# debug : 调试日志
# info ：普通日志
# warning ：警告日志
# success ：成功日志
# error ：错误日志

logger.debug("这是一条Debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

#  输出到文件 :add()  用于将日志写到本地文件中
# sys.stderr ： 输出文件
# format ：设置格式化
# level ：设置级别


# logger.add('a.log',level='DEBUG')
logger.add("a.log", format="{time} {level} {message}", level="INFO")

logger.debug("这是一条Debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")

# 进行传入参数的格式化
logger.info("{}在{}","张三","学习")

