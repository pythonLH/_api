from api_url.per_url import __per
from tool.response_log import process_response


def queryFreeProducts(_param):
    """
    查询用户可接产品接口
    hc/app/noAuth/param/queryFreeProducts?pageNo=1&pageSize=30
    POST
    无参数
    响应说明:
            productName -产品名称
            merchantNo -商户编号
            orgNo -机构编号
            prductPayAmountMax -放款金额范围max
            prductPayAmountMin -放款金额范围min
            dayRate -日利率
            productPictureUrl -产品照片
            homeStatus - 按钮状态 0申请(默认)，1再来一笔，2去还款
    :return:
    """

    response = __per.queryFreeProducts(parmas=_param)
    process_response(response)
    return response.json()


def getAppUpdateInfo(_param):
    """
    获取app更新信息
    :param _param:
    :return:
    """
    response = __per.getAppUpdateInfo(parmas=_param)
    process_response(response)
    return response.json()


def getSelectOptionRespDtos(_param):
    """
    获取码表接口,/拼接common_system_code表里的code_item
    :param _param:
    :return:
    """
    response = __per.getSelectOptionRespDtos(parmas=_param)
    process_response(response)
    return response.json()


def getMarketInfo(_param):
    """
    获取贷超用户的相关信息
    :param _param:
    :return:
    """
    response = __per.getMarketInfo(parmas=_param)
    process_response(response)
    return response.json()


def saveMarketInfo(_param):
    """
    保存贷超用户的相关信息
    :param _param:
    :return:
    """
    response = __per.saveMarketInfo(parmas=_param)
    process_response(response)
    return response.json()


def burying_point_platform_report(_param):
    """
    APP埋点数据上传
    :param _param:
    :return:
    """
    response = __per.burying_point_platform_report(parmas=_param)
    process_response(response)
    return response.json()


def hc_app_upload_attach(_param):
    """
    上传附件方法
    :param _param:
    :return:
    """
    response = __per.hc_app_upload_attach(parmas=_param)
    process_response(response)
    return response.json()


def ocr_count_config(_param):
    """
    获取ocr次数配置
    :param _param:
    :return:
    """
    response = __per.ocr_count_config(parmas=_param)
    process_response(response)
    return response.json()


def advance_card_ocr(_param):
    """
    advance证件OCR识别
    :param _param:
    :return:
    """
    response = __per.advance_card_ocr(parmas=_param)
    process_response(response)
    return response.json()


def getAddressList(_param):
    """
    获取省市区的接口
    :param _param:
    :return:
    """
    response = __per.getAddressList(parmas=_param)
    process_response(response)
    return response.json()


def saveAddressBook(_param):
    """
    保存用户手机通讯录
    :param _param:
    :return:
    """
    response = __per.saveAddressBook(parmas=_param)
    process_response(response)
    return response.json()


def market_is_firsttime_loans_in_app(_param):
    """
    贷超-查询app内是否是首贷
    :param _param:
    :return:
    """
    response = __per.market_is_firsttime_loans_in_app(parmas=_param)
    process_response(response)
    return response.json()


def loan_queryAvailableProduct(_param):
    """
    真分期查询最大可借金额
    :param _param:
    :return:
    """
    response = __per.loan_queryAvailableProduct(parmas=_param)
    process_response(response)
    return response.json()


def loan_repayTrialStage(_param):
    """
    还款试算接口
    :param _param:
    :return:
    """
    response = __per.loan_repayTrialStage(parmas=_param)
    process_response(response)
    return response.json()


def getProductUserIsAdjustment(_param):
    """
    贷超-获取用户是否需要调整所选产品
    :param _param:
    :return:
    """
    response = __per.getProductUserIsAdjustment(parmas=_param)
    process_response(response)
    return response.json()


def getProductUserStatus(_param):
    """
    贷超-获取用户在产品中的状态
    :param _param:
    :return:
    """
    response = __per.getProductUserStatus(parmas=_param)
    process_response(response)
    return response.json()


def getRecommendProducts(_param):
    """
    申请单个产品成功后，获取推荐产品页接口,为空跳转单个申请成功提示页，不空跳转推荐页
    :param _param:
    :return:
    """
    response = __per.getRecommendProducts(parmas=_param)
    process_response(response)
    return response.json()


def queryStageAuditLoanLists(_param):
    """
    贷超-查询审核中(真分期分期账单版本)
    :param _param:
    :return:
    """
    response = __per.queryStageAuditLoanLists(parmas=_param)
    process_response(response)
    return response.json()


def queryStageMarketLoanLists(_param):
    """
    贷超-查询我的借款信息(真分期账单版本)
    :param _param:
    :return:
    """
    response = __per.queryStageMarketLoanLists(parmas=_param)
    process_response(response)
    return response.json()


def queryStageRepayLoanLists(_param):
    """
    贷超-查询还款中(真分期账单版本)
    :param _param:
    :return:
    """
    response = __per.queryStageRepayLoanLists(parmas=_param)
    process_response(response)
    return response.json()


def submitOneProduct(_param):
    """
    提交单个盘子借款信息接口
    :param _param:
    :return:
    """
    response = __per.submitOneProduct(parmas=_param)
    process_response(response)
    return response.json()


def submitRecommendProducts(_param):
    """
    推荐产品提交接口
    :param _param:
    :return:
    """
    response = __per.submitRecommendProducts(parmas=_param)
    process_response(response)
    return response.json()


def payment_payin_method_list(_param):
    """
    获取订单的还款方式列表
    :param _param:
    :return:
    """
    response = __per.payment_payin_method_list(parmas=_param)
    process_response(response)
    return response.json()


def app_payment_collection_amount_range(_param):
    """
    代收金额范围
    :param _param:
    :return:
    """
    response = __per.app_payment_collection_amount_range(parmas=_param)
    process_response(response)
    return response.json()


def app_payment_choose_detail_stage(_param):
    """
    获取还款金额选择数据(真分期版本)
    :param _param:
    :return:
    """
    response = __per.app_payment_choose_detail_stage(parmas=_param)
    process_response(response)
    return response.json()


def app_payment_collection_card(_param):
    """
    创建订单代收在线转账
    :param _param:
    :return:
    """
    response = __per.app_payment_collection_card(parmas=_param)
    process_response(response)
    return response.json()


def app_bill_save_repay_entry_slip(_param):
    """
    保存app端还款凭条
    :param _param:
    :return:
    """
    response = __per.app_bill_save_repay_entry_slip(parmas=_param)
    process_response(response)
    return response.json()
