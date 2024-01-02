import json

import pytest
from tool.redconfig import red_data
from api_util.phl.phl_api import saveDeviceInfo, \
    saveAddressBook, \
    queryAvailableProduct, \
    submitOneProduct


def test_saveDeviceInfo():
    result = saveDeviceInfo(json.dumps(red_data["saveDeviceInfo"]))
    # 断言
    assert result['code'] == 0
    assert result['msg'] == "成功"
    assert result['success'] is True


def test_saveAddressBook():
    result = saveAddressBook(json.dumps(red_data["saveAddressBook"]))
    # 断言
    assert result['code'] == 0
    assert result['msg'] == "成功"
    assert result['success'] is True


def test_queryAvailableProduct():
    result = queryAvailableProduct(json.dumps(red_data["queryAvailableProduct"]))
    # 断言
    assert result['code'] == 0
    assert result['msg'] == "成功"
    assert result['success'] is True


def test_submitOneProduct():
    result = submitOneProduct(json.dumps(red_data["submitOneProduct"]))
    # 断言
    assert result['code'] == 0
    assert result['msg'] == "成功"
    assert result['success'] is True


if __name__ == '__main__':
    pytest.main(['-vs'])
