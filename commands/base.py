from .errors.missingarg import MissingArgument


class Base(object):

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    def data_file_content(self):
        if '<data_file>' not in self.options.keys():
            raise MissingArgument('data_file argument is mandatory.')
        with open(self.options['<data_file>'], 'r') as data_file:
            return data_file.read()
