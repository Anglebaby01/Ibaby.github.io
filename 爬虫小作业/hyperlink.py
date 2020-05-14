import requests
from lxml import etree
def crawler():
    url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    url2 = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/"

    response = requests.get(url=url,headers=headers)
    response.encoding = "GB2312"
    html = etree.HTML(response.text)
    name_result = html.xpath('//a/text()')[:31]
    herf_result = html.xpath("//a/@href")[:31]
    result = {}
    for i in range(len(name_result) ):
        result[name_result[i]] = url2 + herf_result[i]
    print(result)


crawler()