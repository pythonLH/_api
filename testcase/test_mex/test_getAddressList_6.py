import pytest
from api_util.mex_util.mex_api import getAddressList


class Test_getAddressList:
    @pytest.mark.run(order=1)
    def test_getAddressList(self):
        """
        获取省市区接口
        :return:
        """
        _result = getAddressList(_param='0')
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True

    @pytest.mark.run(order=2)
    def test_getAddressList_1(self):
        """
        获取省市区接口
        :return:
        """
        _result = getAddressList(_param='1')
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True
        assert _result['data'] == []
