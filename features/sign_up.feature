Feature: Jules sign up tests

  Background:
    Given sign_up_page: I am a user on Jules sign up page

#  @pireu
#  Scenario: Wrong email validation message!
#    When sign_up_page: I verify if I am on the correct page
#    When sign_up_page: I click on the selection of the person
#    When sign_up_page: I click the continue1 button
#    When sign_up_page: I set my first name to "<first_name>"
#    When sign_up_page: I set my last name to "<last_name>"
#    When sign_up_page: I set my email to "<email>"
#    Then sign_up_page: I verify if message wrong email is displayed!
  @pireu
  Scenario Outline: Complete with email validation message!
    When sign_up_page: I verify correct url
    When sign_up_page: I click on the selection of the person
    When sign_up_page: I click the continue1 button
    When sign_up_page: I set my first name to "<first_name>"
    When sign_up_page: I set my last name to "<last_name>"
    When sign_up_page: I set my email to "<email>"
    When sign_up_page: I set correct email to "<email_correct>"
    Then sign_up_page: I verify if message wrong email is displayed after input correct email!

    Examples:
      | first_name |   last_name |    email      |  email_correct      |
      | Mihail     |   Ilut      |    last_name  |  last_name@mail.com |
      | Vasile     |   Pop       |    sasda      |  sasda@mail.com     |
#      | Paul       |   Camataru  |    dadasdsa   |  dadasdsa@mail.com  |
#      | Iulia      |   Parizel   |    para_mar   |  para_mar@mail.com  |