# coding=utf-8
import json
from string import Template
import re
def find(data):
    # 此时data为空字典{}
    if isinstance(data,dict):
        data = json.dumps(data)
        pattern = "\${(.*?)}"
        return re.findall(pattern,data)

def relace(ori_data,replace_data):
    ori_data = json.dumps(ori_data)
    s = Template(ori_data)
    res = s.safe_substitute(replace_data)
    return res

if __name__ == '__main__':
    ori_data = {"admin-token": "${token}"}
    replace_data = {'token': 'sllkdslksd'}
    print(relace(ori_data,replace_data))