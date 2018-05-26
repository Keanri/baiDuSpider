import requests

def getBaiduMsg(keyword,page):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    }
    #源代码
    res = requests.get('https://www.baidu.com/s?wd={}'.format(keyword,page),headers = headers).text

    return res.replace("//www.baidu.com/img/baidu_jgylogo3.gif", 'static/images/logo.jpg').replace('百度一下','搜索').replace('百度搜索','搜索')






if __name__=='__mian__':
    getBaiduMsg("python")