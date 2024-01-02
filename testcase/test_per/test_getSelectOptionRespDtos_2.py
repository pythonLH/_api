import pytest
from api_util.per_util.per_api import getSelectOptionRespDtos


class Test_qetSelectOptionRespDtos:
    @pytest.mark.parametrize("gender", [{"_param": "IN_SEX_TYPE"}, {"_param": "IN_SEX_OCR_TYPE"}])
    @pytest.mark.run(order=1)
    def test_getSelectOptionRespDtos_gender(self, gender):
        """
        获取码表(性别)-接口参数IN_SEX_TYPE
        :return:
        """
        _result = getSelectOptionRespDtos(_param=gender["_param"])

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    @pytest.mark.run(order=10)
    def test_getSelectOptionRespDtos_Married(self):
        """
        获取码表(婚姻状况)-接口参数IN_MARITAL_STATUS_TYPE
        :return:
        """
        _result = getSelectOptionRespDtos(_param="IN_MARITAL_STATUS_TYPE")

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    @pytest.mark.run(order=11)
    def test_getSelectOptionRespDtos_Education(self):
        """
        获取码表(教育经历)-接口参数IN_HIGH_EDUCATION
        :return:
        """
        _result = getSelectOptionRespDtos(_param="IN_HIGH_EDUCATION")

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    @pytest.mark.run(order=2)
    def test_getSelectOptionRespDtos_contact(self):
        """
        获取码表(紧急联系人)-接口参数IN_EMERGENCY_CONTACT_RELATION_TYPE
        :return:
        """
        _result = getSelectOptionRespDtos(_param="IN_EMERGENCY_CONTACT_RELATION_TYPE")

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    @pytest.mark.run(order=3)
    def test_getSelectOptionRespDtos_payone(self):
        """
        获取码表(发薪频率)-接口参数IN_SALARY_TYPE
        :return:
        """
        _result = getSelectOptionRespDtos(_param="IN_SALARY_TYPE")

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    @pytest.mark.run(order=4)
    def test_getSelectOptionRespDtos_paytwo(self):
        """
        获取码表(周薪)-接口参数IN_WEEK_SALARY_TYPE
        :return:
        """
        _result = getSelectOptionRespDtos(_param="IN_WEEK_SALARY_TYPE")

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    @pytest.mark.parametrize("job", ["IN_WORK_INCOME_TYPE",
                                     "IN_CHILD_COUNT_TYPE", "IN_WORKING_HOURS_TYPE"])
    @pytest.mark.run(order=5)
    def test_getSelectOptionRespDtos_work(self, job):
        """
        获取码表(工作信息)-接口参数IN_WORK_INCOME_TYPE/IN_CHILD_COUNT_TYPE/IN_WORKING_HOURS_TYPE
        :return:
        """
        _result = getSelectOptionRespDtos(_param=job)

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    @pytest.mark.run(order=6)
    def test_getSelectOptionRespDtos_income(self):
        """
        获取码表(收入来源)-接口参数IN_SOURCE_INCOME
        :return:
        """
        _result = getSelectOptionRespDtos(_param="IN_SOURCE_INCOME")

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    @pytest.mark.run(order=7)
    def test_getSelectOptionRespDtos_post(self):
        """
        获取码表(工作类型)-接口参数IN_WORK_POST_TYPE
        :return:
        """
        _result = getSelectOptionRespDtos(_param="IN_WORK_POST_TYPE")

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    @pytest.mark.run(order=8)
    @pytest.mark.parametrize("bank", ["IN_BANK_ACCOUNT_TYPE", "IN_BANK_NAME_TYPE"])
    def test_getSelectOptionRespDtos_bank(self, bank):
        """
        获取码表(银行账户类型/可用银行)-IN_BANK_ACCOUNT_TYPE/IN_BANK_NAME_TYPE
        :return:
        """
        _result = getSelectOptionRespDtos(_param=bank)

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True

    # 涉及到不同包名得，还是药把参数放到yaml去,免得获取别的包正则还要代码里改参数
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize("package", ["com.ahorrar.dinero.chancheuklung",
                                         "com.mexico.loan.open.purse",
                                         "com.dinero.urgente.mexican"])
    def test_getSelectOptionRespDtos_v3(self, package):
        """
        获取码表(输入框正则)-APP_VALIDATE_RULES_V3/包名
        :return:
        """
        _result = getSelectOptionRespDtos(_param=f"APP_VALIDATE_RULES_V3/{package}")

        assert '成功' == _result['msg']
        assert 0 == _result['code']
        assert _result['data'] is not None
        assert _result['success'] is True
