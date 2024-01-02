import pytest
import json
from tool.logger_ import logger
from tool.redconfig import america_parma
from api_util.mex_util.mex_api import ocr_count_config


class Test_ocr_count:
    @pytest.mark.run(order=1)
    def test_ocr_count_config_normal(self):
        """
        获取ocr次数配置-正向用例
        :return:
        """
        _result = ocr_count_config(_param=None)
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True
