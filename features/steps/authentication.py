from behave import *

use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, password=password)

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/accounts/login'))
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    context.browser.find_by_id('login').click()

@given('Im not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('/accounts/login'))

@given('I register as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.find_by_id('sign').click()
    context.browser.fill('username', username)
    context.browser.fill('password1', password)
    context.browser.fill('password2', password)
    context.browser.find_by_id('login').click()

@then('Im in home')
def step_impl(context):
    assert context.browser.url.startswith(context.get_url(''))