# Word2Vec model visualization

# Install gensim - pip install gensim
from gensim.models import KeyedVectors

filename = 'GoogleNews-vectors-negative300.bin'
print("test")
model = KeyedVectors.load_word2vec_format(filename, binary=True)

similar_words = model.most_similar('kawaii')
print(similar_words)

similar_words_with_constraints = model.most_similar(positive=['tokyo', 'kawaii'], negative=['Hello_Kitty'])
print(similar_words_with_constraints)

odd_one_out = model.doesnt_match("breakfast cereal dinner lunch".split())
print(odd_one_out)


