import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('demo', help='demo how to use argparse')
    args = parser.parse_args()
    print args.demo
#run: python argparse_usage.py Test
#output: Test
