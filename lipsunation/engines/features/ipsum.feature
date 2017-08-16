Feature: Generate Lorem Ipsum
    # In order to test my awesome software
    # I need an awesome BDD tool like radish
    # to test my software.
    Scenario: get paragraph
        Given I want to generate lorem ipsum
        When I choose 1 paragraphs(s)
        Then I expect the result have 1 paragraph(s)

    Scenario: get mutliple paragraphs
        Given I want to generate lorem ipsum
        When I choose 5 paragraphs(s)
        Then I expect the result have 5 paragraph(s)
