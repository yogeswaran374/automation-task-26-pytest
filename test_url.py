import pytest
from test_data import test_data
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class Test_Automation_pytest:
    url = "https://www.imdb.com/search/name/"
    @pytest.fixture()
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    def test_url(self, booting_function):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            assert self.driver.current_url == "https://www.imdb.com/search/name/"
            print ("success: correct url")

            name = self.driver.find_element(By.XPATH, test_data.TestSelectors.name)
            name.click()
            wait = WebDriverWait(self.driver, 10)
            name_box = wait.until(EC.visibility_of_element_located((By.XPATH,test_data.TestSelectors.name_box)))
            name_box.send_keys(test_data.TestData.name_box)


            # birth_date = self.driver.find_element(By.XPATH, test_data.TestSelectors.birth_date)
            # birth_date.click()
            # wait = WebDriverWait(self.driver, 10)
            # birth_date_from = wait.until(EC.visibility_of_element_located((By.XPATH,test_data.TestSelectors.birth_date_from)))
            # birth_date_from.send_keys(test_data.TestData.birth_date_from)
            # birth_date_to = self.driver.find_element(By.XPATH,test_data.TestSelectors.birth_date_to)
            # birth_date_to.send_keys(test_data.TestData.birth_date_to)


            # filling birthday box
            # birthday = self.driver.find_element(By.XPATH, test_data.TestSelectors.birthday)
            # birthday.click()
            # birthday_box = self.driver.find_element(By.XPATH, test_data.TestSelectors.birthday_box)
            # birthday_box.send_keys(test_data.TestData.birthday_box)


            # Awards & recognition
            # wait = WebDriverWait(self.driver, 10)
            # awards_and_recognition = wait.until(
            # EC.visibility_of_element_located((By.XPATH, test_data.TestSelectors.awards_and_recognition)))
            # awards_and_recognition.click()
            #
            # awards_and_recognition_1 = self.driver.find_element(By.XPATH,test_data.TestSelectors.awards_and_recognition_1)
            # awards_and_recognition_2 = self.driver.find_element(By.XPATH,test_data.TestSelectors.awards_and_recognition_2)
            # awards_and_recognition_1.click()
            # awards_and_recognition_2.click()
            #
            # # page topics
            # page_topics = self.driver.find_element(By.XPATH, test_data.TestSelectors.page_topics)
            # page_topics.click()
            # page_topics_1 = self.driver.find_element(By.XPATH, test_data.TestSelectors.page_topics_1)
            # page_topics_2 = self.driver.find_element(By.XPATH, test_data.TestSelectors.page_topics_2)
            # page_topics_1.click()
            # page_topics_2.click()
            # wait = WebDriverWait(self.driver, 10)
            # dropdown_element = wait.until(EC.element_to_be_clickable((By.ID, test_data.TestSelectors.dropdown_element)))
            # dropdown = Select(dropdown_element)
            # dropdown.select_by_value(test_data.TestData.placeholder)
            # placeholder = self.driver.find_element(By.ID, test_data.TestSelectors.placeholder)
            # placeholder.send_keys(data.test_TestData.placeholder)
            #
            # # death date
            # death_date = self.driver.find_element(By.XPATH, test_data.TestSelectors.death_date)
            # death_date.click()
            # wait = WebDriverWait(self.driver, 10)
            # death_date_from = wait.until(
            # EC.visibility_of_element_located((By.XPATH, test_data.TestSelectors.death_date_from)))
            # death_date_from.send_keys(test_data.TestData.death_date_from)
            # death_date_to = self.driver.find_element(By.XPATH, test_data.TestSelectors.death_date_to)
            # death_date_to.send_keys(test_data.TestData.death_date_to)
            #
            # # general identity
            # general_identity = self.driver.find_element(By.XPATH,test_data.TestSelectors.general_identity)
            # general_identity.click()
            # general_identity_1 = self.driver.find_element(By.XPATH, test_data.TestSelectors.general_identity_1)
            # general_identity_1.click()
            #
            # # credit
            # credit = self.driver.find_element(By.XPATH, test_data.TestSelectors.credit)
            # credit.click()
            # wait = WebDriverWait(self.driver, 10)
            # credit_box = wait.until(EC.visibility_of_element_located(
            # (By.XPATH, test_data.TestSelectors.credit_box)))
            # credit_box.send_keys(test_data.TestData.credit)
            #
            # # adult names radio button
            # adult_names = self.driver.find_element(By.XPATH, test_data.TestSelectors.adult_names)
            # adult_names.click()
            # adult_names_radio_button = self.driver.find_element(By.XPATH, test_data.TestSelectors.adult_names_radio_button)
            # adult_names_radio_button.click()

            search_button = self.driver.find_element(By.XPATH, test_data.TestSelectors.search_button)
            search_button.click()


            assert self.driver.current_url == "https://www.imdb.com/search/name/?name=yogeswaran"
            print("script is working successfully")
        except:
            print("failing: error occered")






