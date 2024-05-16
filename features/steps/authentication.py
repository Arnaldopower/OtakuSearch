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


@given('I logout')
def step_impl(context):
    context.browser.find_by_id('prof').click()
    context.browser.find_by_id('out').click()


@given('I erase my account')
def step_impl(context):
    context.browser.find_by_id('prof').click()
    context.browser.find_by_id('delete-account-button').click()
    context.browser.find_by_id('del').click()


@given('Im not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('/accounts/login'))


@given('Im going to register but i remember my user and password')
def step_imp(context):
    context.browser.visit(context.get_url('/accounts/login'))
    context.browser.find_by_id('sign').click()
    context.browser.find_by_id('logi').click()


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


@then('Im back at login')
def step_impl(context):
    assert context.browser.url.startswith(context.get_url('/accounts/login'))
