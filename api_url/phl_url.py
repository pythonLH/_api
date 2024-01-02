from tool.object_path.file_path import Header_yaml
from tool.redconfig import YamlRed
from tool.registerlogin import registlogin
from tool.request_ import RrestClient


class phlurl(RrestClient):
    def __init__(self):
        super(phlurl, self).__init__()
        # 初始化一个登录之后的header
        registlogin().getPhone()
        self.header = YamlRed(Header_yaml).yaml_data()

    # 储存注册时的设备信息
    def saveDeviceInfo(self, parmas):
        return self.post(url_="/hc/app/userInfo/saveDeviceInfo", api_header=self.header, data=parmas)

    # 上传通讯录
    def saveAddressBook(self, parmas):
        return self.post(url_="/hc/app/userInfo/saveAddressBook", api_header=self.header, data=parmas)

    # 查询最大可借天数
    def queryAvailableProduct(self, parmas):
        return self.post(url_="/hc/app/loan/queryAvailableProduct", api_header=self.header, data=parmas)

    # 提交进件
    def submitOneProduct(self, parmas):
        return self.post(url_="/hc/app/market/submitOneProduct", api_header=self.header, data=parmas)


phl_api = phlurl()
