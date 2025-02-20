from rest_framework.views import APIView
from rest_framework.response import Response
from .models import profile
from .serializers import ProfileSerializer

class ProfileList(APIView):
    def get(self, request):
        profiles = profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)