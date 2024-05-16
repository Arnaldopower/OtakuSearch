from behave import *

use_step_matcher("parse")


@then('I see the "{comment}" has been published')
def step_impl(context, comment):
    context.browser.find_by_text(comment)


@given('I publish the comment "{comment}"')
def step_impl(context, comment):
    context.browser.visit(context.get_url('/entry/anime/52991/'))
    context.browser.is_element_present_by_id('create-ta', wait_time=4)
    context.browser.find_by_id('create-ta').fill(comment)
    context.browser.find_by_id('submit_comment').click()


@given("I erase my comment")
def step_impl(context):
    context.browser.find_by_id('delete_comment').click()


@then('I do not see my comment "{comment}"')
def step_impl(context, comment):
    context.browser.is_element_not_present_by_text(comment, wait_time=4)


@given('I replace my comment with "{new_comment}"')
def step_impl(context, new_comment):
    context.browser.find_by_id('edit-btn').click()
    context.browser.is_element_present_by_id('edit-ta', wait_time=2)
    context.browser.find_by_id('edit-ta').fill(new_comment)
    context.browser.find_by_id('edit_submit').click()
