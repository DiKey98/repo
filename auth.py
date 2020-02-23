import time
import sim

def yandex_auth(token):
    err = requests.get("yandex.ru/auth", token)