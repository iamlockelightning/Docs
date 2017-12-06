#coding=utf-8
import os
import chardet
import math

def read_data(data_path):
	file_dirs =  os.listdir(data_path)
	sentences_splitor = [u'。'.encode('GB2312'), u'！'.encode('GB2312'), u'？'.encode('GB2312'), u'，'.encode('GB2312'), u'”'.encode('GB2312'), u'“'.encode('GB2312'), u'（'.encode('GB2312'), u'）'.encode('GB2312'), u'、'.encode('GB2312'), u'：'.encode('GB2312')]
	word_freq_dict = {}
	pair_freq_dict = {}
	sentences = []
	sen = []
	for filename in file_dirs:
		with open(data_path + filename, 'r') as fr:
			# print filename
			words = fr.read().replace('\n', '').split('  ')
			for w in words:
				w = w.strip()
				if w == "":
					continue
				# print w.decode('GB2312')
				w = w[0 : w.index('/')]
				if w[0]=='['.encode('GB2312'):
					w = w[1 : ]
				if w in sentences_splitor:
					if len(sen) >= 2:
						for i in range(len(sen)-1):
							if sen[i] not in pair_freq_dict:
								pair_freq_dict[sen[i]] = {}
							if sen[i+1] not in pair_freq_dict[sen[i]]:
								pair_freq_dict[sen[i]][sen[i+1]] = 0
							pair_freq_dict[sen[i]][sen[i+1]] += 1
						sentences.append(sen)
						# if len(sentences)==57350:
							# print " ".join(sen).decode('GB2312')
					elif len(sen) == 1:
						sentences.append(sen)
					sen = []
					continue
				else:
					sen.append(w)
					if w not in word_freq_dict:
						word_freq_dict[w] = {"value": 0, "show": set()}
						word_freq_dict[w]["value"] = 1
						word_freq_dict[w]["show"].add(len(sentences))
					else:
						word_freq_dict[w]["value"] += 1
						word_freq_dict[w]["show"].add(len(sentences))
	return word_freq_dict, pair_freq_dict, sentences

def frequency(word_freq_dict, pair_freq_dict):
	pairs = {}
	for i in pair_freq_dict:
		for j in pair_freq_dict[i]:
			pairs['('+i+','+j+')'] = pair_freq_dict[i][j]
	sorted_pairs = sorted(pairs.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
	for i in range(10):
		print sorted_pairs[i][0].decode('GB2312'), '\t', sorted_pairs[i][1]

def mean_and_variance(word_freq_dict, pair_freq_dict, sentences):
	pairs = {}
	ii = 0
	for i in word_freq_dict:
		for j in word_freq_dict:
			if i == j:
				continue
			ii += 1
			if ii % 1000000 == 0:
				# print ii
				break
			inter_set = word_freq_dict[i]["show"] & word_freq_dict[j]["show"]
			# print i.decode('GB2312'), j.decode('GB2312')
			# print inter_set
			if len(inter_set) == 0:
				continue
			pairs['('+i+','+j+')'] = {"s": 0.0, "d": 0.0}
			array = []
			for n in inter_set:
				# print " ".join(sentences[n]).decode('GB2312')
				# print sentences[n].index(j)
				# print sentences[n].index(i)
				array.append(sentences[n].index(j)-sentences[n].index(i)-1)
			pairs['('+i+','+j+')']["s"] = 1.0* sum(array) / len(array)
			if len(array) > 1:
				pairs['('+i+','+j+')']["d"] = math.sqrt(1.0* sum([(xi - pairs['('+i+','+j+')']["s"])**2 for xi in array]) / (len(array)-1))
			else:
				pairs['('+i+','+j+')']["d"] = 0.0
		if ii % 100000 == 0:
				break
	sorted_pairs = sorted(pairs.items(), lambda x, y: cmp(x[1]["s"], y[1]["s"]))
	# for i in range(10):
		# print sorted_pairs[i][0].decode('GB2312'), '\t', sorted_pairs[i][1]["s"], '\t', sorted_pairs[i][1]["d"]
	num = 5
	for item in sorted_pairs:
		if item[1]["d"] >= 0.0 and item[1]["d"] < 1.0:
			print item[0].decode('GB2312'), '\t', item[1]["s"], '\t', item[1]["d"]
			num -= 1
			if num == 0:
				break
	print '--------------'
	num = 5
	for item in sorted_pairs:
		if item[1]["d"] >= 1.0 and item[1]["d"] < 2.0:
			print item[0].decode('GB2312'), '\t', item[1]["s"], '\t', item[1]["d"]
			num -= 1
			if num == 0:
				break
	print '--------------'
	num = 5
	for item in sorted_pairs:
		if item[1]["d"] >= 2.0 and item[1]["d"] < 3.0:
			print item[0].decode('GB2312'), '\t', item[1]["s"], '\t', item[1]["d"]
			num -= 1
			if num == 0:
				break

def hypothesis_testing(word_freq_dict, pair_freq_dict):
	bigram_num = 0
	for i in pair_freq_dict:
		for j in pair_freq_dict[i]:
			bigram_num += pair_freq_dict[i][j]
	pairs = {}
	for i in pair_freq_dict:
		for j in pair_freq_dict[i]:
			pairs['('+i+','+j+')'] = (1.0*pair_freq_dict[i][j]/bigram_num - 1.0*word_freq_dict[i]["value"]*word_freq_dict[j]["value"]/(len(word_freq_dict)*len(word_freq_dict))) / math.sqrt(1.0*pair_freq_dict[i][j]/bigram_num/bigram_num)
	sorted_pairs = sorted(pairs.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
	for i in range(10):
		print sorted_pairs[i][0].decode('GB2312'), '\t', sorted_pairs[i][1]

def pointwise(word_freq_dict, pair_freq_dict):
	pairs = {}
	for i in pair_freq_dict:
		for j in pair_freq_dict[i]:
			pairs['('+i+','+j+')'] = math.log(1.0*pair_freq_dict[i][j]/word_freq_dict[i]["value"])
	sorted_pairs = sorted(pairs.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
	for i in range(10):
		print sorted_pairs[i][0].decode('GB2312'), '\t', sorted_pairs[i][1]


if __name__=="__main__":
	data_path = u"/Users/locke/Desktop/2017-2018秋季学期/计算语言学(0)/熟语料/"
	word_freq_dict, pair_freq_dict, sentences = read_data(data_path)
	print "len(word_freq_dict):", len(word_freq_dict)

	frequency(word_freq_dict, pair_freq_dict)
	# mean_and_variance(word_freq_dict, pair_freq_dict, sentences)
	# hypothesis_testing(word_freq_dict, pair_freq_dict)
	# pointwise(word_freq_dict, pair_freq_dict)
