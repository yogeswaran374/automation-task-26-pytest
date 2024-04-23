class TestData:

    name_box = "yogeswaran"
    birth_date_from = "1997-08"
    birth_date_to = "2024-04"
    birthday_box = "08-15"
    placeholder = "arrested"
    death_date_from = "1997-08"
    death_date_to = "2024-04"
    credit = "80"

class TestSelectors:

    name = '//*[@id="nameTextAccordion"]/div[1]/label/span[1]/div'
    name_box = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input'
    birth_date = '//*[@id="birthDateAccordion"]/div[1]/label/span[1]/div'
    birth_date_from = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/input'
    birth_date_to = '/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/input'
    birthday = '//*[@id="birthdayAccordion"]/div[1]/label/span[1]/div'
    birthday_box = '//input[@aria-label="Enter birthday"]'
    awards_and_recognition = '//*[@id="awardsAccordion"]/div[1]/label/span[1]/div'
    awards_and_recognition_1 = '//button[@data-testid="test-chip-id-oscar_best_actor_nominees"]'
    awards_and_recognition_2 = '//button[@data-testid="test-chip-id-oscar_best_actress_winners"]'
    page_topics = '//*[@id="pageTopicsAccordion"]/div[1]/label/span[1]/div'
    page_topics_1 = '//button[@data-testid="test-chip-id-AWARD_NOMINATIONS"]'
    page_topics_2 ='//button[@data-testid="test-chip-id-BIOGRAPHY"]'
    dropdown_element = "within-topic-dropdown-id"
    placeholder = '//input[@placeholder="e.g. Arrested"]'
    death_date = '//*[@id="deathDateAccordion"]/div[1]/label/span[1]/div'
    death_date_from = '//input[@data-testid="deathYearMonth-start"]'
    death_date_to = '//input[@data-testid="deathYearMonth-end"]'
    general_identity = '//*[@id="genderIdentityAccordion"]/div[1]/label/span[1]/div'
    general_identity_1 = '//button[@data-testid="test-chip-id-MALE"]'
    credit ='//*[@id="filmographyAccordion"]/div[1]/label/span[1]/div'
    credit_box = '//input[@data-testid="autosuggest-input-test-id-filmography"]'
    adult_names = '//*[@id="adultNamesAccordion"]/div[1]/label/span[1]/div'
    adult_names_radio_button = '//input[@id="include-adult-names"]'
    search_button = '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button/span'