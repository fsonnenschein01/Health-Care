from selenium import webdriver
from selenium.webdriver.common.by import By

class TestOnlinePharmacy:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")
    
    def test_home_page(self):
        assert "HealthCare" in self.driver.title
    
    def test_search_functionality(self):
        search_box = self.driver.find_element(By.NAME, "query")
        search_box.send_keys("Эссенциале")
        search_box.submit()
        assert "Эссенциале" in self.driver.page_source
    
    def teardown_method(self):
        self.driver.quit()
