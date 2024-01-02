import os
import yaml
from tool.logger_ import logger
from tool.redconfig import IniRead, country
from tool.object_path.file_path import Header_yaml, yaml_path, logonController_config


# 因为header中有些数据，是动态得所以得根据不同项目，传入不同得请求头
class creditHeader(object):

    def __init__(self):
        if country == "MEX":
            self.app_name = IniRead(logonController_config).red_get("MexHeader", "appName")
            self.app_version = IniRead(logonController_config).red_get("MexHeader", "appVersion")
            self.lang = IniRead(logonController_config).red_get("MexHeader", "lang")
            self.organizationid = IniRead(logonController_config).red_get("MexHeader", "organizationid")
            self.commercialid = IniRead(logonController_config).red_get("MexHeader", "commercialid")
            self.channel = IniRead(logonController_config).red_get("MexHeader", "channel")
            self.token = ""
            self.Content_Type = IniRead(logonController_config).red_get("MexHeader", "Content_Type")
        elif country == "PER":
            self.app_name = IniRead(logonController_config).red_get("PerHeader", "appName")
            self.app_version = IniRead(logonController_config).red_get("PerHeader", "appVersion")
            self.lang = IniRead(logonController_config).red_get("PerHeader", "lang")
            self.organizationid = IniRead(logonController_config).red_get("PerHeader", "organizationid")
            self.commercialid = IniRead(logonController_config).red_get("PerHeader", "commercialid")
            self.channel = IniRead(logonController_config).red_get("PerHeader", "channel")
            self.token = ""
            self.Content_Type = IniRead(logonController_config).red_get("PerHeader", "Content_Type")

    def returnHeader(self, yamlpath=Header_yaml, encoding="utf-8"):
        """
        将header存入yaml
        :param yamlpath:
        :param encoding:
        :return:
        """
        __Header = {
            "app-version": self.app_version,
            "lang": self.lang,
            "organizationid": self.organizationid,
            "commercialid": self.commercialid,
            "channel": self.channel,
            "app-name": self.app_name,
            "token": self.token,
            "Content-Type": self.Content_Type
        }

        # 存放header的yaml文件,有就写入header,没有就创建yaml写入
        if os.path.exists(yamlpath):
            with open(yamlpath, "w", encoding=encoding) as f:
                if type(__Header) is dict:
                    yaml.dump(__Header, f)

        else:
            with open(os.path.join(yaml_path, "Header.yaml"), "w") as f:
                yaml.safe_dump(__Header, f)

        # 返回一个header,如果项目header不需要更改，就直接用默认得header;
        # 这个header是用来搞 手机号是否注册 进行注册 登录者三个接口的，因为这时候的header是不需要token的
        return __Header


if __name__ == '__main__':
    Header = creditHeader().returnHeader()
    print(Header)
