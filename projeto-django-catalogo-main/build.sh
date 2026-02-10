#!/usr/bin/env bash
# Interrompe a execução se algum comando falhar
set -o errexit

# Instala as dependências
pip install -r requirements.txt

# Coleta arquivos estáticos
python manage.py collectstatic --noinput

# Aplica migrações do banco de dados
python manage.py migrate

# Cria o superusuário se ele não existir
if [ "$SUPERUSER_NAME" ]; then
  python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='$SUPERUSER_NAME').exists():
    User.objects.create_superuser('$SUPERUSER_NAME', '$SUPERUSER_EMAIL', '$SUPERUSER_PASSWORD')
    print("Superuser criado com sucesso!")
else:
    print("Superuser já existe.")
END
fi