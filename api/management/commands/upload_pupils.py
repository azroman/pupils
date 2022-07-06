from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from api.models import Pupil, Test, Exam


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('filepath', nargs='+', type=str)

    def handle(self, *args, **options):
        filepath = options['filepath'][0]
        print('uploading pupils from file {}'.format(filepath))
        # right now I believe that file absolutely correct
        # todo we need a validation for name (i mean we have first name and last name), date, score e.t.c
        with open(filepath) as f:
            line = f.readline()
            while line:
                if not line:
                    continue
                line = f.readline()
                splitted = line.split(',')
                p_id = splitted[0]
                name = splitted[1].replace('"', '')
                first_name = name.split(' ')[0]
                last_name = name.split(' ')[1]
                grade = splitted[2]
                test_name = splitted[3].replace('"', '')
                score = splitted[4]
                p_date = splitted[5].replace('\n', '').replace('"', '')
                date = datetime.strptime(p_date, '%Y-%m-%d')
                pupil, _ = Pupil.objects.get_or_create(
                    id=int(p_id),
                    first_name=first_name,
                    last_name=last_name,
                )
                test, _ = Test.objects.get_or_create(
                    name=test_name
                )
                try:
                    Exam.objects.create(
                        pupil=pupil,
                        test=test,
                        score=score,
                        grade=grade,
                        date=date
                    )
                except IntegrityError:
                    # we ignore duplicates
                    pass
                print('uploaded: {}'.format(line))
