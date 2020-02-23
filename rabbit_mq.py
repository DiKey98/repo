import time
import sim

def send_message(query, msg):
    _, err = mq.send(query, msg)
    return err


def get_message(query):
    msg = mq.get(query)
    return msg