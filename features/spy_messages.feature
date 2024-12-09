Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    And I enter the Caesar Shift as 1
    And I enter the message "Coding is fun!"
    When I click the Translate button
    Then I should see the message "Frglqj lv ixq!"

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    And I enter the Caesar Shift as 1
    And I enter the method as D
    And I enter the message "Frglqj lv ixq!"
    When I click the Translate button
    Then I should see the decoded message "Coding is fun!"
