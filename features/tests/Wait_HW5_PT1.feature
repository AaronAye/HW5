Feature: Test Scenarios for Target Search

  Scenario: Verify Target search results
    Given Open Target main page
    When Enter search for item Coffee
    When Add item to cart
    Then Verify search item in cart
