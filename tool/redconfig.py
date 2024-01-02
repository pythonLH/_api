import configparser
import json
import os
import yaml

from tool.logger_ import logger

from tool.object_path.file_path import yaml_, config_, logonController_config, Header_yaml, america_yaml, \
    america_yaml_per


class IniRead:
    # 初始化库
    def __init__(self, filename_, encoding='utf-8'):
        self.filename_ = filename_
        self.encoding_ = encoding
        self.conf_ = configparser.ConfigParser()

        if os.path.exists(filename_):
            try:
                self.red_conf = self.conf_.read(self.filename_, encoding=encoding)
            except Exception as e:
                raise logger.error("加载配置文件出错：%s" % e)
        else:
            pass

    # 写入数据至ini
    def write_ini(self, section, option, value):
        section_list = self.conf_.sections()
        if section not in section_list:
            self.conf_.add_section(section)
            self.conf_.set(section, option, value)
        else:
            self.conf_.set(section, option, value)

        try:
            with open(self.filename_, "w+") as f:
                self.conf_.write(f)
        except FileNotFoundError as e:
            logger.error("写入配置文件错误: %s" % e)
            raise e

    # 读取ini中的str类型数据
    def red_get(self, section, option):
        return self.conf_.get(section, option)

    # 读取ini中的int类型数据
    def red_int(self, section, option):
        return self.conf_.getint(section, option)

    # 读取ini中的布尔值，就是true和false
    def red_boolean(self, section, option):
        return self.conf_.getboolean(section, option)


class YamlRed:
    def __init__(self, filename_, encoding='utf-8'):

        self.filename_ = filename_
        self.encoding_ = encoding

        if os.path.exists(filename_):
            try:
                self.file_ = open(filename_, encoding=encoding)
            except Exception as e:
                raise logger.error("加载yaml文件出错：%s" % e)
        else:
            pass

    def yaml_data(self):
        return yaml.safe_load(self.file_)

    # 写的这个需要的时候在优化
    def taml_write(self, _data):
        return yaml.dump(self.file_, _data)


# 信贷接口参数
red_data = YamlRed(yaml_).yaml_data()
# 信贷请求头参数
header_data = YamlRed(Header_yaml).yaml_data()

# 美洲但接口测试参数
# 墨西哥
america_parma = YamlRed(america_yaml).yaml_data()
# 秘鲁
america_parma_per = YamlRed(america_yaml_per).yaml_data()

# 接口域名存放地,拿的是common.ini里面的credit_host配置
test_mex_host = IniRead(config_).red_get("credit_host_mex", "api_mex_test")
test_per_host = IniRead(config_).red_get("credit_host_per", "api_per_test")
test_phl_host = IniRead(config_).red_get("credit_host_phl", "api_phl_test")

# header开关
country = IniRead(logonController_config).red_get("on-off", "country")
# 国家码手机号,拿的是logonController.ini里面的getRegisterStatus配置
countryCode = IniRead(logonController_config).red_get("getRegisterStatus", "mex_countryCode")
phone = IniRead(logonController_config).red_get("getRegisterStatus", "mex_phone")

# 登录接口参数,拿的是logonController.ini里面的getRegisterStatus配置,手机号默认是为空的,
Login_parameter = eval(IniRead(logonController_config).red_get("getRegisterStatus", "Login_parameter"))

# 注册接口参数,拿的是logonController.ini里面的getRegisterStatus配置,手机号国家码没填
Registration_parameter = eval(IniRead(logonController_config).red_get("getRegisterStatus", "Registration_parameter"))

if __name__ == '__main__':
    # header = YamlRed(Header_yaml).yaml_data()
    # print(json.dumps(header))
    # print(Login_parameter)
    # print(type(Login_parameter))
    print(json.dumps(america_parma['queryAvailableProduct'][0]))
    print(test_per_host)
