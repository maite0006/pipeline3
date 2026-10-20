from config import APP_NAME


def saludo(nombre):
    return f"Hola, {nombre}! Saludos desde {APP_NAME}"


if __name__ == "__main__":
    print(saludo("DevOps"))
