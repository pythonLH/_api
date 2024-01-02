import pytest
import json
from tool.logger_ import logger
from tool.redconfig import america_parma
from api_util.mex_util.mex_api import saveMarketInfo, getMarketInfo


class Test_saveMarketInfo:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('userinfo', america_parma["saveMarketInfo"])
    def test_saveMarketInfo_normal(self, userinfo):
        """
        保存贷超用户信息-正向用例
        :return:
        """
        logger.info(userinfo["title"])
        _result = saveMarketInfo(_param=json.dumps(userinfo["case param"]))
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('userinfo', america_parma["saveMarketInfo_two"])
    def test_saveMarketInfo_abnormal(self, userinfo):
        """
        保存贷超用户信息-异常用例
        :param userinfo:
        :return:
        """
        logger.info(userinfo["title"])
        _result = saveMarketInfo(_param=json.dumps(userinfo["case param"]))
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True

    @pytest.mark.run(order=2)
    def test_getMarketInfo(self):
        """
        获取贷超用户信息-正常用例
        :return:
        """
        _result = getMarketInfo(_param=None)
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True
