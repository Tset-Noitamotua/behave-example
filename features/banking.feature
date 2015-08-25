Feature: Actions with customers and accounts

  Scenario: create a new customer
    Given we have a new customer
    Then the customer should have 0 accounts

  Scenario: add an account
    Given we have a new customer
    When we add a new account
    Then the customer should have 1 accounts
    And the account should have 0 balance

  Scenario Outline: deposit some money
    Given we have a new customer
    When we add a new account
    And we deposit <some money> to the account
    Then the account should have <some money> balance
    Examples: Deposits
      | some money |
      |  10.50     |
      |  55.50     |
      | 100.00     |

  Scenario Outline: withdraw some money
    Given we have a new customer
    And we have 200 in the account
    When we withdraw <some money> from the account
    Then the account should have <leftover balance> balance
    Examples: Withdrawals
      | some money | leftover balance |
      |  10.50     | 189.50           |
      |  55.50     |  44.50           |
      | 100.00     | 100.00           |

  Scenario: withdraw more money than available
    Given we have a new customer
    And we have 200 in the account
    When we withdraw 300 from the account
    Then the withdrawal should fail with "Not enough money in the account."

  Scenario: close an account
    Given we have a new customer
    When we add a new account
    And we close the account
    Then the account should be closed

  @wip
  Scenario: close an account with non-zero balance
    Given we have a new customer
    And we have 100 in the account
    When we close the account
    Then the closing should fail with "Account has a non-zero balance."
