Feature: Testing Login Functionality

  Scenario: User logs in successfully
    Given I login as user "sukuna" with password "itadori69"
    Then I should see the "Top" page