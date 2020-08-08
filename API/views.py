from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from API.models import UserModel
from API.serializers import UserSerializer

@api_view(["GET"])
@csrf_exempt
def get_users(request):
    users = UserModel.objects.filter()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'ok':True,'members': serializer.data}, safe=False)