import json

import yaml

from tool.headerfunction import creditHeader
from tool.logger_ import logger
from tool.object_path.file_path import Header_yaml
from tool.redconfig import countryCode, phone, Login_parameter, Registration_parameter
from tool.request_ import RrestClient


# 写个方法查询是否注册,注册登录后,将token写入Header.yaml
class registlogin(RrestClient):

    def __init__(self):
        super(registlogin, self).__init__()
        self.header = creditHeader().returnHeader()
        # 接口地址，不是可变的，直接写死;国家码电话号码，配置化
        self.reg_url = f"/hc/app/noAuth/logon/getRegisterStatus/{countryCode}/{phone}"
        self.doRegister_url = "/hc/app/noAuth/logon/doRegister"
        self.login_url = "/hc/app/noAuth/logon/login"

    def getPhone(self):
        """
        用来验证测试账号,是否注册
        已注册就进行登录,更新header便于后续接口使用
        未注册就注册登录,更新header
        :return:
        """
        data = {}
        reg = self.get(self.reg_url, self.header, data).json()
        logger.info(f"调用-信贷判断手机号是否注册接口：{reg}")

        # 已注册,就登录并更新Header.yaml中的header参数
        if reg["data"]:
            Login_parameter["phone"] = phone
            result = self.post(self.login_url, self.header, json.dumps(Login_parameter)).json()
            logger.info(f"调用-信贷登录接口：{result}")
            if result["success"] and result["data"] is not None:
                with open(Header_yaml, "w", encoding="utf-8") as header_file:
                    new_header = self.header
                    for value in result['data'].values():
                        new_header['token'] = value
                    yaml.dump(new_header, header_file)
        # 没注册，就注册登录并更新Header.yaml中的header参数
        else:
            Registration_parameter["countryCode"] = countryCode
            Registration_parameter["phone"] = phone
            if self.post(self.doRegister_url, self.header, json.dumps(Registration_parameter)).json()["success"]:
                Login_parameter["phone"] = phone
                result = self.post(self.login_url, self.header, json.dumps(Login_parameter)).json()
                logger.info(f"调用-信贷登录接口：{result}")
                if result["success"] and result["data"] is not None:
                    with open(Header_yaml, "w", encoding="utf-8") as header_file:
                        new_header = self.header
                        for value in result['data'].values():
                            new_header['token'] = value
                        yaml.dump(new_header, header_file)
            else:
                logger.info(f"调用-信贷注册接口报错")


if __name__ == '__main__':
    registlogin().getPhone()
