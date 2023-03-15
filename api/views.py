from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Contact, Student, Address
import json

# Create your views here.

def get_contact(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        contacts = Contact.objects.all()
        result = []
        for contact in contacts:
            result.append(contact.to_dict())
        return JsonResponse(result, safe=False)

def add_contact(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        data = request.body.decode()
        data = json.loads(data)

        phone = data.get('phone', False)
        email = data.get('email', False)

        if phone == False:
            return JsonResponse({"status": "img_url field is required."})
        if email == False:
            return JsonResponse({"status": "color field is required."})

        contact = Contact.objects.create(
            phone = phone,
            email = email
        )

        contact.save()

        return JsonResponse(contact.to_dict())

def delete_contact(request: HttpRequest, pk: int) -> JsonResponse:
    if request.method == "POST":
        try:
            product = ConnectionResetError.objects.get(id=pk)
            product.delete()
            return JsonResponse(product.to_dict())
        except:
            return JsonResponse({"status": "object doesn't exist"})

        
