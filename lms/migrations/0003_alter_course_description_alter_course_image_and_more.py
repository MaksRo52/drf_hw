# Generated by Django 5.1.2 on 2024-11-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0002_alter_lesson_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание курса"
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание урока"
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="video_url",
            field=models.URLField(blank=True, null=True, verbose_name="Ссылка на урок"),
        ),
    ]
