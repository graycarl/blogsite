# read the global config file when start
from configparser import ConfigParser

blogconf = ConfigParser()
blogconf.read("blog.conf")
