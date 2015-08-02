#!/usr/bin/python

import sys
from collections import defaultdict
import os

# TODO(burdon): Fails if not set; (default to ~/.nexus.log)
LOG_FILE = os.environ['NEXUS_LOG']

# TODO(burdon): By default add command line to log (e.g., memo !!)
# TODO(burdon): List all commands: memo --list
# TODO(burdon): List commands by type (e.g., memo docker rmi); add if new? normalize args?
# TODO(burdon): Auto group by first command then sort alphabetically.
# TODO(burdon): Auto link docs (from web search)
# TODO(burdon): Delete log entry (e.g., memo rm 2)
# TODO(burdon): Add comment to log entry (e.g, memo !! -m List all files)
# TODO(burdon): Edit file directly: memo edit
# TODO(burdon): Install via brew: http://formalfriday.club/2015/01/05/creating-your-own-homebrew-tap-and-formula.html


# TODO(burdon): Move to class.
class Parser(object):

    def __init__(self, filename):
        """ Parses the file and builds a command map. """
        self.filename = filename
        self.command_map = defaultdict(list)
        # TODO(burdon): Error if file does not exist.
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                words = line.split()
                if words:
                    command = words[0]
                    self.command_map[command].append(line)
                    self.command_map[command].sort()

    def dump(self, command=None):
        print
        if command:
            for line in self.command_map[command]:
                print line
            print
        else:
            for k, v in self.command_map.iteritems():
                for line in v:
                    print line
                print

    def write(self):
        f = open(self.filename, 'w')
        for k, v in self.command_map.iteritems():
            for line in v:
                f.write(line + '\n')
            f.write('\n')
        f.close()


def main():
    # TODO(burdon): Match anything.
    parser = Parser(LOG_FILE)
    if len(sys.argv) == 2:
        command = sys.argv[1]
        parser.dump(command)
    else:
        parser.dump()
        parser.write()

        # TODO(burdon): Process flags
        print 'DEBUG'
        for arg in sys.argv:
            print arg


main()

