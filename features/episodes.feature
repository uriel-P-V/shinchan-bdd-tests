Feature: Shinchan Episodes API

Background:
        Given the Episodes API is availabled
    @smoke
    Scenario: GET espisodes
        When I request episodes with anime ID 966
        Then the response status code should be 200

    @regression
    Scenario: validate fields from episode 1
        When I request episodes with anime ID 966 
        And I request episode 1
        Then the response should contain the fields:
            |fields |value                                                 |
            |mal_id |1                                                     |
            |title  |Running an Errand / Mom's Mornings are Busy / Drawing |
            |score  |4.07                                                  |            
    
    @regression
    Scenario: validate that the first episode is not a filler
        When I request episodes with anime ID 966
        And I request episode 1
        Then the episode should not be filler