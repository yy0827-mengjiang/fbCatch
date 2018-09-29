import requests
import re
import time
res = requests.get('http://live.500.com/zqdc.php')
res.encoding = 'gbk'
mainText = res.text
# print(mainText)
idAndName = {}
detailUrl =  'http://odds.500.com/fenxi/shuju-num.shtml'
idNum = re.findall(r'id="a(.\d+?)" status="0" gy="',mainText)
for n in idNum:
    resDetail = requests.get(detailUrl.replace('num',n))
    resDetail.encoding = 'gbk'
    teamName = re.search(r'id="a'+n+'" status="0" gy="(.+?)"',mainText).group(1)
    # print(resDetail.text)
    zj = re.findall(r'<td valign="bottom" height="65">最近</td>(.+?)<td valign="bottom">最远</td>',resDetail.text,re.S)
    # print(teamName)
    idAndName['name'] = teamName
    isIn = False
    for z in zj:
        zjsf = ''
        sf = re.findall(r'<img src="/images/(.*).png" alt="(.+?)" />',z)
        for s in sf:
            zjsf = zjsf+s[1].__str__()
        if '平平平平' in zjsf:
            isIn = True
            idAndName['zjsf'] = zjsf
    if isIn:
        print(idAndName)
    time.sleep(2) #暂停2秒
print('结束')
