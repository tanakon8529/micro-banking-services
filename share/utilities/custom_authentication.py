# utilities/custom_authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from utilities.redis_controller import RedisController
from utilities.logger import Logger
from django.contrib.auth.models import AnonymousUser

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        logger = Logger()
        authorization_header = request.headers.get('Authorization')
        logger.debug(f'Authorization header: {authorization_header}')
        
        if not authorization_header:
            raise AuthenticationFailed('Authorization header not provided')
        
        if not authorization_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid authorization scheme')
        
        token = authorization_header.split(' ')[1]  # Extract the token

        redis_controller = RedisController()
        if not redis_controller.get_token(token):
            raise AuthenticationFailed('Invalid or expired token')
        
        # Return a dummy user object and the token
        return (AnonymousUser(), token)
