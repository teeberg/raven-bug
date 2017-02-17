# Reproduce bug

- pip install -r requirements.txt
- Add a dsn.txt with your DSN (or just add it to the `settings.py`)
- Run `./manage.py migrate`
- Run `./manage.py bug`

Output:
```
>>> ./manage.py bug
/api/{api_name}/{api_name}/{resource_name}/
```