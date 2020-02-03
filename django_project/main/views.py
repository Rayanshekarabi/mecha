from django.shortcuts import render

from .models import User
from django.http import JsonResponse, HttpResponse

import secrets


# Create your views here.
def check_phone_number(request):
    pass


def generate_token(request):
    nickname = request.GET.get('nickname')
    phone_number = request.GET.get('phone_number')
    # TODO check if these are not empty , then try:
    try:
        user = User()
        user.nickname = nickname
        user.phone_number = phone_number
        generated_token = secrets.token_hex()
        user.token = generated_token
        user.save()
        return JsonResponse(
            {'token': generated_token,
             'status': 200}
        )
    except:
        return JsonResponse(
            {'status': 500}
        )
