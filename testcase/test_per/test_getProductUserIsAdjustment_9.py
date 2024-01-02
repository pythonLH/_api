import pytest
import json
import random
import yaml
from tool.logger_ import logger
from api_util.per_util.per_api import getProductUserIsAdjustment
from tool.object_path.file_path import america_yaml
from tool.redconfig import america_parma, YamlRed,america_parma_per


class Test_getProductUserIsAdjustment:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('Adjustment', america_parma_per['getProductUserIsAdjustment'])
    def test_getProductUserIsAdjustment(self, Adjustment):
        _result = getProductUserIsAdjustment(_param=json.dumps(Adjustment))
        assert '成功' == _result['msg']
        assert 0 == _result['code']

    def test_getProductUserIsAdjustment_2(self):
        pass

