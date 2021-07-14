python -m pip install -r requirements.txt

# Download & Setup Instructions

- 1 - Clone project: git clone https://github.com/yinglu91/django-ambassador.git
- 2 - cd django-ambassador
- 3 - Create virtual environment:
  virtualenv myenv
- 4 - source myenv/Scripts/activate
- 5 - pip install -r requirements.txt
- 6 - in another cmd $ docker run -p 6379:6379 -d redis:5
- 7 - python manage.py runserver

If install new package, need to update requirements.txt by running
pip freeze > requirements.txt
