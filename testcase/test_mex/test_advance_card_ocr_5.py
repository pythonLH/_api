import json

import pytest

from api_util.mex_util.mex_api import advance_card_ocr
from tool.redconfig import america_parma,america_parma_per


class Test_advance_ocr:
    # 两条测试用例:能识别出来 和 识别不出来的
    @pytest.mark.parametrize('ocr', america_parma['advance_card_ocr'])
    def test_advance_card_ocr(self, ocr):
        """
        advance证件OCR识别
        :param ocr:
        :return:
        """

        _result = advance_card_ocr(_param=json.dumps(ocr))
        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['success'] is True
