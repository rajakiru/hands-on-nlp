# Word2Vec model visualization

# Install gensim - pip install gensim
from gensim.models import KeyedVectors

filename = 'GoogleNews-vectors-negative300.bin'

model = KeyedVectors.load_word2vec_format(filename, binary=True)

model.most_similar('kawaii')

model.most_similar(positive=['tokyo','kawaii'], negative= ['Hello_Kitty']) #, topn=1

model.doesnt_match("breakfast cereal dinner lunch".split())