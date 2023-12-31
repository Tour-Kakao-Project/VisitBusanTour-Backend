# Generated by Django 4.2.3 on 2023-08-30 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CourseStyle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "schedule_style",
                    models.CharField(
                        choices=[("1", "부지런하게"), ("2", "여유롭게")], max_length=50
                    ),
                ),
                (
                    "activity_style",
                    models.CharField(
                        choices=[("1", "액티비티_여행"), ("2", "잔잔한_여행")], max_length=50
                    ),
                ),
                (
                    "accommodation_style",
                    models.CharField(
                        choices=[("1", "시설"), ("2", "가성비")], max_length=50
                    ),
                ),
                (
                    "attraction_style",
                    models.CharField(
                        choices=[("1", "유명한명소"), ("2", "덜유명한명소")], max_length=50
                    ),
                ),
                (
                    "travel_keyword",
                    models.CharField(
                        choices=[
                            ("1", "한류"),
                            ("2", "K-POP"),
                            ("3", "첫 부산여행"),
                            ("4", "전통문화"),
                            ("5", "인스타그램"),
                            ("6", "바다"),
                        ],
                        max_length=50,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("place", models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("departure", models.CharField(max_length=50)),
                ("destination", models.CharField(max_length=50)),
                ("course_detail", models.JSONField()),
                (
                    "course_style",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.coursestyle",
                    ),
                ),
            ],
        ),
    ]
