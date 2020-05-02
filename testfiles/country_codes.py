import pygal.maps.world

def get_country_code(country_name):
    # 返回两个字母的国别码
    for code,name in pygal.maps.world.COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到制定的国家，返回None
    return None

# print(get_country_code('Andorra')) 
# print(get_country_code('United Arab Emirates')) 
# print(get_country_code('Afghanistan'))
