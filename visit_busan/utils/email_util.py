from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import render_to_string

import random

from account.cache.authorized_code import save_authorized_code
from visit_busan.settings import EMAIL_HOST_USER

RANDOM_CONDE_LENGTH = 4


def send_sign_up_email(email):
    # 1. 인증 코드 생성 및 저장
    authorized_code = random.randrange(1000, 10000)
    save_authorized_code(authorized_code, email)

    # 2. 이메일 전송
    title = "Visit Busan Tour 이메일 인증"
    content = f"인증코드: {authorized_code}"
    email = EmailMessage(title, content, to=[email])
    email.send()


def send_sign_up_email_with_templete(email):
    # 1. 인증 코드 생성 및 저장
    authorized_code = random.randrange(1000, 10000)
    save_authorized_code(authorized_code, email)

    subject = "[Visit Busan Tour] Membership e-mail authentication"
    sender_email = EMAIL_HOST_USER
    context = {
        "email": email,
        "authorized_code": authorized_code,
    }

    # 2. 이메일 전송
    html_mail = render_to_string("account/email_authentication_b.html", context)
    content = f"인증코드: {authorized_code}"
    send_mail(subject, content, sender_email, [email], html_message=html_mail)


def send_passwd(email, passwd):
    # 2. 이메일 전송
    title = "Visit Busan Tour 비밀번호 찾기"
    content = f"이메일: {email} \n 비밀번호: {passwd}"
    email = EmailMessage(title, content, to=[email])
    email.send()


def send_passwd_with_templete(email, passwd):
    # 1. 인증 코드 생성 및 저장
    authorized_code = random.randrange(1000, 10000)
    save_authorized_code(authorized_code, email)

    subject = "[Visit Busan Tour] Find password"
    sender_email = EMAIL_HOST_USER
    context = {
        "email": email,
        "passwd": passwd,
    }

    # 2. 이메일 전송
    html_mail = render_to_string("account/find_passwd.html", context)
    content = f"email: {email} \n passwd: {passwd}"
    send_mail(subject, content, sender_email, [email], html_message=html_mail)
