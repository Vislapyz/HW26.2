# Generated by Django 5.0.6 on 2024-07-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите аватар",
                null=True,
                upload_to="users/avatars",
                verbose_name="Аватар",
            ),
        ),
    ]
