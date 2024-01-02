from api_util.mex_util.mex_api import market_is_firsttime_loans_in_app


class Test_loans_in_app:
    def test_loans_in_app(self):
        """
        贷超-查询app内是否是首贷
        :return:
        """
        _result = market_is_firsttime_loans_in_app(_param=None)
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True
