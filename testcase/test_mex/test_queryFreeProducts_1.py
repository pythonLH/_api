import pytest
from api_util.mex_util.mex_api import queryFreeProducts


class Test_queryFreeProducts:
    @pytest.mark.run(order=1)
    def test_queryFreeProducts(self):
        """
        该接口不需要传参数,简直就是鬼扯
        :return:
        """
        _result = queryFreeProducts(_param={})

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True
