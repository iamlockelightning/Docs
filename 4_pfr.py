#coding=utf-8
import os
import chardet
import math


def read_data(data_path, path_list=[]):
	sentences_splitor = [u'。'.encode('GB2312'), u'！'.encode('GB2312'), u'？'.encode('GB2312')]
	word_freq_dict = {}
	word_freq_dict['<BOS>'] = 0
	word_freq_dict['<EOS>'] = 0
	sentences = []
	sen = []
	for sub_path in path_list:
		file_dirs = os.listdir(data_path+sub_path)
		for filename in file_dirs:
			with open(data_path + sub_path + filename, 'r') as fr:
				# print filename
				for line in fr:
					words = line.strip().split('  ')
					for w in words:
						w = w[0 : w.index('/')]
						if w[0]=='['.encode('GB2312'):
							w = w[1 : ]
						if w not in word_freq_dict:
							word_freq_dict[w] = 1
						else:
							word_freq_dict[w] += 1

						if w in sentences_splitor:
							sentences.append('<BOS> ' + ' '.join(sen) + ' <EOS>')
							word_freq_dict['<BOS>'] += 1
							word_freq_dict['<EOS>'] += 1
							sen = []
						else:
							sen.append(w)
	N = 0
	for k in word_freq_dict:
		N += word_freq_dict[k]
	return word_freq_dict, sentences, N


def problem_1():
	data_path = u"/Users/locke/Desktop/2017-2018秋季学期/计算语言学(0)/4_第四章作业续/"
	path_list = [u"train/", u"valid/", u"test/"]
	word_freq_dict, sentences, N = read_data(data_path, path_list)
	print 'total sentences num:', len(sentences)
	B = len(word_freq_dict)

	def bigram_prob_adding_lambda(sentence, _lambda, fw):
		win_len = 2
		words = sentence.split(' ')
		for w in words:
			if w not in word_freq_dict:
				word_freq_dict[w] = 0
		gram_probs = []
		sen_prob = 1.0
		for i in range(len(words)+1-win_len):
			cnt = 0
			tar = ' '.join(words[i:i+win_len])
			for sen in sentences:
				if tar in sen:
					cnt += 1
			gram_probs.append((1.0*cnt + _lambda)/(word_freq_dict[words[i]] + _lambda * B))
			sen_prob *= (1.0*cnt + _lambda)/(word_freq_dict[words[i]] + _lambda * B)
		sen_prob *= (1.0*word_freq_dict[words[0]] + _lambda)/(N + _lambda * B)
		fw.write(str(round(math.log(sen_prob), 6)))
		for p in gram_probs:
			fw.write('\t'+str(round(math.log(p), 6)))
		fw.write('\n')
	
	with open('../1.txt', 'w') as fw:
		bigram_prob_adding_lambda(u'<BOS> 扶贫 开发 工作 取得 很 大 成绩 <EOS>'.encode('GB2312'), 0.1, fw)
		bigram_prob_adding_lambda(u'<BOS> 扶贫 开发 工作 得到 很 大 成绩 <EOS>'.encode('GB2312'), 0.1, fw)
		bigram_prob_adding_lambda(u'<BOS> 时报社 与 Taylor 签订 的 合约 有效期 到 劳动节 <EOS>'.encode('GB2312'), 0.1, fw)
		bigram_prob_adding_lambda(u'<BOS> 不忘 初心 继续 前进 <EOS>'.encode('GB2312'), 0.1, fw)
		bigram_prob_adding_lambda(u'<BOS> 扶贫 开发 工作 取得 很 大 成绩 <EOS>'.encode('GB2312'), 1.0, fw)
		bigram_prob_adding_lambda(u'<BOS> 扶贫 开发 工作 得到 很 大 成绩 <EOS>'.encode('GB2312'), 1.0, fw)
		bigram_prob_adding_lambda(u'<BOS> 时报社 与 Taylor 签订 的 合约 有效期 到 劳动节 <EOS>'.encode('GB2312'), 1.0, fw)
		bigram_prob_adding_lambda(u'<BOS> 不忘 初心 继续 前进 <EOS>'.encode('GB2312'), 1.0, fw)


def problem_2(held_path=[]):
	data_path = u"/Users/locke/Desktop/2017-2018秋季学期/计算语言学(0)/4_第四章作业续/"
	word_freq_dict_train, sentences_train, N_t = read_data(data_path, [u"train/"])
	word_freq_dict_held, sentences_held, N_h = read_data(data_path, held_path)
	print 'total sentences_train num:', len(sentences_train)
	print 'total sentences_held num:', len(sentences_held)
	n_gram_freq_dict = {}
	tmp_ws = " ".join(sentences_train).split(" ")
	for i in range(len(tmp_ws)-1):
		tar = tmp_ws[i] + " " + tmp_ws[i+1]
		if tmp_ws[i] == "<EOS>" or tmp_ws[i+1] == "<BOS>":
			continue
		if tar in n_gram_freq_dict:
			n_gram_freq_dict[tar] += 1
		else:
			n_gram_freq_dict[tar] = 1

	Nr = {}
	for k in n_gram_freq_dict:
		if n_gram_freq_dict[k] not in Nr:
			Nr[n_gram_freq_dict[k]] = 1
		else:
			Nr[n_gram_freq_dict[k]] += 1
	Nr[0] = len(word_freq_dict_train)*len(word_freq_dict_train) - len(n_gram_freq_dict)

	held_n_gram_freq_dict = {}
	tmp_ws = " ".join(sentences_held).split(" ")
	for i in range(len(tmp_ws)-1):
		tar = tmp_ws[i] + " " + tmp_ws[i+1]
		if tmp_ws[i] == "<EOS>" or tmp_ws[i+1] == "<BOS>":
			continue
		if tar in held_n_gram_freq_dict:
			held_n_gram_freq_dict[tar] += 1
		else:
			held_n_gram_freq_dict[tar] = 1

	Tr = {}
	for r in Nr:
		Tr[r] = 0
		for k in n_gram_freq_dict:
			if n_gram_freq_dict[k] == r and k in held_n_gram_freq_dict:
				Tr[r] += held_n_gram_freq_dict[k]
	Tr[0] = 0
	for i in held_n_gram_freq_dict:
		ws = i.split(" ")
		if i not in n_gram_freq_dict and ws[0] in word_freq_dict_train and ws[1] in word_freq_dict_train:
			Tr[0] += 1

	word_freq_dict_star = {}
	for r in Nr:
		if Tr[r]!=0:
			word_freq_dict_star[r] = 1.0*Tr[r]/Nr[r]
		else:
			word_freq_dict_star[r] = int(r)

	Nr_one = {}
	for k in word_freq_dict_train:
		if word_freq_dict_train[k] not in Nr_one:
			Nr_one[word_freq_dict_train[k]] = 1
		else:
			Nr_one[word_freq_dict_train[k]] += 1
	Nr_one[0] = 0

	Tr_one = {}
	for r in Nr_one:
		Tr_one[r] = 0
		for k in word_freq_dict_train:
			if word_freq_dict_train[k] == r and k in word_freq_dict_held:
				Tr_one[r] += word_freq_dict_held[k]				

	def bigram_prob_held_out(sentence, fw):
		win_len = 2
		words = sentence.split(' ')
		gram_probs = []
		sen_prob = 1.0
		for i in range(len(words)+1-win_len):
			cnt = 0
			tar = ' '.join(words[i:i+win_len])
			if tar in n_gram_freq_dict:
				cnt = n_gram_freq_dict[tar]
			gram_probs.append(1.0 * word_freq_dict_star[cnt] / N_t)
			sen_prob *= 1.0 * word_freq_dict_star[cnt] / N_t
		sen_prob *= 1.0*Tr_one[word_freq_dict_train[words[0]]]/(Nr_one[word_freq_dict_train[words[0]]]*N_t)
		fw.write(str(round(math.log(sen_prob), 6)))
		for p in gram_probs:
			fw.write('\t'+str(round(math.log(p), 6)))
		fw.write('\n')
	
	with open('../2.txt', 'w') as fw:
		bigram_prob_held_out(u'<BOS> 扶贫 开发 工作 取得 很 大 成绩 <EOS>'.encode('GB2312'), fw)
		bigram_prob_held_out(u'<BOS> 扶贫 开发 工作 得到 很 大 成绩 <EOS>'.encode('GB2312'), fw)
		bigram_prob_held_out(u'<BOS> 时报社 与 Taylor 签订 的 合约 有效期 到 劳动节 <EOS>'.encode('GB2312'), fw)
		bigram_prob_held_out(u'<BOS> 不忘 初心 继续 前进 <EOS>'.encode('GB2312'), fw)


def problem_3(path_list=[]):
	data_path = u"/Users/locke/Desktop/2017-2018秋季学期/计算语言学(0)/4_第四章作业续/"
	word_freq_dict, sentences, N = read_data(data_path, path_list)
	print 'total sentences num:', len(sentences)
	threshold = 8

	n_gram_freq_dict = {}
	tmp_ws = " ".join(sentences).split(" ")
	for i in range(len(tmp_ws)-1):
		tar = tmp_ws[i] + " " + tmp_ws[i+1]
		if tmp_ws[i] == "<EOS>" or tmp_ws[i+1] == "<BOS>":
			continue
		if tar in n_gram_freq_dict:
			n_gram_freq_dict[tar] += 1
		else:
			n_gram_freq_dict[tar] = 1

	Nr = {}
	for k in n_gram_freq_dict:
		if n_gram_freq_dict[k] not in Nr:
			Nr[n_gram_freq_dict[k]] = 1
		else:
			Nr[n_gram_freq_dict[k]] += 1
	Nr[0] = len(word_freq_dict)*len(word_freq_dict) - len(n_gram_freq_dict)
	# print Nr

	word_freq_dict_star = {}
	for k in n_gram_freq_dict:
		if n_gram_freq_dict[k]+1 not in Nr:
			Nr[n_gram_freq_dict[k]+1] = 0
		if n_gram_freq_dict[k] <= threshold:
			word_freq_dict_star[n_gram_freq_dict[k]] = 1.0*(n_gram_freq_dict[k]+1)*Nr[n_gram_freq_dict[k]+1] / Nr[n_gram_freq_dict[k]]
		else:
			word_freq_dict_star[n_gram_freq_dict[k]] = Nr[n_gram_freq_dict[k]]
	# print word_freq_dict_star

	Nr_one = {}
	for k in word_freq_dict:
		if word_freq_dict[k] not in Nr_one:
			Nr_one[word_freq_dict[k]] = 1
		else:
			Nr_one[word_freq_dict[k]] += 1
	Nr_one[0] = 0

	word_freq_dict_star_one = {}
	for k in word_freq_dict:
		if word_freq_dict[k]+1 not in Nr_one:
			Nr_one[word_freq_dict[k]+1] = 0
		if word_freq_dict[k] <= threshold:
			word_freq_dict_star_one[word_freq_dict[k]] = 1.0*(word_freq_dict[k]+1)*Nr_one[word_freq_dict[k]+1] / Nr_one[word_freq_dict[k]]
		else:
			word_freq_dict_star_one[word_freq_dict[k]] = Nr_one[word_freq_dict[k]]

	def bigram_prob_good_turing(sentence, fw):
		win_len = 2
		words = sentence.split(' ')
		gram_probs = []
		sen_prob = 1.0
		for i in range(len(words)+1-win_len):
			cnt = 0
			tar = ' '.join(words[i:i+win_len])
			for sen in sentences:
				if tar in sen:
					cnt += 1
			if cnt > 0 :
				gram_probs.append(1.0*word_freq_dict_star[cnt]/word_freq_dict_star_one[word_freq_dict[words[i]]])
				sen_prob *= 1.0*word_freq_dict_star[cnt]/word_freq_dict_star_one[word_freq_dict[words[i]]]
			else:
				gram_probs.append(1.0*Nr[1]/(Nr[0]*N))
				sen_prob *= 1.0*Nr[1]/(Nr[0]*N)
		sen_prob *= 1.0*word_freq_dict_star_one[word_freq_dict[words[0]]] / N
		fw.write(str(round(math.log(sen_prob), 6)))
		for p in gram_probs:
			fw.write('\t'+str(round(math.log(p), 6)))
		fw.write('\n')
	
	with open('../3.txt', 'w') as fw:
		bigram_prob_good_turing(u'<BOS> 扶贫 开发 工作 取得 很 大 成绩 <EOS>'.encode('GB2312'), fw)
		bigram_prob_good_turing(u'<BOS> 扶贫 开发 工作 得到 很 大 成绩 <EOS>'.encode('GB2312'), fw)
		bigram_prob_good_turing(u'<BOS> 时报社 与 Taylor 签订 的 合约 有效期 到 劳动节 <EOS>'.encode('GB2312'), fw)
		bigram_prob_good_turing(u'<BOS> 不忘 初心 继续 前进 <EOS>'.encode('GB2312'), fw)


# problem_1()

# problem_2([u"valid/"])
# problem_2([u"valid/", u"test/"])

# problem_3([u"train/", u"valid/"])
problem_3([u"train/", u"valid/", u"test/"])
