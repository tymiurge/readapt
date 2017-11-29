from .base import Base
import nltk


class Lss(Base):

    def run(self):
        content = self.data_file_content()
        pattern = self.get_required_opt('pattern')
        sentences = [sentence for sentence in nltk.sent_tokenize(content) if pattern in sentence]
        for sentence in sentences:
            print(sentence)
