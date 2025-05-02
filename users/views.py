# from rest_framework.viewsets import ModelViewSet
# from .models import User
# from .serializers import UserSerializer
# from rest_framework.permissions import AllowAny

# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]


from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer
from rest_framework.views import APIView


from rest_framework.generics import RetrieveAPIView


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    


# class CurrentUserView(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request):
#         print("✅ USER DEBUG:")
#         print("First Name:", request.user.first_name)
#         print("Last Name:", request.user.last_name)
#         print("Role:", request.user.role)
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)



class CurrentUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

