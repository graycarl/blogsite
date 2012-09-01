# define users function
from blogconf import blogconf

_username = blogconf.get("user", "username")
_password = blogconf.get("user", "password")

cookiename = blogconf.get("cookies", "name")
cookiesecret = blogconf.get("cookies", "secret")

def verify_user(username, password):
	return _username == username and _password == password

def get_login(request):
	return request.get_cookie(cookiename, secret=cookiesecret)

def set_cookie(response):
	response.set_cookie(cookiename, _username, secret=cookiesecret)

def logout(response):
	response.delete_cookie(cookiename)	
