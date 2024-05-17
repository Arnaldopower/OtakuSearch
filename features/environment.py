from django.core.management import call_command
from splinter import Browser


def before_all(context):
    context.browser = Browser('edge', headless=False)


def before_feature(context, scenario):
    call_command('populate')


def after_all(context):
    context.browser.quit()
    context.browser = None
