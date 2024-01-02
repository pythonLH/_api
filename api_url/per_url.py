from tool.object_path.file_path import Header_yaml
from tool.redconfig import YamlRed
from tool.registerlogin import registlogin
from tool.request_ import RrestClient


class per_url(RrestClient):
    def __init__(self):
        super(per_url, self).__init__()
        # 初始化一个登录之后的header
        registlogin().getPhone()
        self.header = YamlRed(Header_yaml).yaml_data()

    # 获取首页产品列表
    def queryFreeProducts(self, parmas):
        return self.post(url_="/hc/app/noAuth/param/queryFreeProducts?pageNo=1&pageSize=50", api_header=self.header,
                         data=parmas)

    # 获取app更新信息
    def getAppUpdateInfo(self, parmas):
        return self.get(url_="/hc/app/noAuth/param/getAppUpdateInfo/{packageName}/{versionNum}", api_header=self.header,
                        data=parmas)

    # 获取码表接口,/拼接common_system_code表里的code_item
    def getSelectOptionRespDtos(self, parmas):
        return self.get(url_=f"/hc/app/noAuth/param/getSelectOptionRespDtos/{parmas}", api_header=self.header,
                        data=None)

    # 获取贷超用户的相关信息
    def getMarketInfo(self, parmas):
        return self.get(url_="/hc/app/marketInfo/getMarketInfo", api_header=self.header, data=parmas)

    # 保存贷超用户的相关信息
    def saveMarketInfo(self, parmas):
        return self.post(url_="/hc/app/marketInfo/saveMarketInfo", api_header=self.header, data=parmas)

    # APP埋点数据上传
    def burying_point_platform_report(self, parmas):
        return self.post(url_="/hc/app/payment/collection/card", api_header=self.header, data=parmas)

    # 上传附件方法
    def hc_app_upload_attach(self, parmas):
        return self.post(url_="/hc/app/upload/attach", api_header=self.header, data=parmas)

    # 获取ocr次数配置
    def ocr_count_config(self, parmas):
        return self.get(url_="/hc/app/noAuth/market/ocr/count/config", api_header=self.header, data=parmas)

    # advance证件OCR识别--有可能墨西哥秘鲁用得接口不一样,先标记
    # 墨西哥的ocr识别接口/hc/app/thirdparty/advance/card/ocr
    # 秘鲁的ocr识别接口hc/app/thirdparty/per/card/ocr
    def advance_card_ocr(self, parmas):
        return self.post(url_=f"/hc/app/thirdparty/per/card/ocr", api_header=self.header, data=parmas)

    # 获取省市区的接口
    def getAddressList(self, parmas):
        return self.get(url_=f"/hc/app/noAuth/param/getAddressList/{parmas}", api_header=self.header, data=parmas)

    # 保存用户手机通讯录
    def saveAddressBook(self, parmas):
        return self.post(url_="/hc/app/userInfo/saveAddressBook", api_header=self.header, data=parmas)

    # 贷超-查询app内是否是首贷
    def market_is_firsttime_loans_in_app(self, parmas):
        return self.get(url_="/hc/app/market/is/firsttime/loans/in/app", api_header=self.header, data=parmas)

    def usercorrtoken(self):
        pass

    def getRepaymentAccount(self):
        pass

    def queryBills(self):
        pass

    def queryStageBillDetail(self):
        pass

    def slip(self):
        pass

    def getRegConfig(self):
        pass

    def getInsertCalConf(self):
        pass

    def __getInsertCalConf(self):
        pass

    def saveCol(self):
        pass

    def saveColEvent(self):
        pass

    def saveComRecords(self):
        pass

    def saveSms(self):
        pass

    def saveSmsFull(self):
        pass

    def records(self):
        pass

    def uploadPhoto(self):
        pass

    def appinnerappuserinfo(self):
        pass

    def rawDataPush(self):
        pass

    def sendRepayOrOverDueEvent(self):
        pass

    def statistics(self):
        pass

    def customersmslist(self):
        pass

    def smsCleanPhoneFix(self):
        pass

    def existPhonesNum(self):
        pass

    def findDistinctPhoneNumByUUidOriginal(self):
        pass

    def findUserNoByCustomerNo(self):
        pass

    def getAddressBookListByUserNo(self):
        pass

    def getAddressBookOriginListByUserNo(self):
        pass

    def getMediaByUUIDAndCustomerSource(self):
        pass

    def getPhonesByAndoridId(self):
        pass

    def getRegisterUserList(self):
        pass

    def getRegisterUserListByMac(self):
        pass

    def getUserNoApplyOrder(self):
        pass

    def getUserRegisterInfo(self):
        pass

    def queryAndroidIdsByPhone(self):
        pass

    def pushTransMoneyEventToAf(self):
        pass

    def queryBlackMacByMac(self):
        pass

    def queryDynamicUserCount(self):
        pass

    def queryDynamicUserQuantity(self):
        pass

    def queryMatchAppUserNum(self):
        pass

    def queryUserListByAndroidId(self):
        pass

    def queryUserListByImsi(self):
        pass

    def smseventrangecount(self):
        pass

    def unzlib(self):
        pass

    def updateCustomerName(self):
        pass

    def updateUserPaymentInfo(self):
        pass

    def loanadvancelivenessswitch(self):
        pass

    def loan_bank_enable_query(self):
        pass

    def loan_borrow_money(self):
        pass

    def loan_borrow_money_contract_data(self):
        pass

    def loan_borrow_money_contract_preview(self):
        pass

    def loan_borrow_money_judge(self):
        pass

    def loan_borrow_money_update(self):
        pass

    def loan_card_info_config(self):
        pass

    def loan_is_firsttime_loans(self):
        pass

    def loan_lastSelletParameter(self):
        pass

    def loan_order_reject(self):
        pass

    def loan_order_reject_list(self):
        pass

    def loan_promocode_switch(self):
        pass

    def loan_promocode_verify(self):
        pass

    # 真分期查询最大可借金额
    def loan_queryAvailableProduct(self, parmas):
        return self.post(url_="/hc/app/loan/queryAvailableProduct", api_header=self.header, data=parmas)

    def loan_queryRepayPlan(self, parmas):
        return self.post(url_="/hc/app/loan/queryAvailableProduct", api_header=self.header, data=parmas)

    # 还款试算接口
    def loan_repayTrialStage(self, parmas):
        return self.post(url_="/hc/app/loan/repayTrialStage", api_header=self.header, data=parmas)

    def addProductPageHits(self):
        pass

    def advance_liveness_switch(self):
        pass

    def getSuperMarketAppHomepageBannerImagerConfig(self):
        pass

    def card_info_config(self):
        pass

    # 贷超-获取用户是否需要调整所选产品
    def getProductUserIsAdjustment(self, parmas):
        return self.post(url_="/hc/app/market/getProductUserIsAdjustment", api_header=self.header, data=parmas)

    # 贷超-获取用户在产品中的状态
    def getProductUserStatus(self, parmas):
        return self.post(url_="/hc/app/market/getProductUserStatus", api_header=self.header, data=parmas)

    # 申请单个产品成功后，获取推荐产品页接口,为空跳转单个申请成功提示页，不空跳转推荐页
    def getRecommendProducts(self, parmas):
        return self.post(url_="/hc/app/market/getRecommendProducts", api_header=self.header, data=parmas)

    def is_firsttime_loans_in_app(self):
        pass

    def loan_info(self):
        pass

    def payment_cancel(self):
        pass

    def payment_detail(self):
        pass

    def queryAuditLoanLists(self):
        pass

    def queryAuditLoanListsV2(self):
        pass

    def queryMarketLoanLists(self):
        pass

    def queryMarketLoanListsV2(self):
        pass

    def queryRepayLoanLists(self):
        pass

    def queryRepayLoanListsV2(self):
        pass

    # 贷超-查询审核中(真分期分期账单版本)
    def queryStageAuditLoanLists(self, parmas):
        return self.post(url_="/hc/app/market/queryStageAuditLoanLists", api_header=self.header, data=parmas)

    # 贷超-查询我的借款信息(真分期账单版本)
    def queryStageMarketLoanLists(self, parmas):
        return self.post(url_="/hc/app/market/queryStageMarketLoanLists", api_header=self.header, data=parmas)

    # 贷超-查询还款中(真分期账单版本)
    def queryStageRepayLoanLists(self, parmas):
        return self.post(url_="/hc/app/market/queryStageRepayLoanLists", api_header=self.header, data=parmas)

    # 提交单个盘子借款信息接口
    def submitOneProduct(self, parmas):
        return self.post(url_="/hc/app/market/submitOneProduct", api_header=self.header, data=parmas)

    # 推荐产品提交接口
    def submitRecommendProducts(self, parmas):
        return self.post(url_="/hc/app/market/submitRecommendProducts", api_header=self.header, data=parmas)

    # 获取订单的还款方式列表
    def payment_payin_method_list(self, parmas):
        return self.get(url_="/hc/app/payment/payin/method/list", api_header=self.header, data=parmas)

    # 代收金额范围
    def app_payment_collection_amount_range(self, parmas):
        return self.post(url_="/hc/app/payment/collection/amount/range", api_header=self.header, data=parmas)

    # 获取还款金额选择数据(真分期版本)
    def app_payment_choose_detail_stage(self, parmas):
        return self.get(url_="/hc/app/payment/choose/detail/stage/{orderNo}", api_header=self.header, data=parmas)

    # 创建订单代收在线转账
    def app_payment_collection_card(self, parmas):
        return self.post(url_="/hc/app/payment/collection/card", api_header=self.header, data=parmas)

    # 保存app端还款凭条
    def app_bill_save_repay_entry_slip(self, parmas):
        return self.post(url_="/hc/app/bill/save/repay/entry/slip", api_header=self.header, data=parmas)


# 实例化
__per = per_url()
