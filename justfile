# Run development server.
s:
    ./manage.py runserver

# Open a Django interactive shell.
sh:
    ./manage.py shell

# Check Django project
c:
    ./manage.py check

# Generate migrations
mm app="":
    ./manage.py makemigrations {{ app }}

# Migrate models
m app="":
    ./manage.py migrate {{ app }}

# https://medium.com/@mustahibmajgaonkar/how-to-reset-django-migrations-6787b2a1e723
# https://stackoverflow.com/a/76300128
# Remove migrations and database. Reset DB artefacts.
[confirm("⚠️ All migrations and database will be removed. Continue? [yN]:")]
r-db:
    #!/usr/bin/env bash
    find . -path "*/migrations/*.py" ! -path "./.venv/*" ! -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc" ! -path "./.venv/*" -delete
    rm -f db.sqlite3
    ./manage.py makemigrations
    ./manage.py migrate
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | ./manage.py shell
    echo
    echo "Creating superuser → admin:admin ... OK"

# Reset admin (admin user must exist!)
@reset-admin password="admin":
    echo "from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('{{ password }}'); u.save()" | ./manage.py shell
    echo "✔ Reseted admin account with password '{{ password }}'"

# Open sqlite project database
db:
    sqlite3 db.sqlite3

# Show sqlite DB schema for given table
@schema table:
    sqlite3 db.sqlite3 '.schema --indent {{ table }}'
