#coding=utf-8
import os
import chardet
import math

def problem_1(data_path):
	file_dirs =  os.listdir(data_path)
	word_freq_dict = {}
	for filename in file_dirs:
		with open(data_path + filename, 'r') as fr:
			print filename
			for line in fr:
				words = line.strip().split('  ')
				for w in words:
					if w not in word_freq_dict:
						word_freq_dict[w] = 1
					else:
						word_freq_dict[w] += 1

	sorted_pairs = sorted(word_freq_dict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True) 
	with open(data_path+"../1.txt", 'w') as fw:
		for item in sorted_pairs:
			fw.write(item[0] + '\t' + str(item[1]).encode('GB2312') + '\n')
	return

def problem_2(data_path):
	file_dirs =  os.listdir(data_path)
	sentences_splitor = [u'。'.encode('GB2312'), u'！'.encode('GB2312'), u'？'.encode('GB2312')]
	word_freq_dict = {}
	word_freq_dict['<BOS>'] = 0
	word_freq_dict['<EOS>'] = 0
	sentences = []
	sen = []
	N = 0
	for filename in file_dirs:
		with open(data_path + filename, 'r') as fr:
			print filename
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
	
	for k in word_freq_dict:
		N += word_freq_dict[k]

	print 'total sentences num:', len(sentences)

	def unigram_prob(sentence, fw):
		words = sentence.split(' ')
		probs = []
		sen_prob = 1.0
		for w in words:
			if w not in word_freq_dict:
				print 'warning.'
			else:
				probs.append(1.0*word_freq_dict[w]/N)
				sen_prob *= 1.0*word_freq_dict[w]/N
		fw.write(str(round(math.log(sen_prob), 6)))
		for p in probs:
			fw.write('\t'+str(round(math.log(p), 6)))
		fw.write('\n')

	def bigram_prob(sentence, fw):
		win_len = 2
		words = sentence.split(' ')
		gram_probs = []
		sen_prob = 1.0
		for i in range(len(words)+1-win_len):
			cnt = 0
			tar = ' '.join(words[i:i+win_len-1])
			for sen in sentences:
				if tar in sen:
					cnt += 1
			gram_probs.append(1.0*cnt/word_freq_dict[words[i]])
			sen_prob *= 1.0*cnt/word_freq_dict[words[i]]
		sen_prob *= 1.0*word_freq_dict[words[0]]/N
		fw.write(str(math.log(round(sen_prob, 6))))
		for p in gram_probs:
			fw.write('\t'+str(round(math.log(p), 6)))
		fw.write('\n')

	with open('../3.txt', 'w') as fw:
		unigram_prob(u'扶贫 开发 工作 取得 很 大 成绩'.encode('GB2312'), fw)
		bigram_prob(u'扶贫 开发 工作 取得 很 大 成绩'.encode('GB2312'), fw)
		bigram_prob(u'<BOS> 扶贫 开发 工作 取得 很 大 成绩'.encode('GB2312'), fw)
		bigram_prob(u'<BOS> 扶贫 开发 工作 取得 很 大 成绩 <EOS>'.encode('GB2312'), fw)

		unigram_prob(u'扶贫 开发 工作 得到 很 大 成绩'.encode('GB2312'), fw)
		bigram_prob(u'扶贫 开发 工作 得到 很 大 成绩'.encode('GB2312'), fw)
		bigram_prob(u'<BOS> 扶贫 开发 工作 得到 很 大 成绩'.encode('GB2312'), fw)
		bigram_prob(u'<BOS> 扶贫 开发 工作 得到 很 大 成绩 <EOS>'.encode('GB2312'), fw)


data_path = u"/Users/locke/Desktop/2017-2018秋季学期/计算语言学(0)/熟语料/"

problem_1(data_path)
problem_2(data_path)
