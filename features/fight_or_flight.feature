Feature: Fight or Flight


  Scenario Outline: Fight or Flight (<hiptest-uid>)
    Given the ninja has a ""
    When attacked by  ""
    Then the ninja should ""

    Examples:
      | achievement_level | opponent_role | reaction | hiptest-uid |
      | third level black-belt | samurai | engage the opponent |  |
      | third level black-belt | Chuck Norris | run for his life |  |
