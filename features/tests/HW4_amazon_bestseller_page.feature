# Created by rkshe at 2/28/2023
Feature: Amazon Best Seller Page header links

  Scenario: Best Seller page has correct amount of header links
    Given open amazon page
    When click on Best Seller link
    Then verify Best Seller page has 5 header links
