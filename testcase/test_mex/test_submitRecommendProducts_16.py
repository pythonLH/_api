import pytest
import json
import random
import yaml
from tool.logger_ import logger
from api_util.mex_util.mex_api import submitOneProduct, loan_queryAvailableProduct
from tool.object_path.file_path import america_yaml
from tool.redconfig import america_parma, YamlRed,america_parma_per


class Test_submitOneProduct:
    def setup_class(self):
        """
        先调用loan_queryAvailableProduct
        :return:
        """
        _parma = america_parma['queryAvailableProduct'][0]
        _result = loan_queryAvailableProduct(json.dumps(_parma))

        # 定义提交借款接口的依赖参数
        merchantNo = _parma['merchantNo']
        orgNo = _parma['orgNo']
        applyLoanAmount = None
        firstExpectDay = None
        productNo = None
        for value in _result.values():
            if type(value) is list:
                for item in value:
                    applyLoanAmount = item['maxLoanAmount']
                    firstExpectDay = item['fistInstallmentDays']
                    productNo = item['productNo']
        return merchantNo, orgNo, applyLoanAmount, firstExpectDay, productNo

    def teardown_class(self):
        pass

    @pytest.mark.parametrize('_submitOneProduct', america_parma['submitOneProduct'])
    def test_submitOneProduct(self, _submitOneProduct):

        for item in america_parma['submitOneProduct']:
            item['applyLoanAmount'] = self.setup_class()[2]
            item['firstExpectDay'] = self.setup_class()[3]
            item['productNo'] = self.setup_class()[-1]
        print(self.setup_class())
        _result = submitOneProduct(_param=json.dumps(_submitOneProduct))

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert 'data' is not None

