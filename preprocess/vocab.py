def extractVocab(datafile):
	word_vocab_index = 2
	tag_vocab_index = 2
	word2id = {'<pad>': 0, '<unk>': 1}
	tag2id = {'<pad>': 0, '<unk>': 1}
	id2word = ['<pad>', '<unk>']
	id2tag = ['<pad>', '<unk>']
	fin = open(datafile, 'r')
	for line in fin:
		line = line.split("\t")
		word = line[0].strip()
		tag = line[1].strip()
		if word not in word2id:
			word2id[word] = word_vocab_index
			id2word.append(word)
			word_vocab_index += 1
		if tag not in tag2id:
			tag2id[tag] = tag_vocab_index
			id2tag.append(tag)
			tag_vocab_index += 1
	return word2id, tag2id, id2word, id2tag
