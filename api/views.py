import statistics
from datetime import datetime

from django.http import JsonResponse
from .models import Exam, Pupil


def grades(request, grade_value=None):
    exam_q = Exam.objects.all()
    if grade_value:
        exam_q = exam_q.filter(grade=grade_value)
    pupils = Pupil.objects.filter(id__in=exam_q.values('pupil_id'))
    return JsonResponse([p.to_dict() for p in pupils], safe=False)


def pupil_scores(request, pk):
    return JsonResponse([e.to_dict() for e in Exam.objects.filter(pupil__id=pk)], safe=False)


def scores(request):
    grade = request.GET.get('grade')
    pupil_id = request.GET.get('pupil_id')
    test_name = request.GET.get('test_name')
    min_score = request.GET.get('min_score')
    max_score = request.GET.get('max_score')
    min_date = request.GET.get('min_date')
    max_date = request.GET.get('max_date')
    q = Exam.objects.all()
    if grade:
        q = q.filter(grade=grade)
    if pupil_id:
        q = q.filter(pupil__id=pupil_id)
    if test_name:
        q = q.filter(test__name=test_name)
    if min_score:
        min_score = int(min_score)
        q = q.filter(score__gte=min_score)
    if max_score:
        max_score = int(max_score)
        q = q.filter(score__lte=max_score)
    if min_date:
        min_date = datetime.strptime(min_date, '%Y-%m-%d')
        q = q.filter(date__gte=min_date)
    if max_date:
        max_date = datetime.strptime(max_date, '%Y-%m-%d')
        q = q.filter(date__lte=max_date)
    values = list(q.values_list('score', flat=True))

    return JsonResponse({
        'median': statistics.median(values) if values else '',
        'average': statistics.mean(values) if values else '',
    }, safe=False)
