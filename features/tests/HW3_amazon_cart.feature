# Created by rkshe at 2/20/2023
Feature: Test scenario for amazon cart


  Scenario: user sees text Your Amazon Cart is empty when clicked on Cart
    Given open amazon page
    When click on cart
    Then verify that text Your Amazon Cart is empty shown


  Scenario: amazon cart has a product
    Given open amazon page
    When click on cart
    Then verify that text Your Amazon Cart is empty shown