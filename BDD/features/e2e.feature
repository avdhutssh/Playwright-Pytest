Feature: E-Commerce API and UI Integration

  Scenario: Create order via API and verify it in UI
    Given I am logged into the application with valid credentials
    When I select the product "ZARA COAT 3" for viewing
    And I retrieve the product ID
    And I verify the product is visible
    And I navigate to orders page
    And I delete all existing orders
    And I verify no orders are present
    And I create an order via API using the product ID
    And I navigate back to login page
    And I navigate to orders page
    Then I should see my order in the orders list
    And I can view the order details
    And I should see the thank you message 