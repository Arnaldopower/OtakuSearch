from behave import *

use_step_matcher("parse")


@given('I publish the comment "{comment}" in Anime')
def step_impl(context, comment):
    context.browser.visit(context.get_url('/entry/anime/52991/'))
    context.browser.is_element_present_by_id('create-ta', wait_time=4)
    context.browser.find_by_id('create-ta').fill(comment)
    context.browser.find_by_id('submit_comment').click()


@given('I publish the comment "{comment}" in Manga')
def step_impl(context, comment):
    context.browser.visit(context.get_url('/entry/manga/2/'))
    context.browser.is_element_present_by_id('create-ta', wait_time=4)
    context.browser.find_by_id('create-ta').fill(comment)
    context.browser.find_by_id('submit_comment').click()


@given("I erase my comment")
def step_impl(context):
    context.browser.find_by_id('delete_comment').click()


@given('I replace my comment with "{new_comment}"')
def step_impl(context, new_comment):
    context.browser.find_by_id('edit-btn').click()
    context.browser.is_element_present_by_id('edit-ta', wait_time=2)
    context.browser.find_by_id('edit-ta').fill(new_comment)
    context.browser.find_by_id('edit_submit').click()


@then('I see the "{comment}" has been published')
def step_impl(context, comment):
    assert context.browser.find_by_text(comment)


@then('I do not see my comment "{comment}"')
def step_impl(context, comment):
    assert context.browser.is_element_not_present_by_text(comment, wait_time=4)


@then("I can't edit the comment of sukuna in Anime")
def step_impl(context):
    context.browser.visit(context.get_url('/entry/anime/52991/'))
    assert not context.browser.is_element_present_by_id('edit-ta', wait_time=4)


@then('I do not see comment "{comment}" in Anime')
def step_impl(context, comment):
    context.browser.visit(context.get_url('/entry/anime/52991/'))
    assert context.browser.is_element_not_present_by_text(comment)


@then('I do not see comment "{comment}" in Manga')
def step_impl(context, comment):
    context.browser.visit(context.get_url('/entry/manga/2/'))
    assert context.browser.is_element_not_present_by_text(comment)


@then("I can't edit the comment of sukuna in Manga")
def step_impl(context):
    context.browser.visit(context.get_url('/entry/manga/2/'))
    assert not context.browser.is_element_present_by_id('edit-ta', wait_time=4)
