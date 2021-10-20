from selenium import webdriver
import unittest

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        self.driver = webdriver.Chrome()

    def test_addition(self):
        self.driver.get("C:/Users/prati/PycharmProjects/pythonProject4/calculator.html")
        self.driver.find_element_by_name("5").click()
        self.driver.find_element_by_name("+").click()
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("=").click()
        value = self.driver.find_element_by_id("result").get_attribute("value")
        print(value)
        self.assertEqual('13', value)

    def test_substraction(self):
        self.driver.get("C:/Users/prati/PycharmProjects/pythonProject4/calculator.html")
        self.driver.find_element_by_name("5").click()
        self.driver.find_element_by_name("-").click()
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("=").click()
        value = self.driver.find_element_by_id("result").get_attribute("value")
        print(value)
        self.assertEqual('-3', value)

    def test_division(self):
        self.driver.get("C:/Users/prati/PycharmProjects/pythonProject4/calculator.html")
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("/").click()
        self.driver.find_element_by_name("2").click()
        self.driver.find_element_by_name("=").click()
        value = self.driver.find_element_by_id("result").get_attribute("value")
        print(value)
        self.assertEqual('4', value)

    def test_multiplication(self):
        self.driver.get("C:/Users/prati/PycharmProjects/pythonProject4/calculator.html")
        self.driver.find_element_by_name("5").click()
        self.driver.find_element_by_name("*").click()
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("=").click()
        value = self.driver.find_element_by_id("result").get_attribute("value")
        print(value)
        self.assertEqual('40', value)

    def tearDown(self):
            #close the browser window
            self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)