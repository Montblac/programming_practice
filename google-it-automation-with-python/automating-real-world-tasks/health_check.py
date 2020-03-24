#!/usr/bin/env python3
import os
import time
import shutil
import psutil
import emails
import socket

def check_disk_usage(disk, threshold):
    du = shutil.disk_usage('/')
    free = du.free / du.total * 100
    return free > threshold

def check_cpu_usage(interval, threshold):
    usage = psutil.cpu_percent(interval)
    return usage < threshold

def check_memory_usage(threshold):
    mu = psutil.virtual_memory()
    threshold = threshold * 1024 ** 2
    return mu.available > threshold

def check_hostname(name):
    ip = socket.gethostbyname(name)
    return ip == '127.0.0.1'


if __name__ == '__main__':
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(os.environ.get('USER'))
    body = 'Please check your system and resolve the issue as soon as possible'

    while true:
        du_limit = 20
        if not check_disk_usage('/', du_limit):
            subject = 'Error - Available disk space is less than 20%'
            msg = emails.generate_email(sender, recipient, subject, body)
            emails.send_email(msg)

        cpu_limit = 80
        interval = 60
        if not check_cpu_usage(interval, cpu_limit):
            subject = 'Error - CPU usage is over 80%'
            msg = emails.generate_email(sender, recipient, subject, body)
            emails.send_email(msg)

        mu_limit = 500
        if not check_memory_usage(mu_limit):
            subject = 'Error - Available memory is less than 500MB'
            msg = emails.generate_email(sender, recipient, subject, body)
            emails.send_email(msg)

        hostname = 'localhost'
        if not check_hostname(hostname):
            subject = 'Error - localhost cannot be resolved to 127.0.0.1'
            msg = emails.generate_email(sender, recipient, subject, body)
            emails.send_email(msg)
