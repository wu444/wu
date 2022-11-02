# coding=utf-8
import logging
import time
import os
# 获取文件的绝对路径
abs_path = os.path.abspath(__file__)
# print(abs_path)
# 获取文件所在目录的上一级目录,也就是根目录
project_path = os.path.dirname(os.path.dirname(abs_path))
# print(project_path)
# 通过os.sep的方法来获取config目录的全路径
_conf_path = project_path + os.sep + "config"
# 通过os.sep的方法来获取log日志目录的全路径
_log_path = project_path + os.sep + "log"
# 通过os.sep的方法来获取report报告目录的全路径
_report_path = project_path + os.sep + "report"

# 返回日志目录
def get_log_path():
    return _log_path

# 返回报告目录
def get_report_path():
    return _report_path

# 返回config目录
def get_config_path():
    return _conf_path
class Utils_Log():
    def __init__(self):
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        # 避免日志重复
        if not self.logger.handlers:
            self.log_name = '{}.log'.format(time.strftime("%Y_%m_%d",time.localtime()))
            self.log_path_file = os.path.join(get_log_path(),self.log_name)
            fh = logging.FileHandler(self.log_path_file,encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            fh.close()
    def log(self):
        return self.logger
logger = Utils_Log().log()
if __name__ == '__main__':
    logger.info('dddd')