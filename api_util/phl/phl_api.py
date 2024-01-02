from api_url.phl_url import phl_api
from tool.response_log import process_response


def saveDeviceInfo(params):
    """
    # 储存注册时的设备信息
    :param params:
    :return:
    """
    response = phl_api.saveDeviceInfo(parmas=params)
    process_response(response)
    return response.json()


def saveAddressBook(parmas):
    """
    # 上传通讯录
    :return:
    """
    response = phl_api.saveAddressBook(parmas=parmas)
    process_response(response)
    return response.json()


def queryAvailableProduct(parmas):
    """
    # 查询最大可借天数
    :return:
    """
    response = phl_api.queryAvailableProduct(parmas=parmas)
    process_response(response)
    return response.json()


def submitOneProduct(parmas):
    """
    # 提交进件
    :return:
    """
    response = phl_api.submitOneProduct(parmas=parmas)
    process_response(response)
    return response.json()
