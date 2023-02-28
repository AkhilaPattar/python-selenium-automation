# Created by rkshe at 2/28/2023
Feature: user can add the product to cart and verify its there

   Scenario: user can search for sofa on amazon
    Given open amazon page
    When input text dress
    When click on search button
    When click on the first product price
    When click on Add to cart button
    When click on cart
    Then verify that 1 item is shown in the cart