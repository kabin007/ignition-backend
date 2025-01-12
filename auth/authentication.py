from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
from datetime import datetime
from user.models import Student  

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            # Extract the token
            token = auth_header.split(' ')[1]
            
            # Decode the token
            payload = jwt.decode(
                token, 
                settings.JWT_SECRET_KEY, 
                algorithms=['HS256']
            )

            # Check if token is expired
            if datetime.fromtimestamp(payload['exp']) < datetime.now():
                raise AuthenticationFailed('Token has expired')

            # Get the user
            user = Student.objects.get(id=payload['user_id'])
            
            return (user, token)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        except Student.DoesNotExist:
            raise AuthenticationFailed('User not found')
        except (IndexError, KeyError):
            raise AuthenticationFailed('Invalid token format')

    def authenticate_header(self, request):
        return 'Bearer'