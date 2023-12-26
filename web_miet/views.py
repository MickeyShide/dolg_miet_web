import json

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from web_miet.models import Subject, Subject, Prepod, Work, LikeDislike
from web_miet.serializers import SubjectSerializer, SubjectSerializer, PrepodSerializer, WorkSerializer
from django.template import loader
from django.shortcuts import render, redirect

def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    context = {'allobject': Subject.objects.all(), 'username': username}
    return render(request, "index.html", context)

def show_subject(request, id):
    obj = Work.objects.filter(subject_id=id)
    context = {'allobject': obj}
    return render(request, "subject.html", context)


@api_view(['GET', 'POST', 'DELETE'])
def subject_list(request):
    if request.method == 'GET':
        subjects = Subject.objects.all() # берем все
        name = request.query_params.get('name', None)
        if name is not None: # если name есть, то фильтруем по нему
            subjects = subjects.filter(title__icontains=name)
        subjects_serializer = SubjectSerializer(subjects, many=True)
        return JsonResponse(subjects_serializer.data, safe=False)

    elif request.method == 'POST':
        subject_data = JSONParser().parse(request)
        subjects_serializer = SubjectSerializer(data=subject_data)
        if subjects_serializer.is_valid():
            subjects_serializer.save()
            return JsonResponse(subjects_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(subjects_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Subject.objects.all().delete()
        return JsonResponse({'message': '{} Subjects were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def prepod_list(request):
    if request.method == 'GET':
        prepods = Prepod.objects.all() # берем все
        name = request.query_params.get('name', None)
        if name is not None: # если name есть, то фильтруем по нему
            prepods = prepods.filter(title__icontains=name)
        prepods_serializer = PrepodSerializer(prepods, many=True)
        return JsonResponse(prepods_serializer.data, safe=False)

    elif request.method == 'POST':
        prepods_data = JSONParser().parse(request)
        prepods_serializer = PrepodSerializer(data=prepods_data)
        if prepods_serializer.is_valid():
            prepods_serializer.save()
            return JsonResponse(prepods_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(prepods_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Prepod.objects.all().delete()
        return JsonResponse({'message': '{} Prepods were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def work_list(request):
    if request.method == 'GET':
        works = Work.objects.all() # берем все
        name = request.query_params.get('name', None)
        if name is not None: # если name есть, то фильтруем по нему
            works = works.filter(title__icontains=name)
        works_serializer = WorkSerializer(works, many=True)
        return JsonResponse(works_serializer.data, safe=False)

    elif request.method == 'POST':
        works_data = JSONParser().parse(request)
        works_serializer = WorkSerializer(data=works_data)
        if works_serializer.is_valid():
            works_serializer.save()
            return JsonResponse(works_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(works_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Work.objects.all().delete()
        return JsonResponse({'message': '{} Works were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class VotesView(View):
    model = None  # Модель данных - Статьи или Комментарии
    vote_type = None  # Тип комментария Like/Dislike

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id,
                                                  user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['likes'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.likes.create(user=request.user, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.likes.likes().count(),
                "dislike_count": obj.likes.dislikes().count(),
                "sum_rating": obj.likes.sum_rating()
            }),
            content_type="application/json"
        )

@api_view(['GET'])
def likes_count(request, id):
    if request.method == 'GET':
        likes = LikeDislike.objects.all() # берем все
        total_likes = 0
        total_dislikes = 0
        for item in likes.filter(object_id=id):
            if item.vote == 1:
                total_likes+=1
            elif item.vote == -1:
                total_dislikes+=1

        return JsonResponse({"likes": total_likes, "dislikes": total_dislikes }, safe=False)