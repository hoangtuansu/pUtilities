import subprocess
import shlex

def run(cmd):
	process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
	out, err = process.communicate()
	return out.decode()

if __name__ == '__main__':
	print run('dir')
