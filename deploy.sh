
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytnon manage.py migrate
pytnon manage.py collectstatic --input
deactivate
