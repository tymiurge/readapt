"""
Usage:
    readupp lss <data_file> <pattern>
    readupp lsw <data_file> [--wt=FILES]
"""

"""
    command examples:
    readupp.py lsw data/the-happy-prince.txt --wt="data/garbage.txt, data/known.txt"
    readupp.py lss " fumble "
"""

from docopt import docopt
from inspect import getmembers, isclass


def _find_command(opts):
    import commands
    for k in opts.keys():
        if hasattr(commands, k) and opts[k]:
            command_module = getattr(commands, k)
            commands = getmembers(command_module, isclass)
            command = [command[1] for command in commands if k == command[0].lower()][0]
            return command(opts)
    raise NotImplemented('not implemented command.')


def main(opts):
    command = _find_command(opts)
    command.run()


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments)
