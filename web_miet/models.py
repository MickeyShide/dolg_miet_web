from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum

from web_miet import settings


class Subject(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()

class Prepod(models.Model):
    name = models.CharField(max_length=80)
    subject = models.ForeignKey(Subject, on_delete=models.SET("Удален"))


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

class LikeDislike(models.Model):

    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()


class Work(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    prepod = models.ForeignKey(Prepod, on_delete=models.SET("Удален"))
    likes = GenericRelation(LikeDislike, related_query_name='works')


