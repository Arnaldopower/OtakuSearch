Feature: Testing Login Functionality

  Scenario: User logs in successfully
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Then Im in home

  Scenario: User signs up successfully
    Given Im not logged in
    And I register as user "todo" with password "blackflash69"
    Then Im in home