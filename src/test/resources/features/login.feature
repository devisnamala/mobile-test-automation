Feature: SauceLabs Login

    Scenario: Login with valid credentials
        Given the user is on the login page
        When the user enters valid login details
        And the user clicks on the login button
        Then the user should log in successfully
