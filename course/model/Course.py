from django.db import models

from course.model.CourseStyle import CourseStyle
from account.model.Member import Member


class Course(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    course_style = models.OneToOneField(CourseStyle, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)

    start_date = models.DateField()
    end_date = models.DateField()
    departure = models.CharField(max_length=50)  # 출발지
    destination = models.CharField(max_length=50)  # 도착지
    total_people_cnt = models.IntegerField(null=True)
    course_detail = models.JSONField()

    class Meta:
        db_table = "courses"

    """
    [
       {
          "date": XXXX-XX-XX,
          "location": [ {
              "location_name": "",
              "location_url": "",
              "location_address"; "",
              "location_longitude": 0,
              "location_latitude": 0,
              "location_score": 0.00,
              "location_type": "MUSEUM/RESTARTANT/YACHT/",
            }       
          ]
        },
    ]
    """
