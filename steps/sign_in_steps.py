from behave import *


# Given, When, And, But, Then -> Gherkin Syntax
# Given = seteaza situatia curenta
# When = defineste pasi din test
# Then = efectueaza verificarea testului

@Given('sign_in_page: I am a user on Jules App')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()


@When('sign_in_page: I set my email to "{email_correct}"')
def step_impl(context, email_correct):
    context.sign_in_page.set_email(email_correct)


@When('sign_in_page: I set my password to "{pwd}"')
def step_impl(context, pwd):
    context.sign_in_page.set_pwd(pwd)


@When('sign_in_page: I verify correct url')
def step_impl(context):
    context.sign_in_page.verify_url_sign_in()


@When('sign_in_page: I click the login button')
def step_impl(context):
    context.sign_in_page.click_login_button()


@When('sign_in_page: I click the forgot password link')
def step_impl(context):
    context.sign_in_page.clik_forgot_pwd_link()


@When('sign_in_page: I verify if message is displayed!')
def step_impl(context):
    context.sign_in_page.verify_display_invalid_email()


@Then('sign_in_page: I verify if url is correct')
def step_impl(context):
    context.sign_in_page.verify_url_message()


@Then('sign_in_page: I verify if button is enabled')
def step_impl(context):
    context.sign_in_page.verify_enable_button()
