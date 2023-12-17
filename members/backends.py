from django.contrib.auth.backends import ModelBackend

class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        print("inside custom backend")
        if user is not None and user.last_login is None:
            print("inside custom backend if")
            # First time this user has logged in
            request.session['first_login'] = True
            return user
        else:
            request.session['first_login'] = False

        return user
