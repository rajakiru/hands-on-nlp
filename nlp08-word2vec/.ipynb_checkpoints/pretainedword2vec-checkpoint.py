# Word2Vec model visualization

# Install gensim - pip install gensim
from gensim.models import KeyedVectors

filename = 'GoogleNews-vectors-negative300.bin'
print("test")
model = KeyedVectors.load_word2vec_format(filename, binary=True)

# similar_words = model.most_similar('kawaii')
# print(similar_words)

# similar_words_with_constraints = model.most_similar(positive=['tokyo', 'kawaii'], negative=['Hello_Kitty'])
# print(similar_words_with_constraints)

# odd_one_out = model.doesnt_match("breakfast cereal dinner lunch".split())
# print(odd_one_out)

# Check if the words are in the vocabulary

if 'lotus' in model.vocab and 'flower' in model.vocab:
    vector_lotus = model['lotus']
    vector_flower = model['flower']
    
    print("Vector representation of 'lotus':")
    print(vector_lotus)
    
    print("\nVector representation of 'flower':")
    print(vector_flower)
else:
    print("One or both of the words are not in the vocabulary.")
