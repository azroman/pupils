from django.db import models

# Create your models here.
from django.db import models
from django.db.models import CASCADE


class Pupil(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }


class Test(models.Model):
    name = models.CharField(max_length=200)

    def to_dict(self):
        return {
            'name': self.name,
        }


class Exam(models.Model):
    pupil = models.ForeignKey(Pupil, on_delete=CASCADE)
    test = models.ForeignKey(Test, on_delete=CASCADE)
    grade = models.IntegerField()
    score = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        unique_together = ['pupil', 'test', 'grade', 'score', 'date']
        # do we need more complex indexes? I need more info about how do we use it
        indexes = [
            models.Index(fields=['pupil']),
            models.Index(fields=['grade']),
            models.Index(fields=['test']),
            models.Index(fields=['score']),
            models.Index(fields=['date']),
        ]

    def to_dict(self):
        return {
            'pupil': self.pupil.to_dict(),
            'test': self.test.to_dict(),
            'grade': self.grade,
            'score': self.score,
            'date': self.date.strftime('%Y-%m-%d'),
        }