import geoip2.database

from tool.object_path.file_path import mmp_path


if __name__ == '__main__':

    ip = '218.89.224.254'


    def ip_get_region(database_path, ip_address):
        """
        获取地址的方法
        ("国家":.country.names['zh-CN']) # names[zh-CN']转换为中文
        ("省份":.subdivisions.most_specific.names["zh-CN'])
        ("城市":.city.names.get["zh-CN'])
        ("经度":.location.longitude,)
        ("纬度":.location.latitude)

        :param database_path:
        :param ip_address:
        :return:
        """
        # 文件用with处理,使用后关闭
        try:
            with geoip2.database.Reader(database_path) as _reader:
                red_city = _reader.city(ip_address)
                # 需要返回多个值,搞部字典接收
                return {
                    'country': red_city.country.names.get('zh-CN', ''),
                    'subdivision': red_city.subdivisions.most_specific.names.get('zh-CN', ''),
                    'city': red_city.city.names.get('zh-CN', '', ),
                    'longitude': red_city.location.longitude,
                    'dimensionality': red_city.location.latitude
                }
        except FileNotFoundError:
            return {'error': '指定的文件不存在'}
        except geoip2.errors.AddressNotFoundError:
            return {'error': '无效的 IP 地址'}


    result = ip_get_region(mmp_path, ip)
    if 'error' in result:
        print(result['error'])
    else:
        print(f"国家: {result['country']}, "
              f"省份: {result['subdivision']}, "
              f"城市: {result['city']}, "
              f"经度: {result['longitude']}, "
              f"纬度: {result['dimensionality']}")
