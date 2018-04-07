import sys
import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

with stdoutIO() as s:
	sys.argv = ['-image_file_name', 'test.jpg', '-question' ,'"what is the vehicle?"']
	execfile('demo.py')
  

print "out:", s.getvalue()

