Feature: Jules forgot password tests
  #se ruleaza inainte de fiecare test
  Background:
    Given sign_in: I am a user on Jules sign in page

  @cartof
  Scenario: Wrong email validation message
    When sign_in: I click the forgot password link
    When forgot_pass: I set my email to "abcd"
    Then forgot_pass: I verify that the email validation is correct

  @cartof
  Scenario Outline: Wrong email validation message with table data
    When sign_in: I click the forgot password link
    When forgot_pass: I set my email to "<email>"
    Then forgot_pass: I verify that the email validation is correct

    Examples:
      | email           |
      | abcde.com       |
      | test.com        |
      | test2.com       |
      | test3.com       |