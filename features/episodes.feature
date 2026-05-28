Feature: Shinchan Episodes API

  Background:
    Given the Episodes API is available

  @smoke
  Scenario: GET episodes
    When I request episodes with anime ID 966
    Then the response status code should be 200

  @regression
  Scenario: Validate fields from episode 1
    When I request episodes with anime ID 966
    And I request episode 1
    Then the episode fields should match:
      | fields | value                                                 |
      | mal_id | 1                                                     |
      | title  | Running an Errand / Mom's Mornings are Busy / Drawing |


  @regression
  Scenario: Validate that the first episode is not a filler
    When I request episodes with anime ID 966
    And I request episode 1
    Then the episode should not be filler
