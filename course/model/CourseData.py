from django.db import models

LOCATION = [
    ("1", "Gijang"),
    ("2", "Dongnae"),
    ("3", "Haeundae"),
    ("4", "Seomyeon"),
    ("5", "Gwangan"),
    ("6", "Sasang/Gangseo"),
    ("7", "Yeongdo"),
]

TRAVELING_COMPANION_STYLE = [
    ("1", "Infant"),
    ("2", "Child"),
    ("3", "Teens"),
    ("4", "20s"),
    ("5", "30s"),
    ("6", "40s"),
    ("7", "50s"),
    ("8", "60s"),
    ("9", "70sOr"),
]

SCHEDULE_STYLE = [
    ("1", "Diligently"),
    ("2", "Leisurely"),
]

ACTIVITY_STYLE = [
    ("1", "Walking"),
    ("2", "Dynamic"),
    ("3", "Calm"),
]

ATTRACTION_STYLE = [
    ("1", "Urban"),
    ("2", "Nature"),
]

TRAVEL_KEYWORD = [
    ("1", "K-pop"),
    ("2", "With Family"),
    ("3", "Traditional"),
    ("4", "With friend"),
    ("5", "Instagramable"),
    ("6", "Ocean"),
]


class CourseData(models.Model):
    traveling_companion = models.CharField(max_length=100)  # / 로 구분
    is_disablity = models.BooleanField(null=True)

    schedule = models.CharField(max_length=50, choices=SCHEDULE_STYLE, null=True)
    activity = models.CharField(max_length=50, choices=ACTIVITY_STYLE, null=True)
    attraction = models.CharField(max_length=50, choices=ATTRACTION_STYLE, null=True)
    keyword = models.CharField(max_length=100)  # / 로 구분

    days = models.IntegerField(null=True)

    location = models.CharField(max_length=50, choices=LOCATION, default=LOCATION[0])

    detail = models.JSONField()

    class Meta:
        db_table = "course_data"
