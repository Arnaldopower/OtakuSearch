Feature: Testing Comment Functionality

  Scenario: User publishes a comment
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "test comment"
    Then I see the "test comment" has been published

  Scenario: User deletes comment successfully
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "test comment 2"
    Then I see the "test comment 2" has been published
    Given I erase my comment
    Then I do not see my comment "test comment 2"

  Scenario: User edits comment successfully
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "test comment 3"
    Then I see the "test comment 3" has been published
    Given I replace my comment with "replace success"
    Then I see the "replace success" has been published