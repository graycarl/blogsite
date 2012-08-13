#!\python31\python.exe
# adapter for apache mod_wsgi

import sys, os
cur_path = os.path.abspath(os.path.dirname(__file__))
sys.path = [cur_path] + sys.path
os.chdir(cur_path)

import bottle
import main

application =  main.app



