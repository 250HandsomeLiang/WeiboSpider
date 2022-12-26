# 封装一个日志模块
import logging, time
import os
from logging.handlers import RotatingFileHandler

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))  # 获取本地路径
log_path = os.path.join(path, 'logs')  # log_path是存放日志的路径
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path): os.mkdir(log_path)

class Log():
    def __init__(self):
        # 文件的命名
        self.logname = os.path.join(log_path, './%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter(f'%(asctime)s -| %(filename)s->%(funcName)s -| line:%(lineno)d [%(levelname)s] %(message)s')
        self.__create_log()
    def __create_log(self):
        # 创建一个fileHander，用于写入本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        # fh =  RotatingFileHandler(self.logname, maxBytes=1 * 1024, backupCount=3)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输入到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        # 关闭打开文件
        fh.close()
        ch.close()
    def getlog(self):
        return self.logger

log=Log()
if __name__ == '__main__':
    log.getlog().info("hello world")
    log.getlog().warning("测试")

