from django.db import models
from django.contrib.auth.models import User

OAUTH_PROVIDER_CHOICES = [
    ("1", "NONE"),
    ("2", "KAKAO"),
    ("3", "GOOGLE"),
]


class Member(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    # course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    email = models.EmailField(max_length=300)  # 이메일
    passwd = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=30, blank=True)  # 이름: 이름
    last_name = models.CharField(max_length=150, blank=True)  # 이름: 성
    refresh_token = models.CharField(
        max_length=350, default=None, null=True
    )  # refresh token : access token 이 만료되면 이것을 비교해서 같으면 재 발급
    oauth_provider = models.CharField(
        max_length=50, choices=OAUTH_PROVIDER_CHOICES, default=OAUTH_PROVIDER_CHOICES[0]
    )  # 로그인 제공
    is_authorized = models.BooleanField(default=False)

    def __str__(self):
        return self.email  # 닉네임 값을 대표값으로 설정
