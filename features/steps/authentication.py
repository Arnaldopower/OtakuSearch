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
    assert context.browser.is_text_present('Top')

@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url(''))
    assert context.browser.is_text_present('login')

@then('Server responds with page containing "{message}"')
def step_impl(context, message):
    assert context.browser.is_text_present(message)

@then('There is "{link_text}" link available')
def step_impl(context, link_text):
    assert context.browser.is_element_present_by_xpath('//a[text()="'+link_text+'"]')

@then('There is no "{link_text}" link available')
def step_impl(context, link_text):
    assert context.browser.is_element_not_present_by_xpath('//a[text()="'+link_text+'"]')

@then("I'm redirected to the login form")
def step_impl(context):
    assert context.browser.url.startswith(context.get_url('login'))


@then('I should see the "Top" page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the "Top" page')