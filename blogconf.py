# read the global config file when start
try: 
	from configparser import ConfigParser # for python3
except ImportError:
	from ConfigParser import ConfigParser # for python2


blogconf = ConfigParser()
blogconf.read("blog.conf")
