#coding:utf-8
import urllib
import urllib2
'''
Request请求对象里有data参数，它就是用在post里面的，我们要传递的数据就是这个参数，data是一个字典
post方法
测试有道翻译
Content-Length: 209 #字符数209个
X-Requested-With: XMLHttpRequest  #Ajax异步请求
Content-Type: application/x-www-form-urlencoded; charset=UTF-8 #表示浏览器提交 Web 表单时使用，
表单数据会按照 name1=value1&name2=value2 键值对形式进行编码。
'''

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
# url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
ua_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
form_data={
    "i":" delicious",
    "type":" AUTO",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_CLICKBUTTION",
    "typoResult":"true"
}
data=urllib.urlencode(form_data)#进行url编码处理

request=urllib2.Request(url,headers=ua_header,data=data)
response=urllib2.urlopen(request)
print response.read()