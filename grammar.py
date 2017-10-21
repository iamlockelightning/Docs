#coding=utf-8

grammar = {}
grammar['S'] = [['NP', 'VP']]
grammar['VP'] = [['B', 'NP'], ['B']]
grammar['NP'] = [['A'], ['A', 'A']]
grammar['A'] = [[u'小花猫'], [u'老鼠'], [u'爪子']] #N->A
grammar['B'] = [[u'抓'], [u'叫']] #V->B

all_sen = []

def www(sen):
	words = sen.split(' ')
	ch = True
	for w in words:
		if w in grammar:
			ch = False
			for item in grammar[w]:
				www(sen.replace(w, ' '.join(item)))
	if ch:
		all_sen.append(sen)

www('S')
all_sen = list(set(all_sen))

print 'len(all_sen):', len(all_sen)
for i in all_sen:
	print i
