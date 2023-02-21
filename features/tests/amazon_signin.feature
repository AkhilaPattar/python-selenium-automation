# Created by rkshe at 2/20/2023
Feature: Test scenario for Sign in page when clicked on Returns&Orders

  Scenario: Logged out User sees the Sign in page when clicked on Returns&Orders
    Given open amazon page
    When click on Returns&Orders
    Then verify Amazon Sign in page is shown