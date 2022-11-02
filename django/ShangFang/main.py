#coding = utf-8
from utils.panda_util import readfile,isruncase
import pytest
import utils.replacekeyword as rp
from ShangFang.Dynamic import Dynamic_Param
import json
from utils.logger import logger
from utils.Requests_Utils import Send_Request
import re
class TestApi:
    @pytest.mark.parametrize('runcase',isruncase())
    def test_run(self,runcase):
        result = None
        relation = runcase['relation']
        method = runcase['method']
        url = runcase['url']
        header = eval(runcase['header'])
        cookies = eval(runcase['cookies'])
        data = eval(runcase['body'])
        case_name = runcase['case name']

        headers = self.correlation(header)
        datas = self.correlation(data)
        cookie = self.correlation(cookies)

        try:
            logger.info('正在执行用例{}'.format(case_name))
            resutl_data = Send_Request().send(url=url,method=method,headers=headers,cookies=cookie,data=datas)
            logger.info('请求结果{}'.format(resutl_data))
        except:
            logger.info('缺失参数，检查用例')

        if resutl_data:
            if relation != None:
                self.set_relation(relation, resutl_data)

        assert_res = self.assert_respoes
        return resutl_data


    def set_relation(self,data):
        res_data = rp.find(data)
        if res_data:
            replace_dict={}
            pattern = '[a-zA-z]+.A[^\s]*'
            cookie = self.test_run.request.headers.get('Cookie')
            re.findall(pattern,cookie)
            data = json.loads(rp.relace(data,replace_dict))
        return data

    def correlation(self,data):
        res_data = rp.find(data)
        # res_data = ['token']
        if res_data:
            replace_dict={}
            for i in res_data:
                # i = 'token'
                data_tmp = getattr(Dynamic_Param,str(i),"None")
                replace_dict.update({str(i):data_tmp})
                # replaec_dict = {'token':'sllkdslksd'}
            data = json.loads(rp.relace(data,replace_dict))
        return data

    def assert_respoes(self):