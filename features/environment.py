from splinter import Browser


def before_all(context):
    context.browser = Browser('edge', headless=True)


def after_all(context):
    context.browser.quit()
    context.browser = None
