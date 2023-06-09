# Generated by Django 4.2 on 2023-04-19 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Character",
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
                ("name", models.CharField(max_length=32, verbose_name="Имя персонажа")),
                ("image", models.TextField(verbose_name="Модель персонажа")),
            ],
        ),
        migrations.CreateModel(
            name="Level",
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
                ("topic", models.CharField(max_length=32, verbose_name="Тема вопроса")),
                (
                    "task",
                    models.CharField(
                        max_length=256, verbose_name="Вопрос для пользователя"
                    ),
                ),
                (
                    "answer",
                    models.CharField(max_length=256, verbose_name="Ответ на вопрос"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Theory",
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
                ("topic", models.CharField(max_length=32, verbose_name="Тема вопроса")),
                (
                    "content",
                    models.CharField(max_length=256, verbose_name="Содержание вопроса"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                (
                    "wallet",
                    models.CharField(
                        max_length=42,
                        unique=True,
                        verbose_name="Адрес кошелька пользователя",
                    ),
                ),
                (
                    "contract",
                    models.CharField(
                        max_length=42, verbose_name="Контракт пользователя"
                    ),
                ),
                (
                    "character",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="CharacterOf",
                        to="mainTatarin.character",
                    ),
                ),
                (
                    "level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="LevelOf",
                        to="mainTatarin.level",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reward",
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
                (
                    "caption",
                    models.CharField(max_length=32, verbose_name="Название NFT"),
                ),
                ("hash", models.CharField(max_length=46, verbose_name="Хэш NFT")),
                (
                    "theory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="TheoryOf",
                        to="mainTatarin.theory",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="level",
            name="reward",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="RewardOf",
                to="mainTatarin.reward",
            ),
        ),
    ]
