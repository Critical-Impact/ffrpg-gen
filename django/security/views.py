from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from security.serializers import AuthTokenLoginSerializer


class ObtainAuthTokenLogin(APIView):

    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenLoginSerializer
    model = Token

    permission_classes = (AllowAny),
    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended"
    }

    def _error_response(self, message_key):
        """
        Return an error message.
        """
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }
        return Response(data)

    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            try:
                token = Token.objects.get(user=serializer.object['user'])
                return Response({'token': token.key, 'user_id': serializer.object['user'].id})
            except ObjectDoesNotExist:
                return Response({}, status=status.HTTP_403_FORBIDDEN)

        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        """
        Destroy the active session, effectively logging out the
        current user.
        """
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

obtain_auth_token_login = ObtainAuthTokenLogin.as_view()