Feature: Jules sign in tests

  Background:
    Given sign_in_page: I am a user on Jules App

  @cartabos
  Scenario Outline: Verify button is disable
    When sign_in_page: I verify correct url
    When sign_in_page: I set my email to "<email_correct>"
    When sign_in_page: I verify if message is displayed!
    Then sign_in_page: I verify if url is correct





          Examples:
      | first_name |   last_name |    email      |  email_correct      |
      | Mihail     |   Ilut      |    last_name  |  last_name@mail.com |
      | Vasile     |   Pop       |    sasda      |  sasda@mail.com     |
#      | Paul       |   Camataru  |    dadasdsa   |  dadasdsa@mail.com  |
#      | Iulia      |   Parizel   |    para_mar   |  para_mar@mail.com  |