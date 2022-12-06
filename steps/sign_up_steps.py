from behave import *


@Given('sign_up_page: I am a user on Jules sign up page')
def step_impl(context):
    context.sign_up_page.navigate_to_sign_up_page()


@When('sign_up_page: I click the sign up button')
def step_impl(context):
    context.sign_up_page.click_sign_up_button()


@When('sign_up_page: I click on the selection of the person')
def step_impl(context):
    context.sign_up_page.select_person()


@When('sign_up_page: I click the continue1 button')
def step_impl(context):
    context.sign_up_page.click_continue_button1()


@When('sign_up_page: I set my first name to "{first_name}"')
def step_impl(context, first_name):
    context.sign_up_page.set_first_name(first_name)


@When('sign_up_page: I set my last name to "{last_name}"')
def step_impl(context, last_name):
    context.sign_up_page.set_last_name(last_name)


@When('sign_up_page: I set my email to "{email}"')
def step_impl(context, email):
    context.sign_up_page.set_email(email)


@When('sign_up_page: I set correct email to "{email_correct}"')
def step_impl(context, email_correct):
    context.sign_up_page.complete_correct_email(email_correct)


@When('sign_up_page: I verify if I am on the correct page')
def step_impl(context):
    context.sign_up_page.verify_url_sign_up()


@When('sign_up_page: I verify correct url')
def step_impl(context):
    context.sign_up_page.verify_url_sign_up()


@Then('sign_up_page: I verify if message wrong email is displayed!')
def step_impl(context):
    context.sign_up_page.verify_display_invalid_email()


@Then('sign_up_page: I verify if message wrong email is displayed after input correct email!')
def step_impl(context):
    context.sign_up_page.verify_display_invalid_email1()
