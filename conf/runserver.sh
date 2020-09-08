cd /home/batch2-avengers/digicam/current \
&& pip3 install pipenv \
&& (pipenv --rm && pipenv --three) || pipenv --three \
&& pipenv run pip3 install -r requirement.txt \
&& pipenv run python3 manage.py makemigrations \
&& pipenv run python3 manage.py migrate \
&& pipenv run python3 manage.py runserver 8000 \
# python3 -m pipenv install -r requirement.txt
# python3 -m pipenv run python manage.py runserver 8000
