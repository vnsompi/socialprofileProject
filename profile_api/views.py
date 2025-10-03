from rest_framework import viewsets, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from profile_api.models import UserProfile
from profile_api.serializers import UserProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework import filters

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    """handles to get user profile details : read , update , delete"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


"""if the user wants to access to his own information  
, he have to provide a token  from this login  ViewSet """


class LoginViewSet(viewsets.ViewSet):
    """handles  login  and return a token after login """
    """checks email and password  and return a token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """validate user credentials and create token"""
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)



