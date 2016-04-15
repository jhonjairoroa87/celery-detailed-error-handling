from __future__ import absolute_import

from math import log
from proj.base_tasks import CallbackTask
from proj.celery_app import app as celery_app


@celery_app.task(name="tasks.add")
def print_add(x, y):
    """
    Print the sum of two numbers
    :param x: Integer, first number to be summed
    :param y: Integer, second number to be summed
    """
    print x + y


@celery_app.task(name="tasks.mul")
def print_div(x, y):
    """
    Print the division of two numbers
    :param x: Integer, dividend of the operation
    :param y: Integer, divisor of the operation
    :return:
    """
    print x/y


@celery_app.task(base=CallbackTask, name="tasks.xsum")
def print_log(x):
    """
    Print the log of the given number
    :param x: Integer, number calculate its log
    """
    print log(x)
