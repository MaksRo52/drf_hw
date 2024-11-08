# Generated by Django 5.1.2 on 2024-11-08 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0003_alter_course_description_alter_course_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="lesson",
                to="lms.course",
                verbose_name="Курс",
            ),
        ),
    ]
