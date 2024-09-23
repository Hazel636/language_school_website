from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import os

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        wechat = request.POST['wechat']
        message = request.POST['message']
        
        contact = Contact(listing = listing, listing_id = listing_id, name = name, email = email, phone = phone, wechat_account = wechat, message = message)

        contact.save()
        a = os.environ.get("EMAIL_HOST_USER")
        b = os.environ.get("EMAIL_HOST_PASSWORD")
        c = "content"
        print(a, b, c)
        
        send_mail(
            'Language course inquery',
            'There is an inquery for ' + listing + '.',
            'xiehe0620@outlook.com',
            ['xiehe0620@outlook.com'],            
            fail_silently = False,
        )

        messages.success(request,'非常感谢! 您的咨询已经提交, 我们的客服人员会在24小时内联系您! ')

        referer = request.META.get('HTTP_REFERER', '/')
        return redirect(referer)