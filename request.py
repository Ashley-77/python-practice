import requests
import re
url='https://www.weather.com.cn/trip/index.shtml'
resp=requests.get(url)
resp.encoding='utf-8'
print(resp.text)
city=re.findall(' title="([\u4e00-\u9fa5]*)" target="_blank">([\u4e00-\u9fa5]*)</a>',resp.text)
print(city)
spot=re.findall('<li data-id="10101020015A">([\u4e00-\u9fa5]*)</li>',resp.text)
print(spot)
#get pic
url='<img src="https://onehall.cau.edu.cn/tp_fp/uploadfiles/uw_service/2019/11/15/1573822675361.png">'
pic=requests.get(url)
with open('logo.png','wb')as file:
    file.write(pic.content)


