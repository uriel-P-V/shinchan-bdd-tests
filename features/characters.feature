Feature: Shinchan Characters API

  Background:
    Given the Characters API is available

  @smoke
  Scenario: GET character list
    When I request characters with anime ID 966
    Then the response status code should be 200

  @regression
  Scenario: Validate that the list has more than 10 characters
    When I request characters with anime ID 966
    Then the list of characters should contain more than 10 items

  @regression
  Scenario: Validate Shinnosuke fields
    When I request characters with anime ID 966
    And I request the character with ID 2951
    Then the character fields should match:
      | fields    | value             |
      | name      | Shinnosuke Nohara |
      | favorites | 1165              |
      | nicknames | Shin-chan          |