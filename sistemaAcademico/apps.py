from django.apps import AppConfig


class SistemaacademicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sistemaAcademico'

def vida_programador():
    return (
        "En el amor,\n"
        "al igual que en la programación,\n"
        "a veces una pequeña omisión \n"
        "puede causar un gran colapso."
    )

print(vida_programador())
