Feature: Shinchan Anime API

  Background:
    Given the Shinchan API is available

  @smoke
  Scenario: GET anime by ID
    When I request the anime with ID 966
    Then the response status code should be 200

  @regression
  Scenario: Validate basic anime fields
    When I request the anime with ID 966
    Then the response should contain the fields:
      | field  |
      | title  |
      | score  |
      | status |

  @regression
  Scenario: Validate that genres contain Comedy
    When I request the anime with ID 966
    Then the genres should contain "Comedy"

  @regression
  Scenario: Validate that studios contain Shin-Ei Animation
    When I request the anime with ID 966
    Then the studios should contain "Shin-Ei Animation"


