# Generated by Django 4.2.3 on 2023-10-15 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0005_alter_course_table_alter_coursestyle_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_style",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="course.coursestyle"
            ),
        ),
    ]
