# 1. Clone repository
# 2. Go to the pupils folder 
# 3. Create virtual env and install Django (requirements.txt).
```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
# 4. Run migrations
```
python manage.py migrate
```
# 5. Uploda data
```
python manage.py upload_pupils take_home_assignment_data.csv
```
# 6. Run server and test
```
python manage.py runserver
```
Examples:

http://127.0.0.1:8000/api/grades
http://127.0.0.1:8000/api/grades/2/
http://127.0.0.1:8000/api/pupil/1/scores
http://127.0.0.1:8000/api/scores?grade=3&pupil_id=12
http://127.0.0.1:8000/api/scores?grade=3&pupil_id=12&max_score=22
http://127.0.0.1:8000/api/scores?grade=3&pupil_id=12&max_score=30
http://127.0.0.1:8000/api/scores?test_name=CITO_MATH
http://127.0.0.1:8000/api/scores?grade=3&pupil_id=12&min_date=2019-01-01

NOTE:
date format is %Y-%m-%d  (2022-06-06)