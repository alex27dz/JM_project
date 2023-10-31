from chromedriver_py import binary_path as chromeBinary
from selenium.webdriver.chrome.service import Service
from Generic_functions_modules import *

chrome_location = '/Users/alexdezho/Documents/Personal/chromedriver'  # Google Chrome webdriver location
chromeService_obj = Service(chromeBinary)
ie_location = "C:/ChromeDriver/IEDriverServer"
firefox_location = 'H:/Public/Alex_D_Framework/FireFoxDriver'
edge_location = "C:/ChromeDriver/msedgedriver"
tag = 'chrome'
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"


def test_01_HomePageToPersonalInsurance():
    print('\nworking with Chrome')
    driver = webdriver.Chrome(chrome_location)
    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Personal Insurance')
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Personal Insurance').click()
    time.sleep(10)
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 01 - PASSED')
    driver.close()

def test_02_HomePageToGetaQuote():
    print('\nworking with Chrome')
    driver = webdriver.Chrome(chrome_location)
    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access GetaQuote')
    url = '/jewelry-engagement-ring-insurance-quote'
    driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Get a Quote').click()
    time.sleep(10)
    assert str(get_a_quote_body_validation(driver)) == 'True', 'Body elements of Get a Quote - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 02 - PASSED')
    driver.close()






