# define users function

_username = "carl"
_password = "carlblog"

cookiename = "account"
cookiesecret = "carl-cookie-secret-key"

def verify_user(username, password):
	return _username == username and _password == password
