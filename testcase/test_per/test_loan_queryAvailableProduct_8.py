import pytest
import json
import random
import yaml
from tool.logger_ import logger
from api_util.per_util.per_api import loan_queryAvailableProduct, loan_repayTrialStage
from tool.object_path.file_path import america_yaml
from tool.redconfig import america_parma, YamlRed,america_parma_per


class Test_loan_queryAvailableProduct:

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('product', america_parma_per['queryAvailableProduct'])
    def test_loan_queryAvailableProduct(self, product):
        """
        查询真分期最大可借金额
        :param product:
        :return:
        """
        _result = loan_queryAvailableProduct(_param=(json.dumps(product)))
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True

    @pytest.mark.run(order=2)
    def test_loan_repayTrialStage(self):
        """
        还款试算接口,依赖queryAvailableProduct接口的返回值
        线获取真分期最大可借金额
        :return:
        """

        _rely_api = loan_queryAvailableProduct(
            _param=(json.dumps(random.choice(america_parma_per['queryAvailableProduct']))))
        params = {'merchantNo': '01', 'term': '1'}
        if _rely_api['success']:
            for _param in _rely_api.get('data'):
                params['laonAmount'] = _param['maxLoanAmount']
                params['loanDay'] = _param['loanDay']
                params['productNo'] = _param['productNo']
        else:
            logger.error(f"查询真分期最大可借金额失败:{_rely_api}")

        _result = loan_repayTrialStage(_param=json.dumps(params))
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True


if __name__ == '__main__':
    pytest.main(['-vs'])
