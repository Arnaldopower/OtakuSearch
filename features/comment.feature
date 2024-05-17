Feature: Testing Comment Functionality

#Test for animeComment

  Scenario: User publishes a comment
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "test comment" in Anime
    Then I see the "test comment" has been published

  Scenario: User deletes comment successfully
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "test comment 2" in Anime
    Then I see the "test comment 2" has been published
    Given I erase my comment
    Then I do not see my comment "test comment 2"

  Scenario: User edits comment successfully
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "test comment 3" in Anime
    Then I see the "test comment 3" has been published
    Given I replace my comment with "replace success"
    Then I see the "replace success" has been published

  Scenario: User tries to edit comment of another user:
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "This comment can't be edited by todo " in Anime
    And I logout
    Given Im not logged in
    And I register as user "todo" with password "blackflash69"
    Then I can't edit the comment of sukuna in Anime

  Scenario: User comments in page and deletes his user and now the comment don't exists:
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "When I delete my account, this comment will be deleted" in Anime
    Then I see the "When I delete my account, this comment will be deleted" has been published
    Given I erase my account
    Given Im not logged in
    And I register as user "todo" with password "blackflash69"
    Then I do not see comment "When I delete my account, this comment will be deleted" in Anime

#Test for MangaComment

  Scenario: User publishes a comment
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "test comment" in Manga
    Then I see the "test comment" has been published

  Scenario: User deletes comment successfully
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "test comment 2" in Manga
    Then I see the "test comment 2" has been published
    Given I erase my comment
    Then I do not see my comment "test comment 2"

  Scenario: User edits comment successfully
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "test comment 3" in Manga
    Then I see the "test comment 3" has been published
    Given I replace my comment with "replace success"
    Then I see the "replace success" has been published

  Scenario: User tries to edit comment of another user:
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "This comment can't be edited by todo " in Manga
    And I logout
    Given Im not logged in
    And I register as user "todo" with password "blackflash69"
    Then I can't edit the comment of sukuna in Manga

  Scenario: User comments in page and deletes his user and now the comment don't exists:
    Given Exists a user "sukuna" with password "itadori69"
    And I login as user "sukuna" with password "itadori69"
    Given I publish the comment "When I delete my account, this comment will be deleted" in Manga
    Then I see the "When I delete my account, this comment will be deleted" has been published
    Given I erase my account
    Given Im not logged in
    And I register as user "todo" with password "blackflash69"
    Then I do not see comment "When I delete my account, this comment will be deleted " in Manga
