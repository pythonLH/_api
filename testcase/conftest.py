import pytest
from tool.logger_ import logger
from tool.redconfig import america_parma
import json
import random
import yaml
from tool.logger_ import logger
from api_util.mex_util.mex_api import loan_queryAvailableProduct, loan_repayTrialStage
from tool.object_path.file_path import america_yaml
from tool.redconfig import america_parma, YamlRed


# 接口测试的function全都会自动调用这个fixture前后置
@pytest.fixture(scope="function", autouse=True)
def function_fixture_2():
    logger.info("-----------------------分割线-----------------------")
    yield
    logger.info("-----------------------分割线-----------------------\n")


@pytest.mark.parametrize('product', america_parma['queryAvailableProduct'])
@pytest.fixture(scope='class', autouse=False)
def queryAvailableProduct(product):
    _result = loan_queryAvailableProduct(_param=product)
    return _result
