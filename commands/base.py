from .errors.missingarg import MissingArgument


class Base(object):

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.excludes = []

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    def data_file_content(self):
        if '<data_file>' not in self.options.keys():
            raise MissingArgument('data_file argument is mandatory.')
        return self.file_content(self.options['<data_file>'])

    @staticmethod
    def file_content(path):
        with open(path, 'r') as data_file:
            return data_file.read()

    def load_excludes(self):
        if self.options['--wt'] is not None:
            excludes_files = self.options['--wt'].split(',')
            for path in excludes_files:
                with open(path.strip(), 'r') as data_file:
                    content = data_file.readlines()
                self.excludes += [word.replace('\n', '') for word in content]
