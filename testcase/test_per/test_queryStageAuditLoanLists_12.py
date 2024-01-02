import json

import pytest

from api_util.per_util.per_api import queryStageAuditLoanLists
from tool.logger_ import Log
from tool.redconfig import america_parma,america_parma_per


class Test_queryStageAuditLoanLists:
    @pytest.mark.parametrize('loans_list', america_parma_per['LoanLists'])
    def test_queryStageAuditLoanLists(self, loans_list):
        Log().debug(f"测试:{loans_list['_caseTitle']}")

        _result = queryStageAuditLoanLists(_param=json.dumps(loans_list['_caseParam']))

        _actualMsg = _result['msg']
        _actualSuccess = _result['success']

        assert _actualMsg == loans_list['_expectMsg']
        assert _actualSuccess == loans_list['_expectSuccess']


if __name__ == '__main__':
    pytest.main(['s'])
