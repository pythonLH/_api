import pytest
import json
import random
import yaml
from tool.logger_ import logger
from api_util.per_util.per_api import getRecommendProducts
from tool.object_path.file_path import america_yaml
from tool.redconfig import america_parma, YamlRed,america_parma_per


# class Test_getRecommendProducts:
#     @pytest.mark.parametrize('commendProducts', america_parma_per['getRecommendProducts'])
#     def test_getRecommendProducts(self, commendProducts):
#         _result = getRecommendProducts(_param=json.dumps(commendProducts))
#
#         assert '成功' == _result['msg']
#         assert 0 == _result['code']

