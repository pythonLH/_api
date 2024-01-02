import json

import pytest
from api_util.mex_util.mex_api import saveAddressBook
from tool.redconfig import america_parma,america_parma_per


class Test_saveAddressBook:
    @pytest.mark.parametrize('book', america_parma['saveAddressBook'])
    def test_saveAddressBook(self, book):
        """
        保存用户手机通讯录
        :return:
        """
        _result = saveAddressBook(_param=json.dumps(book))
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True
