Feature: Shinchan Characters API

    Background:
            Given the Characters API is available
            
    @smoke
    Scenario: GET character list
        when I request characters with anime ID 966
        Then the response status code should be 200
        
    @regression
    Scenario: validate that the list has more than 10 characters
        When I request characters with anime ID 966
        Then the list of characters should contain more than 10 items
    
    @regression
    Scenario: Validate Shinnosuke fields
        when I request characters with anime ID 966
        And I request the character with ID 2951
        then the response should contain the fields:
            |fields   |value             |
            |name     |Shinnosuke Nohara |
            |favorites|1165              |
            |nicknames|Shin-chan         |