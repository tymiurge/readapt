from .base import Base
import nltk
from nltk.stem.snowball import SnowballStemmer
from collections import Counter


class Lsw(Base):

    word_slot_size = 20

    def run(self):
        stemmer = SnowballStemmer("english")
        content = self.data_file_content()
        # sentences = nltk.sent_tokenize(content)
        # words = [stemmer.stem(word.lower()) for word in nltk.word_tokenize(content)]
        words = [word.lower() for word in nltk.word_tokenize(content)]
        counter = Counter(words)
        ranked = counter.most_common()
        for word_tuple in ranked:
            print(self._word_slot(word_tuple[0]) + str(word_tuple[1]))

    @staticmethod
    def _word_slot(word):
        spaced_slot = ' ' * (Lsw.word_slot_size - len(word))
        return word + spaced_slot

