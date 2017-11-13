import io, json
import glob
import math
import os
from pprint import pprint

with io.open('twn_in_jp.json', encoding='utf-8') as data_file:    
    infos = json.load(data_file)

with io.open('name_dict.json', encoding='utf-8') as data_file:    
    dict = json.load(data_file)
    
#pprint(infos)
#pprint(dict)

max = 0
total = 0
for info in infos['data']:
    total = total + info['number']
    if info['number'] > max:
        max = info['number']

#print max
#print total
        
result = []
for info in infos['data']:
    print info
    percent = info['number'] / float(total) * 100.0
     
    num = 255.0 * info['number'] / float(max)
    num = math.log(num, 255) * 255.0    #use log to add more contrast
    
    if num < 0:
        num = 0
    
    num = 255 - num
    color = '%0*X' % (2,num)
    
    display = 'Number: %d, Percentage: %.2f%%' % (info['number'], percent)
    
    #print percent
    #print color
    for area in dict:
        if info['name'] == area['shortname']:
            result.append({'code':area['code'], 'name':display, 'color':'#FF'+color+color, 'hoverColor':'#000000', 'prefectures':[area['code']]})

str = json.dumps(result, ensure_ascii=False)
str = "var areas = '" + str + "';"
#print str
                
with io.open('result.js', 'w', encoding='utf-8') as jsFile:
    jsFile.write(unicode(str))