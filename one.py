#-*-coding:utf-8-*-

import urllib,urllib2,random
import re,jieba

# target = open('sw1','a')
# for x in slist:
# 	if len(x)>3:
# 		target.write(x)
# 		target.write('\n')
# target.close()


# target = open('python/stopwords','a')
# for x in slist:
# 	target.write(x)
# 	target.write('\n')
# target.close()

text = open('sw1').read()
slist = text.split('\n')

segs = jieba.cut('全球最具影响力的大学排行榜之一')
final = ''
for seg in segs:
	if seg.encode('utf-8') not in slist:
		# print seg
		final += seg
	else:
		print seg
print final





# seg_list = jieba.cut("鹿晗愿望季空降上海欢乐谷，在魅幻的灯光下许下你的愿望吧", cut_all=True)
# print "Full Mode:", "/ ".join(seg_list)  # 全模式
# seg_list = jieba.cut("鹿晗愿望季空降上海欢乐谷，在魅幻的灯光下许下你的愿望吧", cut_all=False)
# print "Default Mode:", "/ ".join(seg_list)  # 精确模式
# seg_list = jieba.cut("鹿晗，胡歌，刘诗诗，angelbaby…这么多明星里，论吃饭我就服欧弟！")  # 默认是精确模式
# print ", ".join(seg_list)
# seg_list = jieba.cut_for_search("鹿晗会给喜欢的粉丝签名时画特别多的爱心？是时候看看你的签名照了！")  # 搜索引擎模式
# print ", ".join(seg_list)


