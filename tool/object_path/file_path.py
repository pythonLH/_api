import os

# 参数路径

yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), "yaml_data")

mmp_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),
                                     "tool"),
                        "GeoLite2-City_20231024", "GeoLite2-City.mmdb")

yaml_ = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), "yaml_data",
                     "payload.yaml")
america_yaml = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), "yaml_data",
                            "AmericaPayload.yaml")
america_yaml_per = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),
                                "yaml_data",
                                "AmericaPayloadPer.yaml")

config_ = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'config',
                       'common.ini')
logonController_config = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),
                                      'config',
                                      'logonController.ini')

Header_yaml = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),
                           "yaml_data",
                           "Header.yaml")
if __name__ == '__main__':
    print(mmp_path)
