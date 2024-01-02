import pytest
import json
import random
import yaml
from tool.logger_ import logger
from api_util.per_util.per_api import getProductUserStatus
from tool.object_path.file_path import america_yaml
from tool.redconfig import america_parma, YamlRed,america_parma_per


class Test_getProductUserStatus:
    @pytest.mark.parametrize('UserStatus', america_parma_per['getProductUserStatus'])
    def test_getProductUserStatus(self, UserStatus):
        _result = getProductUserStatus(_param=json.dumps(UserStatus))

        assert '成功' == _result['msg']
        assert 0 == _result['code']
