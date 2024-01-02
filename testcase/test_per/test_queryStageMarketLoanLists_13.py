import pytest
import json
import random
import yaml
from tool.logger_ import logger
from api_util.per_util.per_api import queryStageMarketLoanLists
from tool.object_path.file_path import america_yaml
from tool.redconfig import america_parma, YamlRed,america_parma_per
from tool.logger_ import Log


class Test_queryStageAuditLoanLists:
    @pytest.mark.parametrize('loans_list', america_parma_per['LoanLists'])
    def test_queryStageAuditLoanLists(self, loans_list):
        Log().debug(f"测试:{loans_list['_caseTitle']}")

        _result = queryStageMarketLoanLists(_param=json.dumps(loans_list['_caseParam']))

        _actualMsg = _result['msg']
        _actualSuccess = _result['success']

        assert _actualMsg == loans_list['_expectMsg']
        assert _actualSuccess == loans_list['_expectSuccess']
