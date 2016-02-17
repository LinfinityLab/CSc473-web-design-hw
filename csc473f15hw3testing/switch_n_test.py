#Fileswitcher for testing
import os
import os.path as op
import argparse
from subprocess import Popen
import requests
import sys

url_prefix = ("http://bitbucket.org/mdogy/html_samples_csc473s15hw3"+
              "/raw/tip")
files = ["hw3p3_ex1.html",
          "hw3p3_ex2.html",
          "hw3p3_ex3.html",
          "hw3p3_ex4.html",
          "hw3p3_ex5.html"]

urls = ["/".join([url_prefix,fl]) for fl in files]

link_name = "index.html"

def main():
    parser = argparse.ArgumentParser(description='Switch the appropriate file for testing via symbolic link.')
    parser.add_argument('integers', type=int, nargs=1, help='index of file to switch')
    arg = parser.parse_args()
    file_index = arg.integers[0]-1
    if (file_index < 0 or len(files) <= file_index):
        error_msg = "Argument {0} must be in the range {1}-{2}\n"
        sys.stderr.write(error_msg.format(file_index+1,1,len(files)))
        return
    if (op.exists(link_name)):
        os.unlink(link_name)
    r = requests.get(urls[file_index])
    print urls[file_index]
    with open(link_name,'w') as fid:
        fid.write(r.text)
    pid = Popen('nosetests test_hw3p3.py',shell=True)
    pid.communicate()
    if (op.exists(link_name)):
        os.unlink(link_name)
    
if __name__ == '__main__':
    main()
