Feature: Testing API for Page Content

  Scenario: Test GET list (response keys):
    When I make get request to /api/string-list
    Then I should get list results with following keys
	    | keys         |
	    | string_list  |

  Scenario: Test GET search (response keys):
    When I make get request to /api/string-list/search/test
    Then I should get detail results with following keys
	    | keys         |
	    | string_list  |
	    | word         |
	    | similar_word |
