import uuid
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from utilities.response_controller import ResponseController as Response
from utilities.redis_controller import RedisController
from utilities.logger import Logger
from django.conf import settings


class CustomTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        logger = Logger()

        try:
            # Get from body json
            client_id = request.data.get('client_id')
            client_secret = request.data.get('client_secret')

            # Validate the provided client_id and client_secret
            if not client_id or not client_secret:
                logger.error(__file__, self.post.__name__, 'client_id or client_secret not provided')
                return Response.error('client_id or client_secret not provided')
            
            if client_id != settings.CLIENT_ID or client_secret != settings.CLIENT_SECRET:
                logger.error(__file__, self.post.__name__, 'Invalid client_id or client_secret')
                return Response.error('Invalid client_id or client_secret')

            # Generate a UUIDv4 token
            token = str(uuid.uuid4())

            # Save the token to Redis with a 1-hour expiration
            redis_controller = RedisController()
            redis_controller.set_token(token, 'valid', expiration=3600)

            logger.debug("Token generated successfully")
            # Return the token in the response
            return Response.success("Token generated successfully", {
                'access_token': token,
                'grant_type': 'Bearer'
            })
        except Exception as e:
            error_id = logger.error(__file__, self.post.__name__, str(e))
            return Response.error(f'Internal server error, error_id: {error_id}', status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        logger = Logger()
        authorization_header = request.headers.get('Authorization')
        
        if not authorization_header:
            logger.error(__file__, self.get.__name__, 'Authorization header not provided')
            return Response.error('Authorization header not provided')
        
        if not authorization_header.startswith('Bearer '):
            logger.error(__file__, self.get.__name__, 'Invalid authorization scheme')
            return Response.error('Invalid authorization scheme')
        
        token = authorization_header.split(' ')[1]  # Extract the token

        try:
            redis_controller = RedisController()
            if redis_controller.get_token(token):
                logger.debug("Token is valid")
                return Response.success("Token is valid", {'valid': True})
            logger.debug("Token is invalid")
            return Response.success("Token is invalid", {'valid': False})
        except Exception as e:
            error_id = logger.error(__file__, self.get.__name__, str(e))
            return Response.error(f'Internal server error, error_id: {error_id}', status.HTTP_500_INTERNAL_SERVER_ERROR)
