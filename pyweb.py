# -*- coding: utf-8 -*-
import re
import urllib.request
import urllib.error

#西安房99地产网
# 长安区  起始地址 --  http://www.fang99.com/buycenter/buildingsearch.aspx?zone=27
# 长安区  终止地址 --  http://www.fang99.com/buycenter/buildingsearch.aspx?zone=27&page=2


# 城西   起始地址 --  http://www.fang99.com/buycenter/buildingsearch.aspx?zone=04
# 城西   终止地址 --  http://www.fang99.com/buycenter/buildingsearch.aspx?zone=04&page=20


#已有楼盘
pat_str_old='<a href="buildingdetail\.aspx\?buildingid=[0-9]*" target="_blank">(\S*)</a><font>(\S*)</font>'

#新获证楼盘
pat_str_new='<a href="buildingdetail\.aspx\?buildingid=[0-9]*" target="_blank">(\S*)</a><span class="xhz">新获证</span><font>(\S*)</font>'

#长安区房99已获证楼盘和价格
url_str="http://www.fang99.com/buycenter/buildingsearch.aspx?zone=27"
web_str=urllib.request.urlopen(url_str).read().decode("gbk")
web_rst=re.compile(pat_str_old).findall(str(web_str))
changanqu_rst_old=web_rst
for x in range(2,3):
    url_str = "http://www.fang99.com/buycenter/buildingsearch.aspx?zone=27"
    url_str+="&page="+str(x)
    web_str = urllib.request.urlopen(url_str).read().decode("gbk")
    web_rst = re.compile(pat_str_old).findall(str(web_str))
    changanqu_rst_old += web_rst

#长安区房99新获证楼盘和价格
url_str="http://www.fang99.com/buycenter/buildingsearch.aspx?zone=27"
web_str=urllib.request.urlopen(url_str).read().decode("gbk")
web_rst=re.compile(pat_str_new).findall(str(web_str))
changanqu_rst_new=web_rst
for x in range(2,3):
    url_str = "http://www.fang99.com/buycenter/buildingsearch.aspx?zone=27"
    url_str+="&page="+str(x)
    web_str = urllib.request.urlopen(url_str).read().decode("gbk")
    web_rst = re.compile(pat_str_new).findall(str(web_str))
    changanqu_rst_new += web_rst

#城西房99已获证楼盘和价格
url_str="http://www.fang99.com/buycenter/buildingsearch.aspx?zone=04"
web_str=urllib.request.urlopen(url_str).read().decode("gbk")
web_rst=re.compile(pat_str_old).findall(str(web_str))
chengxi_rst_old=web_rst
for y in range(2,21):
    url_str = "http://www.fang99.com/buycenter/buildingsearch.aspx?zone=04"
    url_str+="&page="+str(y)
    web_str = urllib.request.urlopen(url_str).read().decode("gbk")
    web_rst = re.compile(pat_str_old).findall(str(web_str))
    chengxi_rst_old += web_rst

#城西房99新获证楼盘和价格
url_str="http://www.fang99.com/buycenter/buildingsearch.aspx?zone=04"
web_str=urllib.request.urlopen(url_str).read().decode("gbk")
web_rst=re.compile(pat_str_new).findall(str(web_str))
chengxi_rst_new=web_rst
for y in range(2,21):
    url_str = "http://www.fang99.com/buycenter/buildingsearch.aspx?zone=04"
    url_str+="&page="+str(y)
    web_str = urllib.request.urlopen(url_str).read().decode("gbk")
    web_rst = re.compile(pat_str_new).findall(str(web_str))
    chengxi_rst_new += web_rst


file=open('D:\script\data.txt','w')
file.write("长安区价格\n")
for i in changanqu_rst_old:
    file.write(i[0]+" "+i[1]+" 已获取预售证\n")
for i in changanqu_rst_new:
    file.write(i[0]+" "+i[1]+" 新获取预售证\n")

file.write("城西价格\n")
for i in chengxi_rst_old:
    file.write(i[0]+" "+i[1]+" 已获取预售证\n")
for i in chengxi_rst_new:
    file.write(i[0]+" "+i[1]+" 新获取预售证\n")
file.close()
