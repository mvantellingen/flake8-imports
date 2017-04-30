import difflib
import io
import os
import sys
from contextlib import contextmanager

from isort import SortImports


class ImportsPlugin(object):
    name = 'flake8_imports'
    version = '0.1.1'
    messages = {
        'I100': "import statement not correctly ordered"
    }

    def __init__(self, tree, filename):
        self.filename = filename

    @classmethod
    def parse_options(cls, options):
        cls.settings_path = os.getcwd()

    def run(self):
        """Run isort on the file"""
        with stdout_redirector(None):
            isort_obj = SortImports(
                file_path=self.filename,
                settings_path=self.settings_path,
                check=True)

        if isort_obj.incorrectly_sorted:
            for line_number in self.get_line_numbers(isort_obj):
                yield (line_number, 0, self.format_message('I100'), '')

    def format_message(self, code):
        return ' '.join((code, self.messages[code]))

    def get_line_numbers(self, isort_obj):
        """Return a list with the line numbers which are incorrect"""
        line_numbers = []
        with io.open(self.filename, encoding=isort_obj.file_encoding) as fh:
            file_contents = fh.read()

        new = isort_obj.output.splitlines()
        old = file_contents.splitlines()
        differ = difflib.Differ().compare(old, new)

        delta = 0
        for i, line in enumerate(differ):
            if line.startswith('  '):
                continue
            if line.startswith(('+', '?')):
                delta += 1
                continue

            if line.startswith('- '):
                line_numbers.append(1 + i - delta)
        return line_numbers


@contextmanager
def stdout_redirector(stream):
    """Redirect stdout for Python < 3.4

    See
    http://eli.thegreenplace.net/2015/redirecting-all-kinds-of-stdout-in-python/

    """
    old_stdout = sys.stdout
    sys.stdout = stream
    try:
        yield
    finally:
        sys.stdout = old_stdout
