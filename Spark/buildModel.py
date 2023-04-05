from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.models.fasttext import FastText
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

SIZE = 300
WINDOW = 5
MIN_COUNT = 10
WORKERS = 6
SG = 1
ITER = 20
SEED = 777

sentences = LineSentence('jawiki_wakati.txt')
model = FastText(sentences, size=SIZE, window=WINDOW, min_count=MIN_COUNT, workers=WORKERS, sg=SG, iter=ITER, seed=SEED)
model.save('jawiki_fasttext.model')
