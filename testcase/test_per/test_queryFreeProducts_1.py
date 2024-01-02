import pytest
from api_util.per_util.per_api import queryFreeProducts


class Test_queryFreeProducts:
    @pytest.mark.run(order=1)
    def test_queryFreeProducts(self):
        """
        查询用户可接产品接口,查询成功将响应结果,保存
        :return:
        """
        _result = queryFreeProducts(_param={})

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True
