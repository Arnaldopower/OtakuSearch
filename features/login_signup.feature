Feature: Testing Login and Signup Functionality

  Scenario: User logs in successfully
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Then Im in home

  Scenario: User signs up successfully
    Given Im not logged in
    And I register as user "todo" with password "blackflash69"
    Then Im in home

  Scenario: User returns to login successfully
    Given Im not logged in
    And Im going to register but i remember my user and password
    Then Im back at login

  Scenario: User logs out successfully
    Given Exists a user "manolito" with password "gafotas69"
    And I login as user "manolito" with password "gafotas69" 
    And I logout
    Then Im back at login

  Scenario: User deletes account successfully
    Given Exists a user "manolo" with password "skibiditoilet69"
    And I login as user "manolo" with password "skibiditoilet69" 
    And I erase my account
    Then Im back at login