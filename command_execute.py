import subprocess
import shlex

def run(cmd):
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode()

def run_multiples(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out,err = process.communicate()
    return out.decode()

if __name__ == '__main__':
    print run('dir')
    print run_multiples('echo a;echo b')
