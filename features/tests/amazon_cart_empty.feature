# Created by rkshe at 2/20/2023
Feature: Test scenario for your amazon cart is empty when user click on cart


  Scenario: user sees text Your Amazon Cart is empty when clicked on Cart
    Given open amazon page
    When click on cart
    Then verify that text Your Amazon Cart is empty shown