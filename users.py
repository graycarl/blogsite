# define users function

_username = "carl"
_password = "carlblog"

cookiename = "account"
cookiesecret = "carl-cookie-secret-key"

def verify_user(username, password):
	return _username == username and _password == password

def get_login(request):
	return request.get_cookie(cookiename, secret=cookiesecret)

def set_cookie(response):
	response.set_cookie(cookiename, _username, secret=cookiesecret)

def logout(response):
	response.delete_cookie(cookiename)	