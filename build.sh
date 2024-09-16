set -0 errexit
pip instal -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate