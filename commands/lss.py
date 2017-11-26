from .base import Base
import nltk


class Lss(Base):

    def run(self):
        content = self.data_file_content()
        sentences = nltk.sent_tokenize(content)
