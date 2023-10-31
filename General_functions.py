import datetime
import json  # working with json dicts
import logging
import pprint
import time
import urllib.request
from datetime import date
import pytest
import requests
from requests.structures import CaseInsensitiveDict
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


chrome_location = '/Users/alexdezho/Documents/Personal/chromedriver'  # Google Chrome webdriver location
google_search_tab = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
# adding test_ before the function name to make it a test readable by pytest


# JM website
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"

# Drivers location
# chrome_location = '/Users/alexdezho/Documents/Personal/chromedriver'
firefox_location = 'executable_path="C:\\geckodriver.exe"'
ie_location = "C:/IEDriver/IEDriverServer/IEDriverServer"
edge_location = "C:/msedgedriver"

# environment links
qna_regular_QA7 = 'http://mytest07.jewelersnt.local/jewelry-insurance-quote-apply/t/Pa_sa8WRd0W_k02oCEi6cQ'
gw_policy_center_QA7 = 'http://jmtgpc07/pc/PolicyCensuter.do'
qna_internal_QA7 = 'http://jmtapp07/QuoteApply/Internal'
qna_regular_QA4 = 'http://mytest04.jewelersnt.local/jewelry-insurance-quote-apply/'
gw_policy_center_QA4 = 'http://jmtgpc04/pc/PolicyCenter.do'
qna_internal_QA4 = 'http://jmtapp04/QuoteApply/Internal'

# Items dictionary
item = {
    "Ring": "jewelry-itemType-1",
    "Earrings": "jewelry-itemType-2",
    "Bracelet": "jewelry-itemType-3",
    "Necklace": "jewelry-itemType-4",
    "Watch": "jewelry-itemType-5",
    "Pendant": "jewelry-itemType-6",
    "Chain": "jewelry-itemType-7",
    "Other": "jewelry-itemType-8",
    "Loose stone": "jewelry-itemType-9",
    "Brooch": "jewelry-itemType-10"
}

# adding test_ before the function name to make it a test readable by pytest


# example 1 - simple scenario
def regular_test_scenario():
    driver = webdriver.Chrome(chrome_location)
    driver.get('https://google.com/')
    driver.maximize_window()
    time.sleep(3)
    googlesearch = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'  # search element
    driver.find_element_by_xpath(googlesearch).click()
    driver.find_element_by_xpath(googlesearch).send_keys('Michael is the best developer')
    driver.find_element_by_xpath(googlesearch).send_keys(Keys.ENTER)
    time.sleep(5)
    driver.close()
    print('first example')

# example 2 - simple scenario as a pytest function
def t01_itsmyfirsttest():
    driver = webdriver.Chrome(chrome_location)
    driver.get('https://google.com/')
    driver.maximize_window()
    time.sleep(3)
    driver.close()
    print('second example')

# example 3 - simple scenario as a pytest function using regular function
def t2_itsmysecondtest():
    regular_test_scenario()  # calling the function
    print('third example')
def michael_function():
    print('I am michaels function')
def t1_function_michael():
    michael_function()
    driver = webdriver.Chrome(chrome_location)  # web driver location
    driver.get('https://google.com/')
    # first validation
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath(google_search_tab).click()  # clicking on any element on the page
    time.sleep(2)
    driver.find_element_by_xpath(google_search_tab).send_keys('michael')  # typing inside the window
    time.sleep(2)
    driver.find_element_by_xpath(google_search_tab).send_keys(Keys.ENTER)
    # second validation
    assert driver.current_url == 'https://google.com/'  # clicking enter keyboard
    driver.close()

# Executing the regular function in a regular run mode
# regular_test_scenario()

def navbar_validation(driver):
    driver.execute_script("window.scrollTo(0,0)")
    print('verifying Navbar containers')
    url = '/jewelry-engagement-ring-insurance-quote'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="'+url+'"]')))
    print('Navbar Personal')

    if driver.current_url == 'https://stage.jewelersmutualalex.com/':
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Personal Insurance').text)
        print(driver.find_element_by_link_text('Get a Quote').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Manage My Policy').text)
        print(driver.find_element_by_link_text('Blog').text)
        print('Navbar Personal passed')

        print('Navbar Business')
        url = '/jewelry-business-jewelers-block-bop-insurance'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Business Insurance').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print(driver.find_element_by_link_text('JM Shipping Solution').text)
        print(driver.find_element_by_link_text('JM Care Plan').text)
        print(driver.find_element_by_link_text('Jeweler Programs').text)
        print(driver.find_element_by_link_text('Pawnbrokers').text)
        print('Navbar Business passed')

        print('Navbar Answers')
        url = '/jewelry-insurance-101'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('Jewelry Insurance 101').text)
        print(driver.find_element_by_link_text('FAQ').text)
        print('Navbar Answers passed')

        print('Navbar About Us')
        url = '/about-us'
        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
        time.sleep(2)
        print(driver.find_element_by_link_text('About Us').text)
        print(driver.find_element_by_link_text('Social Responsibility').text)
        print(driver.find_element_by_link_text('Careers').text)
        print(driver.find_element_by_link_text('Newsroom').text)
        print('Navbar About Us passed')

        print('Navbar Log In')
        try:
            driver.find_element_by_xpath('//a[contains(@href,"https://my.jewelersmutual.com/PLPortal/Security/")]').click()
            time.sleep(2)
        except:
            driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-main-menu"]/ul/div/li[5]/a').click()
            time.sleep(2)

        print(driver.find_element_by_link_text('Personal Jewelry').text)
        print(driver.find_element_by_link_text('Agent').text)
        print(driver.find_element_by_link_text('Zing Platform').text)
        print('Navbar Log In passed')

    else:
        print('Navbar Personal')
        url = '/jewelry-engagement-ring-insurance-quote'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(3)
        print(driver.find_element_by_link_text('Personal Insurance').text)
        print(driver.find_element_by_link_text('Get a Quote').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Manage My Policy').text)
        print(driver.find_element_by_link_text('Blog').text)
        print('Navbar Personal passed')

        print('Navbar Business')
        url = '/jewelry-business-jewelers-block-bop-insurance'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]') # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('Business Insurance').text)
        print(driver.find_element_by_link_text('Claims').text)
        print(driver.find_element_by_link_text('Pay My Bill').text)
        # print(driver.find_element_by_link_text('Zing Platform').text)
        print(driver.find_element_by_link_text('JM Shipping Solution').text)
        print(driver.find_element_by_link_text('JM Care Plan').text)
        print(driver.find_element_by_link_text('Jeweler Programs').text)
        print(driver.find_element_by_link_text('Pawnbrokers').text)
        print('Navbar Business passed')

        print('Navbar Answers')
        url = '/jewelry-insurance-101'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('Jewelry Insurance 101').text)
        print(driver.find_element_by_link_text('FAQ').text)
        print('Navbar Answers passed')

        print('Navbar About Us')
        url = '/about-us'
        action = webdriver.ActionChains(driver)
        element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        print(driver.find_element_by_link_text('About Us').text)
        print(driver.find_element_by_link_text('Social Responsibility').text)
        print(driver.find_element_by_link_text('Careers').text)
        print(driver.find_element_by_link_text('Newsroom').text)
        print('Navbar About Us passed')


        print('Navbar Log In')
        try:
            url = 'https://my.testjewelersmutual.com/plportal'
            action = webdriver.ActionChains(driver)
            element = driver.find_element_by_xpath('//a[@href="' + url + '"]')  # or your another selector here
            action.move_to_element(element)
            action.perform()
            time.sleep(2)
            print(driver.find_element_by_link_text('Personal Jewelry').text)
            print(driver.find_element_by_link_text('Agent').text)
            print(driver.find_element_by_link_text('Zing Platform').text)
            print('Navbar Log In passed')
        except:
            print('different log in element name due to different link')

    print('Navbar - verified')
    return True
def footer_validation(driver):
    driver.execute_script("window.scrollTo(0,4000)")
    time.sleep(5)

    print('verifying Footer containers')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'block-footerplmenu')))
    element = driver.find_element_by_id('block-footerplmenu')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(2)
    print(element.text)
    print(driver.find_element_by_id('block-footerclmenu').text)
    print(driver.find_element_by_id('block-footerinfomenu').text)
    print(driver.find_element_by_id('block-footercontactmenu').text)
    print(driver.find_element_by_id('block-footerrecommendedcontentlinks').text)
    print('Footer - verified')
    return True
def personal_insurance_body_validation(driver):
    print('Verifying Personal_insurance_Body containers')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'What will it cost me?')]")))

    whatwillitcostmebutton = driver.find_element_by_xpath("//a[contains(text(),'What will it cost me?')]")
    print(whatwillitcostmebutton.text)

    header_howthejewelryinsurance = driver.find_element_by_id('title-4366')
    print(header_howthejewelryinsurance.text)

    actions = ActionChains(driver)
    actions.move_to_element(header_howthejewelryinsurance).perform()

    comparisonTable = driver.find_element_by_class_name('comparison-table__center')
    print(comparisonTable.text)
    print(driver.find_element_by_class_name('table-footer').text)

    whatdoesjewelryinsurancecover = driver.find_element_by_id('title-4331')
    print(whatdoesjewelryinsurancecover.text)

    infogrid_jewelryinsurancecover = driver.find_element_by_id('info-grid-4356')
    print(infogrid_jewelryinsurancecover.text)

    protectingallthings = driver.find_element_by_id('text-image-row-4326')
    print(protectingallthings.text)

    image_whatourpolicyholderssay = driver.find_element_by_id('image-container-8266').is_displayed()
    print(image_whatourpolicyholderssay, " Image is displayed")

    whatourpolicyholderssay = driver.find_element_by_id('title-4361')
    print(whatourpolicyholderssay.text)

    image_checkyourrate = driver.find_element_by_id('image-container-8271').is_displayed()
    print(image_checkyourrate, " Image is displayed")

    checkyourrate = driver.find_element_by_id('feature-row-6476')
    print(checkyourrate.text)

    allthingsjewelryinsurance = driver.find_element_by_id('feature-row-4396')
    print(allthingsjewelryinsurance.text)

    element = allthingsjewelryinsurance
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    print('Personal_insurance_Body - verified')
    return True
def get_a_quote_body_validation(driver):
    print('Verifying Get_A_Quote_Body containers')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "appHeaderContainer")))

    jmlogo = driver.find_element_by_id('HeaderImages').is_displayed()
    print(jmlogo, "JM Logo is displayed")

    header_questions = driver.find_element_by_id('QuestionsContainer')
    print(header_questions.text)

    getyourfreejewelryinsurancequote = driver.find_element_by_id('quoteContainer')
    print(getyourfreejewelryinsurancequote.text)

    element = getyourfreejewelryinsurancequote
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    showmyquotebutton = driver.find_element_by_id('quoteInfoNext')
    print(showmyquotebutton.text)

    rightpanel = driver.find_element_by_id('right-panel')
    print(rightpanel.text)

    footer = driver.find_element_by_id('TermsAndPrivacyFooterContainer')
    print(footer.text)

    element = footer
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)

    print('Get_A_Quote_Body - verified')
    return True
def pay_my_bill_body_validation(driver):
    print('Verifying Get_A_Quote_Body containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jm-logo")))
    jmlogo = driver.find_element_by_class_name('jm-logo').is_displayed()

    if jmlogo:  # checking if it's visible
        print('JM Logo is displayed')
    else:
        print('JM Logo is not displayed')

    quickbillpaybody = driver.find_element_by_id('lookupForm')

    element = quickbillpaybody
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    print(quickbillpaybody.text)
    print(driver.find_element_by_id('continueButton').text)
    print(driver.find_element_by_id('recaptcha').text)
    print(driver.find_element_by_class_name('navbar').text)

    footer = driver.find_element_by_xpath("//div[contains(@class, 'col-md-8 col-sm-6 col-xs-12')]")
    element = footer
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    print(footer.text)

    privacyandterms = driver.find_element_by_xpath("//div[contains(@class, 'col-md-4 col-sm-6 col-xs-12')]")
    print(privacyandterms.text)
    time.sleep(3)

    print('Pay_My_Bill_Body - verified')
    return True
def claims_body_validation(driver):
    print('Verifying claims_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-2801")))

    heroimagecontainer = driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container hero__image-container--no-mobile-image')]")
    print(heroimagecontainer.text)

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]")
    print(herocontent.text)

    bodycontent = driver.find_element_by_xpath("//div[contains(@class, 'layout__region layout__region--content')]")
    print(bodycontent.text)

    whatsneeded = driver.find_element_by_id('title-2801')
    print(whatsneeded.text)

    whatsneededcontent = driver.find_element_by_id('info-grid-2826')
    print(whatsneededcontent.text)

    covid19andyourclaim = driver.find_element_by_id('feature-row-6726')
    print(covid19andyourclaim.text)

    howitallworks = driver.find_element_by_id('title-8256')
    print(howitallworks.text)

    startyourclaim = driver.find_element_by_id('text-image-row-2841')
    print(startyourclaim.text)

    chooseajeweler = driver.find_element_by_id('text-image-row-2846')
    print(chooseajeweler.text)

    payyourdeductible = driver.find_element_by_id('text-image-row-2851')
    print(payyourdeductible.text)

    insureyourreplacementjewelry = driver.find_element_by_id('text-image-row-2856')
    print(insureyourreplacementjewelry.text)

    claimsatisfactionratecontent = driver.find_element_by_id('feature-row-2861')
    print(claimsatisfactionratecontent.text)

    claimsatisfactionrateimage = driver.find_element_by_id('image-container-8276').is_displayed()
    print(claimsatisfactionrateimage, " Image is displayed")

    customersstoriesimage = driver.find_element_by_id('image-container-8281').is_displayed()
    print(customersstoriesimage, " Image is displayed")

    customerstoriestext = driver.find_element_by_id('feature-row-8261')
    print(customerstoriestext.text)

    element = driver.find_element_by_id('feature-row-2861')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    claimsrate = driver.find_element_by_id('feature-row-2861')
    print(claimsrate.text)

    whatisandisntcovered = driver.find_element_by_id('info-grid-2921')
    print(whatisandisntcovered .text)

    faqheader = driver.find_element_by_id('title-4196')
    print(faqheader.text)

    faqcontent = driver.find_element_by_id('accordion')
    print(faqcontent.text)

    startaclaim = driver.find_element_by_id('feature-row-8916')
    print(startaclaim.text)

    element = chooseajeweler
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('Claims_Body - verified')
    return True
def manage_my_policy_body_validation(driver):
    print('verifying manage_my_policy containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    print(driver.find_element_by_id('page-body').text)
    time.sleep(3)
    print('manage_my_policy - verified')
    return True
def blog_body_validation(driver):
    print('verifying blog containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "block-jewelers-mutual-content")))

    bloghero = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(bloghero .text)

    # mostPopularPosts = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-personal-popular-posts')]")
    # print(mostPopularPosts.text)

    # postsByTopic = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-jewelry-box-topics')]")
    # print(postsByTopic.text)

    blogposts = driver.find_element_by_xpath("//div[contains(@class, 'layout__region layout__region--first')]")
    print(blogposts.text)

    time.sleep(3)
    print('blog - verified')
    return True
def answers_JewelryInsurance101_body_validation(driver):
    print('verifying JewelryInsurance101_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-7541")))
    yourguidetojewelryinsurance = driver.find_element_by_id('text-image-row-7541')
    print(yourguidetojewelryinsurance.text)
    yourguidetojewelryinsuranceimage = driver.find_element_by_xpath('//img[@alt="jewelry icon"]')
    print(yourguidetojewelryinsuranceimage, "Image is displayed")
    whatscoveredbyjewelryinsurance = driver.find_element_by_id('related-content-7696')
    print(whatscoveredbyjewelryinsurance.text)
    doineedajewelryappraisal = driver.find_element_by_id('related-content-8221')
    print(doineedajewelryappraisal.text)
    howdoestheclaimsprocessworktitle = driver.find_element_by_id('title-7581')
    print(howdoestheclaimsprocessworktitle.text)
    howdoestheclaimsprocessworktext = driver.find_element_by_id('feature-row-8511')
    print(howdoestheclaimsprocessworktext.text)
    myjewelrystoryvideo = driver.find_element_by_id('text-block-7601').is_displayed()
    print(myjewelrystoryvideo, "Video is displayed")
    quotewidget = driver.find_element_by_id('quote-widget-6401')
    print(quotewidget.text)
    stillhavequestions = driver.find_element_by_id('cta-group-7576')
    print(stillhavequestions.text)
    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(herocontent.text)
    pagenavigationlinks = driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]")
    print(pagenavigationlinks.text)
    element = driver.find_element_by_id('cta-group-7576')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('JewelryInsurance101_Body - verified')
    return True
def answers_FAQ_body_validation(driver):
    print('verifying FAQ_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "views-exposed-form-acquia-search-faq-search")))
    searchbox = driver.find_element_by_id('views-exposed-form-acquia-search-faq-search').is_displayed()
    print(searchbox, "Search box is displayed")
    coverageblock = driver.find_element_by_id('text-block-11376')
    print(coverageblock.text)
    allcoveragequestionsbutton = driver.find_element_by_id('cta-group-9216')
    print(allcoveragequestionsbutton.text)
    appraisalsblock = driver.find_element_by_id('text-block-11391')
    print(appraisalsblock.text)
    allappraisalsquestionsbutton = driver.find_element_by_id('cta-group-9226')
    print(allappraisalsquestionsbutton.text)
    gettingstartedblock = driver.find_element_by_id('text-block-11381')
    print(gettingstartedblock.text)
    allgettingstrtedquestionsbutton = driver.find_element_by_id('cta-group-9221')
    print(allgettingstrtedquestionsbutton.text)
    mypolicyblock = driver.find_element_by_id('text-block-11396')
    print(mypolicyblock.text)
    allpolicyquestions = driver.find_element_by_id('cta-group-9231')
    print(allpolicyquestions.text)
    claimsblock = driver.find_element_by_id('text-block-11386')
    print(claimsblock.text)
    allclaimsquestions = driver.find_element_by_id('cta-group-9236')
    print(allclaimsquestions.text)
    popularquestions = driver.find_element_by_id('info-grid-9246')
    print(popularquestions.text)
    actions = ActionChains(driver)
    actions.move_to_element(allcoveragequestionsbutton).perform()
    actions.click(allcoveragequestionsbutton).perform()
    time.sleep(6)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "block-jewelers-mutual-content")))
    faqcoveragequestions = driver.find_element_by_id('block-jewelers-mutual-content')
    print(faqcoveragequestions.text)
    print('FAQ_Body - verified')
    return True
def login_Personal_Jewelry_body_validation(driver):
    print('verifying Personal_Jewelry_Body containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    print(driver.find_element_by_id('page-body').text)

    time.sleep(3)
    print('Personal_Jewelry_Body - verified')
    return True
def login_agent_body_validation(driver):
    print('verifying agent_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    upperLinks = driver.find_element_by_id('utility')
    print(upperLinks.text)
    lowerLinks = driver.find_element_by_id('utility-nav-contain')
    print(lowerLinks.text)
    siteNavigation = driver.find_element_by_id('site-nav')
    print(siteNavigation.text)
    pageBody = driver.find_element_by_id('page-body')
    print(pageBody.text)
    footerLinks = driver.find_element_by_id('footer-utility-links')
    print(footerLinks.text)
    element = driver.find_element_by_id('footer-utility-links')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('agent_Body - verified')
    return True
def login_ZingPlatform_body_validation(driver):
    print('verifying Zing Platform_Body containers')
    time.sleep(3)

    zingLogo = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[2]/div[1]/img').is_displayed()
    print(zingLogo, "Zing logo is displayed.")

    registerButton = driver.find_element_by_class_name('form-container')
    print(registerButton.text, "form-container")

    loginButton = driver.find_element_by_id('loginbutton')
    print(loginButton.text, "loginbutton")

    raisingTheTide = driver.find_element_by_id('Email')
    print(raisingTheTide.text, "Email")

    backgroundVideo = driver.find_element_by_id('pwdInput').is_displayed()
    print(backgroundVideo, "pwdInput")

    time.sleep(3)
    print('Zing Platform_Body - verified')
    return True
def embedded_quote_Estimatemyrate(driver):
    print('verifying embedded_quote_Body containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "step2")))
    print(driver.find_element_by_id('step2').text)

    # quote content box
    print(driver.find_element_by_xpath("//div[contains(@class, 'estimate content-container--margin-bottom')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'quote-cards-container quote-flex-wrapper')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'summary-total content-container row-quote')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'premium-warning content-container row-quote')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'button-container row-buttons')]").text)

    time.sleep(3)
    print('embedded_quote_Body - verifyied')
    return True
def soapUI(url, body):
    url = "http://jmtsvc04.jewelersnt.local/ExternalPaymentService/ExternalPayment.svc?singleWsdl"
    headers = {"SOAPAction": "http://tempuri.org/IExternalPayment/PaymentNotification",
               "Content-Type": "text/xml; charset=UTF-8"}
    data = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/" xmlns:ns="http://jewelersmutual.com/externalpayment/2016/01">
       <soapenv:Header/>
       <soapenv:Body>
          <tem:PaymentNotification>
             <!--Optional:-->
             <tem:request>
                <!--Optional:-->
                <ns:AccountNumber>3000000013</ns:AccountNumber>
                <!--Optional:-->
                <ns:Amount>254.00</ns:Amount>
                <!--Optional:-->
                <ns:ApplicationName>NEW_BUSINESS</ns:ApplicationName>
                <!--Optional:-->
                <ns:AuthorizationCode>123958783</ns:AuthorizationCode>
                <!--Optional:-->
                <ns:CardInfo>
                   <!--Optional:-->
                   <ns:AutoPay>false</ns:AutoPay>
                 
                   <ns:CreditCardExpDate>2018-04-01T00:00:00</ns:CreditCardExpDate>
                   <!--Optional:-->
                   <ns:CreditCardIssuer>Mastercard</ns:CreditCardIssuer>
                   <!--Optional:-->
                   <ns:IsActive>true</ns:IsActive>
                   <!--Optional:-->
                   <ns:LastFourDigits>5454</ns:LastFourDigits>
                </ns:CardInfo>
                <!--Optional:-->
                <ns:PayeeContactInfo>
                   <!--Optional:-->
                   <ns:AddressLine1>safv</ns:AddressLine1>
                   <!--Optional:-->
                   <ns:AddressLine2>vsdavfsad</ns:AddressLine2>
                   <!--Optional:-->
                   <ns:BillingPostalCode>54956</ns:BillingPostalCode>
                   <!--Optional:-->
                   <ns:City>Neenah</ns:City>
                   <!--Optional:-->
                   <ns:Country>US</ns:Country>
                   <!--Optional:-->
                   <!--Optional:-->
                   <ns:EmailAddress>test@test.com</ns:EmailAddress>
                   <!--Optional:-->
                   <ns:FirstName>TEST</ns:FirstName>
                   <!--Optional:-->
                   <ns:LastName>TEST</ns:LastName>
                   <!--Optional:-->
                   <ns:PayeeName>TEST</ns:PayeeName>
                   <!--Optional:-->
                   <ns:PhoneNumber>470-424-7194</ns:PhoneNumber>
                   <!--Optional:-->
                   <ns:State>WI</ns:State>
                </ns:PayeeContactInfo>
                <!--Optional:-->
                <ns:PaymentStatus>ACCEPTED</ns:PaymentStatus>
                <!--Optional:-->
                <ns:ReferenceNumber>578b456A5S3AKKA35965</ns:ReferenceNumber>
                <!--Optional:-->
                <ns:TxnRefNumber>538D85F6J0v5KKK83</ns:TxnRefNumber>
             </tem:request>
          </tem:PaymentNotification>
       </soapenv:Body>
     </soapenv:Envelope>
    """
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    print(resp.text)
    return resp.text




def application(driver, value, zipcode, rand_name, rand_name_last, addr, city, phone, email, itemtest):
    time.sleep(2)
    print('Start new application')
    driver.find_element_by_id('QuoteZipCode').click()
    time.sleep(1)
    driver.find_element_by_id('QuoteZipCode').send_keys(zipcode)
    time.sleep(1)
    driver.find_element_by_id(itemtest).click()
    time.sleep(2)
    print('Value & Item')
    driver.find_element_by_xpath('//*[@id="jewelry-itemType-1"]/option[2]').click()
    time.sleep(2)
    driver.find_element_by_id('jewelry-itemValue-1').click()
    time.sleep(1)
    driver.find_element_by_id('jewelry-itemValue-1').send_keys(value)
    time.sleep(2)
    driver.find_element_by_id('quoteInfoNext').click()
    try:
        driver.find_element_by_id('quoteInfoNext').click()
    except:
        print('button not found')
    time.sleep(3)
    driver.find_element_by_id('quoteResultsNext').click()
    time.sleep(3)
    driver.find_element_by_id('noThanks').click()
    time.sleep(2)
    driver.find_element_by_id('customerNext').click()
    time.sleep(3)
    print(rand_name)
    print(rand_name_last)
    driver.find_element_by_id('ApplicantFirstName').click()
    driver.find_element_by_id('ApplicantFirstName').send_keys(rand_name)
    time.sleep(1)
    driver.find_element_by_id('ApplicantLastName').click()
    driver.find_element_by_id('ApplicantLastName').send_keys(rand_name_last)
    time.sleep(1)
    driver.find_element_by_id('ApplicantAddress').click()
    driver.find_element_by_id('ApplicantAddress').send_keys(addr)
    time.sleep(1)
    driver.find_element_by_id('ApplicantCity').click()
    driver.find_element_by_id('ApplicantCity').send_keys(city)
    time.sleep(1)
    driver.find_element_by_id('ApplicantState').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ApplicantState"]/option[51]').click()
    time.sleep(1)
    driver.find_element_by_id('ApplicantPhoneNumber').click()
    driver.find_element_by_id('ApplicantPhoneNumber').send_keys(phone)
    time.sleep(1)
    driver.find_element_by_id('ApplicantEmailAddress').click()
    driver.find_element_by_id('ApplicantEmailAddress').send_keys(email)
    time.sleep(1)
    driver.find_element_by_id('applicantDOBMonth').click()
    driver.find_element_by_xpath('//*[@id="applicantDOBMonth"]/option[6]').click()
    time.sleep(1)
    driver.find_element_by_id('applicantDOBDay').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="applicantDOBDay"]/option[2]').click()
    time.sleep(1)
    driver.find_element_by_id('applicantDOBYear').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="applicantDOBYear"]/option[28]').click()
    time.sleep(1)
    driver.find_element_by_id('ApplicantGender-Female').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="mainform"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/label[1]/i').click()
    time.sleep(3)
    print('start of application completed')
def section3(driver):
    print('section 3')
    driver.find_element_by_id('ConvictedOfCrime-Misdemeanor').click()
    time.sleep(1)
    driver.find_element_by_id('SentenceCompletionDate').click()
    time.sleep(1)
    today = date.today()
    d1 = today.strftime("%m/%d/2014")
    print(d1)
    driver.find_element_by_id('SentenceCompletionDate').send_keys(d1)
    time.sleep(3)
    driver.find_element_by_id('ConvictionType').click()
    driver.find_element_by_xpath('//*[@id="ConvictionType"]/option[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mainform"]/div[3]/div[2]/div[2]/div/div[1]/div/label[1]/i').click()
    time.sleep(1)
    driver.find_element_by_id('HasAgreedToTerms').click()
    time.sleep(100)
    driver.find_element_by_id('applicantNext').click()
    time.sleep(3)

    print('Jewelry Details')
    driver.find_element_by_xpath(
        '//*[@id="jmnfJewelryDetailsForm"]/div[1]/div[2]/div[1]/div/div/div/label[2]/i').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="jmnfJewelryDetailsForm"]/div[1]/div[2]/div[2]/div/div/div/label[1]/i').click()
    time.sleep(1)
    driver.find_element_by_id('AppraisalDate-JI-1').click()
    driver.find_element_by_id('AppraisalDate-JI-1').send_keys('11/11/2021')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="HasAlarm-No"]').click()
    time.sleep(1)
    print('The effective date is the current date')
    driver.find_element_by_id('EffectiveDate').click()
    driver.find_element_by_id('EffectiveDate').send_keys(d1)
    time.sleep(1)
    driver.find_element_by_id('jewelryDetailsNext').click()
    time.sleep(3)
    app_num = ""
def additionalquestions(driver):
    print('Additional Questions')
    driver.find_element_by_id('DeniedCoverage-No').click()
    time.sleep(1)
    driver.find_element_by_id('SafeDeposit-No').click()
    time.sleep(1)
    driver.find_element_by_id('GatedCommunity-No').click()
    time.sleep(1)
    driver.find_element_by_id('EmploysDomesticHelp-No').click()
    time.sleep(1)
    driver.find_element_by_id('HomeHasOtherResidents-No').click()
    time.sleep(1)
    driver.find_element_by_id('JewelryWearFrequency').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="JewelryWearFrequency"]/option[2]').click()
    time.sleep(1)
    driver.find_element_by_id('OvernightTravelFrequency').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="OvernightTravelFrequency"]/option[2]').click()
    time.sleep(1)
    driver.find_element_by_id('additionalQuestionsNext').click()
    time.sleep(7)
    print('There is no payment')
    print('---------- Review Your Application')
    driver.find_element_by_id('HasAcknowledgedLegalTerms').click()
    time.sleep(3)
    driver.find_element_by_id('SignAndSubmit').click()
    time.sleep(20)
    app_num = driver.find_element_by_xpath(
        '//*[@id="confirmationContainer"]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]').text
    print('account number is: {}'.format(app_num))
    eff_date = driver.find_element_by_xpath(
        '//*[@id="confirmationContainer"]/div/div/div[2]/div[2]/div[2]/div/div[2]').text
    print('effective date is: {}'.format(eff_date))
    time.sleep(3)
    return app_num
def gwpolicycenter(driver, env, appnum):
    print('Opening GW policy center')
    driver.get(env)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="Login:LoginScreen:LoginDV:username-inputEl"]').click()
    driver.find_element_by_xpath('//*[@id="Login:LoginScreen:LoginDV:username-inputEl"]').send_keys('su')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="Login:LoginScreen:LoginDV:password-inputEl"]').click()
    driver.find_element_by_xpath('//*[@id="Login:LoginScreen:LoginDV:password-inputEl"]').send_keys('gw')
    time.sleep(1)
    driver.find_element_by_id('Login:LoginScreen:LoginDV:submit-btnInnerEl').click()
    driver.maximize_window()  # driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_id('TabBar:SearchTab').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="Search:MenuLinks:Search_AccountSearch"]/div/span').click()
    time.sleep(2)
    driver.find_element_by_id('AccountSearch:AccountSearchScreen:AccountSearchDV:AccountNumber-inputEl').click()
    time.sleep(1)
    driver.find_element_by_id('AccountSearch:AccountSearchScreen:AccountSearchDV:AccountNumber-inputEl').send_keys(
        appnum)
    time.sleep(1)
    driver.find_element_by_id(
        'AccountSearch:AccountSearchScreen:AccountSearchDV:SearchAndResetInputSet:SearchLinksInputSet:Search').click()
    time.sleep(2)
    driver.find_element_by_id('AccountSearch:AccountSearchScreen:AccountSearchResultsLV:0:AccountNumber').click()
    time.sleep(3)
def body_ToRegisterForAnOnlineAccount(driver):
    print('verifying Personal_Jewelry_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jm-logo")))
    print(driver.find_element_by_id('page-body').text)
    time.sleep(3)
    print('Personal_Jewelry_Body - verified')
    return True
def body_startaclaim(driver):
    print('verifying startaclaim_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lookupForm")))
    startAClaimbody = driver.find_element_by_id('lookupForm')
    print(startAClaimbody.text)
    helpIcon = driver.find_element_by_id('helpLookupPolicyNumber').is_displayed()
    print(helpIcon, "Help icon is displayed.")
    continueButton = driver.find_element_by_id('continueButton').is_displayed()
    print(continueButton, "Continue button is displayed.")
    print(driver.find_element_by_xpath("//div[contains(@class, 'container')]").text)
    time.sleep(3)
    print('startaclaim_Body - verified')
    return True
def body_jmuniversity(driver):
    print('verifying jmuniversity_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-3071")))
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(heroContent.text)
    heresWhatYoullGet = driver.find_element_by_id('title-3071')
    print(heresWhatYoullGet.text)
    heresWhatYoullGetInfogrid = driver.find_element_by_id('info-grid-3096')
    print(heresWhatYoullGetInfogrid.text)
    getStarted = driver.find_element_by_id('title-3101')
    print(getStarted.text)
    buttons = driver.find_element_by_id('cta-group-3106')
    print(buttons.text, "Buttons are displayed.")
    time.sleep(3)
    print('jmuniversity_Body - verified')
    return True
def body_COVIDResources(driver):
    print('verifying COVIDResources_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-6611")))
    coronaVirusInformationTitle = driver.find_element_by_id('title-6611')
    print(coronaVirusInformationTitle.text)
    informationBlock = driver.find_element_by_id('text-block-6616')
    print(informationBlock.text)
    buttons = driver.find_element_by_id('cta-group-6586')
    print(buttons.text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    time.sleep(3)
    print('COVIDResources_Body - verified')
    return True
def body_ContactUs(driver):
    print('verifying ContactUs_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "info-grid-2741")))
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodecore-pagefield-hero')]")
    print(heroContent.text)
    contactInformationTitle = driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]")
    print(contactInformationTitle.text)
    contactInformationInfogrid = driver.find_element_by_id('info-grid-2741')
    print(contactInformationInfogrid .text)
    map = driver.find_element_by_id('feature-row-2746').is_displayed()
    print(map, "Map is displayed.")
    time.sleep(3)
    print('ContactUs_Body - verified')
    return True
def body_ShareYourConcerns(driver):
    print('verifying ShareYourConcerns_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-2721")))
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(heroContent.text)
    shareYourConcernsTitle = driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]")
    print(shareYourConcernsTitle.text)
    shareYourConcernsTextBlock = driver.find_element_by_id('text-block-2721')
    print(shareYourConcernsTextBlock.text)
    time.sleep(3)
    print('ShareYourConcerns_Body - verified')
    return True
def body_Homuchdoesitcosttoresizearing(driver):
    print('verifying Homuchdoesitcosttoresizearing_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar-2181")))
    checkYourRate = driver.find_element_by_id('sidebar-2181')
    print(checkYourRate.text)
    postImage = driver.find_element_by_xpath('//img[@alt="How much does it cost to resize a ring?"]').is_displayed()
    print(postImage, "Post image is displayed")
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(heroContent.text)
    content = driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodeblog-articlebody')]")
    print(content.text)
    #    mostPopularPosts = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-most-popular-posts-block')]")
    #    print(mostPopularPosts.text)
    postsByTopic = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-blog-detail-topics-list')]")
    print(postsByTopic.text)
    time.sleep(3)
    print('Homuchdoesitcosttoresizearing_Body - verified')
    return True
def body_Howtocleangoldjewelry(driver):
    print('verifying Howtocleangoldjewelry_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar-2181")))
    checkYourRate = driver.find_element_by_id('sidebar-2181')
    print(checkYourRate.text)
    postImage = driver.find_element_by_xpath('//img[@alt="How to Clean Gold Jewelry"]').is_displayed()
    print(postImage, "Post image is displayed")
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(heroContent.text)
    content = driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodeblog-articlebody')]")
    print(content.text)
    #    mostPopularPosts = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-most-popular-posts-block')]")
    #    print(mostPopularPosts.text)
    postsByTopic = driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-blog-detail-topics-list')]")
    print(postsByTopic.text)
    time.sleep(3)
    print('Howtocleangoldjewelry_Body - verified')
    return True
def body_Howmuchshouldcost(driver):
    print('verifying Howmuchshouldcost_Body containers')
    time.sleep(3)

    # side bar
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar-2181")))
    print(driver.find_element_by_id('cta_button_413440_8c15d489-2ed8-41c5-a448-e7e1fa60e414').text)
    print(driver.find_element_by_id('sidebar-2181').text)

    # content in the middle
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodeblog-articlebody')]").text)
    #    print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-most-popular-posts-block')]").text)

    button = driver.find_element_by_xpath('//*[@id="hs-cta-img-faa1df2a-d1f9-4ed1-80b1-61c73d711ed0"]')
    print(button, "button located")

    # images
    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    # print(image, "site-log")

    #image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    #print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    comprehensivecoverageicon = driver.find_element_by_xpath('//img[@alt="Youtube icon"]').is_displayed()
    print(comprehensivecoverageicon, "Icon comprehensive coverage is displayed")

    time.sleep(3)
    print('Howmuchshouldcost_Body - verified')
    return True
def body_Howtomakearing(driver):
    print('verifying Howtomakearing_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "sidebar-2181")))
    print(driver.find_element_by_id('quick-quote').text)
    print(driver.find_element_by_id('sidebar-2181').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'layout__region layout__region--first')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-field-blocknodeblog-articlebody')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-blog-detail-topics-list')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'quote-widget')]").text)

    # images
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")
    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")
    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")
    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")
    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")
    time.sleep(3)
    print('Howtomakearing_Body - verified')
    return True
def body_Moreblogarticles(driver):
    print('verifying Moreblogarticles_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "block-jewelers-mutual-content")))

    # content in the middle
    print(driver.find_element_by_id('block-jewelers-mutual-content').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-sidebars-personal-popular-posts')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-views block--type-views-blockblog-topics-jewelry-box-topics')]").text)

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[4]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div/div/div/div/div[5]/div/div[1]/a/picture/img').is_displayed()
    print(image, "image in the middle")

    time.sleep(3)
    print('Moreblogarticles_Body - verified')
    return True
def body_PrivacyPolicy(driver):
    print('verifying PrivacyPolicy_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-9491")))

    # content in the middle
    print(driver.find_element_by_id('text-block-9491').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)

    # images
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    # print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")


    print('PrivacyPolicy_Body - verified')
    return True
def body_TermsofUse(driver):
    print('verifying PrivacyPolicy_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-9486")))

    # content in the middle
    print(driver.find_element_by_id('text-block-9486').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)

    # images
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    # print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('PrivacyPolicy_Body - verified')
    return True
def body_engagementringinsurance(driver):
    print('verifying engagementringinsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-3496")))

    # content in the middle including questions and table and description
    print(driver.find_element_by_id('title-3496').text)
    print(driver.find_element_by_id('title-3436').text)
    print(driver.find_element_by_id('info-grid-3466').text)
    #    print(driver.find_element_by_id('info-grid-3491').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('accordion-3516').text)
    print(driver.find_element_by_id('feature-row-5201').text)
    #    print(driver.find_element_by_id('feature-row-3521').text)
    #    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    #    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__tout hero__tout--grey no-flex')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table__center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'table-footer')]").text)
    #    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)


    # body page images
    # image = driver.find_element_by_xpath('//*[@id="feature-row-3521"]/style/text()').is_displayed()
    # print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="feature-row-5201"]/div/div[1]/img').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="info-grid-3491"]/div[4]/img[2]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="info-grid-3491"]/div[3]/img[2]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="info-grid-3491"]/div[2]/img[2]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="info-grid-3491"]/div[1]/img[2]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[5]/img[2]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[4]/img[2]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[3]/img[2]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[2]/img[2]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="info-grid-3466"]/div[1]/img[2]').is_displayed()
    #    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[3]/div/div/div/div/div/div[2]/div/img').is_displayed()
    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[7]').is_displayed()
    #    print(image, "image")

    #    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[6]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[5]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[4]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[3]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[2]').is_displayed()
    #    print(image, "image")
    #    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div[2]/div/img[1]').is_displayed()
    #    print(image, "image")

    # images
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    # print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('engagementringinsurance_Body - verifyied')
    return True
def body_comparejewelryinsurancetohomeowners(driver):
    print('verifying comparejewelryinsurancetohomeowners_Body containers')
    time.sleep(3)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table__center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blockinfo-grid block--info-grid background-color-')]").text)

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('comparejewelryinsurancetohomeowners_Body - verifyied')
    return True
def body_personaljewelryinsurancecollections(driver):
    print('verifying personaljewelryinsurancecollections_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-3361")))

    # content in the middle + table + info
    print(driver.find_element_by_id('text-image-row-3361').text)
    print(driver.find_element_by_id('title-3366').text)
    print(driver.find_element_by_id('info-grid-3391').text)
    print(driver.find_element_by_id('feature-row-3396').text)
    print(driver.find_element_by_id('feature-row-3401').text)
    print(driver.find_element_by_id('title-8326').text)
    print(driver.find_element_by_id('timeline-row-3406').text)
    print(driver.find_element_by_id('timeline-row-3411').text)
    print(driver.find_element_by_id('timeline-row-3416').text)
    print(driver.find_element_by_id('timeline-row-3421').text)
    print(driver.find_element_by_id('basic-code-block-trustpilot-horizontal---no-tags').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)

    # images
    image = driver.find_element_by_xpath('//*[@id="timeline-row-3421"]/div[1]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="timeline-row-3416"]/div[1]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="timeline-row-3411"]/div[1]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="timeline-row-3406"]/div[1]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3391"]/div[2]/div[2]/div/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3391"]/div[2]/div[1]/div/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3391"]/div[1]/div[1]/div/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3391"]/div[1]/div[2]/div/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="text-image-row-3361"]/div[1]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    # image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div[1]/div[3]/div/p[1]/img').is_displayed()
    # print(image, "image in the middle")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('personaljewelryinsurancecollections_Body - verifyied')
    return True
def body_crownandcaliber(driver):
    print('verifying crownandcaliber_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12466")))

    # content in the middle
    print(driver.find_element_by_id('text-block-12466').text)
    print(driver.find_element_by_id('feature-row-12476').text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12461"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('crownandcaliber_Body - verifyied')
    return True
def body_adiamor(driver):
    print('verifying adiamor_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12426")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12426').text)
    print(driver.find_element_by_id('feature-row-12436').text)
    print(driver.find_element_by_id('text-block-12431').text)
    print(driver.find_element_by_xpath("//*[@id='feature-row-12436']/div/div[2]/a").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12501"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12421"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('adiamor_Body - verifyied')
    return True
def body_briangavindiamonds(driver):
    print('verifying briangavindiamonds_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12446")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12446').text)
    print(driver.find_element_by_id('feature-row-12451').text)
    print(driver.find_element_by_id('text-block-12456').text)
    print(driver.find_element_by_xpath("//*[@id='feature-row-12451']/div/div[2]/a").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12506"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12441"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('briangavindiamonds_Body - verifyied')
    return True
def body_jamesallen(driver):
    print('verifying jamesallen_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12406")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12406').text)
    print(driver.find_element_by_id('feature-row-12411').text)
    print(driver.find_element_by_id('text-block-12416').text)
    print(driver.find_element_by_xpath("//*[@id='feature-row-12411']/div/div[2]/a").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12521"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12401"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('jamesallen_Body - verifyied')
    return True
def body_bluenile(driver):
    print('verifying bluenile_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12386")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12386').text)
    print(driver.find_element_by_id('feature-row-12391').text)
    print(driver.find_element_by_id('text-block-12396').text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12526"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12381"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('bluenile_Body - verifyied')
    return True
def body_whiteflash(driver):
    print('verifying whiteflash_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-12486")))

    # content in the middle + button
    print(driver.find_element_by_id('text-block-12486').text)
    print(driver.find_element_by_id('feature-row-12496').text)
    print(driver.find_element_by_id('text-block-12491').text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="image-container-12481"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="image-container-12511"]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('whiteflash_Body - verifyied')
    return True
def body_earringinsurance(driver):
    print('verifying earringinsurance_Body containers')
    time.sleep(3)

    # content in the middle + table
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-3971")))
    print(driver.find_element_by_id('title-3971').text)
    print(driver.find_element_by_id('title-3746').text)
    print(driver.find_element_by_id('info-grid-3911').text)
    print(driver.find_element_by_id('info-grid-3966').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('accordion-4106').text)
    print(driver.find_element_by_id('feature-row-5196').text)
    print(driver.find_element_by_id('feature-row-4111').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table__center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="feature-row-5196"]/div/div[1]/img').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="info-grid-3966"]/div[4]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3966"]/div[3]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3966"]/div[2]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3966"]/div[1]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[5]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[4]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[3]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[2]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3911"]/div[1]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[3]/div/div/div/div/div/div[2]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div/div[1]/picture/source[4]').is_displayed()
    print(image, "image")




    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('earringinsurance_Body - verifyied')
    return True
def body_watchinsurance(driver):
    print('verifying watchinsurance_Body containers')
    time.sleep(3)

    # Content in the middle
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-3941")))
    print(driver.find_element_by_id('title-3741').text)
    print(driver.find_element_by_id('info-grid-3791').text)
    print(driver.find_element_by_id('info-grid-3936').text)
    print(driver.find_element_by_id('accordion-4081').text)
    print(driver.find_element_by_id('feature-row-5191').text)
    print(driver.find_element_by_id('feature-row-4086').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content-wrapper hero-scheme-blue-black')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table etb spacing')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'basic-code-block-what-our-policyholders-say')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)

    # Images
    image = driver.find_element_by_xpath('//*[@id="feature-row-5191"]/div/div[1]/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3936"]/div[4]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3936"]/div[3]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3936"]/div[2]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3936"]/div[1]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[5]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[4]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[3]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[2]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="info-grid-3791"]/div[1]/img[2]').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[3]/div/div/div/div/div/div[2]/div/img').is_displayed()
    print(image, "image")
    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-content"]/div/article/div/div/div/div[1]/div/div/div[1]/picture/source[5]').is_displayed()
    print(image, "image")

    image = driver.find_element_by_xpath('//*[@id="block-jewelers-mutual-branding"]/a[1]').is_displayed()
    print(image, "site-log")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Facebook"]').is_displayed()
    print(image, "facebook")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Instagram"]').is_displayed()
    print(image, "instagram")

    image = driver.find_element_by_xpath('//*[@title="Visit us on Twitter"]').is_displayed()
    print(image, "twitter")

    image = driver.find_element_by_xpath('//*[@title="Visit us on LinkedIn"]').is_displayed()
    print(image, "linked-in")

    time.sleep(3)
    print('watchinsurance_Body - verifyied')
    return True
def body_necklaceinsurance(driver):
    print('verifying necklaceinsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "info-grid-3881")))
    print(driver.find_element_by_id('info-grid-3881').text)
    print(driver.find_element_by_id('info-grid-3996').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('accordion-4131').text)
    print(driver.find_element_by_id('feature-row-5186').text)
    print(driver.find_element_by_id('feature-row-4136').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'title-4001')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table etb spacing')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'title-3751')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)
    print('necklaceinsurance_Body - verifyied')
    return True
def body_braceletinsurance(driver):
    print('verifying braceletinsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4061")))
    print(driver.find_element_by_id('title-4061').text)
    print(driver.find_element_by_id('info-grid-3821').text)
    print(driver.find_element_by_id('info-grid-4056').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('accordion-4181').text)
    print(driver.find_element_by_id('feature-row-5181').text)
    print(driver.find_element_by_id('feature-row-4186').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table__center')]").text)
    time.sleep(3)
    print('braceletinsurance_Body - verifyied')
    return True
def body_smartwatchinsurance(driver):
    print('verifying smartwatchinsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4031")))
    print(driver.find_element_by_id('title-4031').text)
    print(driver.find_element_by_id('title-3761').text)
    print(driver.find_element_by_id('info-grid-3851').text)
    print(driver.find_element_by_id('info-grid-4026').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    print(driver.find_element_by_id('quote-widget-11416').text)
    print(driver.find_element_by_id('feature-row-4161').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table etb spacing')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-block-content block--type-block-content13310d8b-6ea7-46ff-8378-d84a47f524f9')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blockaccordion')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'content-lg text-left')]").text)
    time.sleep(3)
    print('smartwatchinsurance_Body - verifyied')
    return True
def body_howtocleanandcareforyourdiamondring(driver):
    print('verifying howtocleanandcareforyourdiamondring_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-5206")))
    print(driver.find_element_by_id('text-image-row-5206').text)
    print(driver.find_element_by_id('title-9146').text)
    print(driver.find_element_by_id('info-grid-5236').text)
    print(driver.find_element_by_id('title-5251').text)
    print(driver.find_element_by_id('info-grid-5281').text)
    print(driver.find_element_by_id('title-9151').text)
    print(driver.find_element_by_id('info-grid-5271').text)
    print(driver.find_element_by_id('title-9156').text)
    print(driver.find_element_by_id('info-grid-4776').text)
    print(driver.find_element_by_id('title-5241').text)
    print(driver.find_element_by_id('info-grid-4836').text)
    print(driver.find_element_by_id('feature-row-5246').text)
    print(driver.find_element_by_id('title-9161').text)
    print(driver.find_element_by_id('related-content-9181').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    time.sleep(3)
    print('howtocleanandcareforyourdiamondring_Body - verifyied')
    return True
def body_weinsurejewelry(driver):
    print('verifying weinsurejewelry_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-5551")))
    print(driver.find_element_by_id('title-5551').text)
    print(driver.find_element_by_id('text-image-row-5556').text)
    print(driver.find_element_by_id('title-5561').text)
    print(driver.find_element_by_id('info-grid-5586').text)
    print(driver.find_element_by_id('title-5591').text)
    print(driver.find_element_by_id('basic-code-block-trustpilot-quote').text)
    print(driver.find_element_by_id('image-container-8481').text)
    print(driver.find_element_by_id('info-grid-4886').text)
    print(driver.find_element_by_id('image-container-8486').text)
    print(driver.find_element_by_id('feature-row-8491').text)
    print(driver.find_element_by_id('feature-row-5636').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table-wrapper')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)
    print('weinsurejewelry_Body - verifyied')
    return True
def body_coronavirusBusiness(driver):
    print('verifying coronavirusBusiness_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-block-6626")))
    print(driver.find_element_by_id('text-block-6626').text)
    print(driver.find_element_by_id('text-block-6631').text)
    print(driver.find_element_by_id('text-block-6686').text)
    print(driver.find_element_by_id('text-block-6636').text)
    print(driver.find_element_by_id('cta-group-9496').text)
    print(driver.find_element_by_id('text-block-6861').text)
    print(driver.find_element_by_id('text-block-7411').text)
    print(driver.find_element_by_id('text-block-7526').text)
    print(driver.find_element_by_id('title-7736').text)
    print(driver.find_element_by_id('text-block-7761').text)
    print(driver.find_element_by_id('text-block-6851').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)
    print('coronavirusBusiness_Body - verifyied')
    return True
def body_GuidetoJewelryInsurance(driver):
    print('verifying GuidetoJewelryInsurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-6926")))
    print(driver.find_element_by_id('text-image-row-6926').text)
    print(driver.find_element_by_id('title-6931').text)
    print(driver.find_element_by_id('info-grid-6971').text)
    print(driver.find_element_by_id('title-7011').text)
    print(driver.find_element_by_id('title-7021').text)
    print(driver.find_element_by_id('quote-widget-6401').text)
    # print(driver.find_element_by_id('feature-row-7031').text)
    print(driver.find_element_by_id('title-7036').text)
    print(driver.find_element_by_id('title-7066').text)
    # print(driver.find_element_by_id('text-block-7151').text)
    print(driver.find_element_by_id('info-grid-7061').text)
    print(driver.find_element_by_id('title-7136').text)
    # print(driver.find_element_by_id('title-7131').text)
    print(driver.find_element_by_id('feature-row-7126').text)
    print(driver.find_element_by_id('title-7141').text)
    # print(driver.find_element_by_id('text-block-7146').text)
    print(driver.find_element_by_id('info-grid-4886').text)
    # print(driver.find_element_by_id('text-block-7166').text)
    # print(driver.find_element_by_id('text-block-7841').text)
    # print(driver.find_element_by_id('feature-row-7171').text)
    print(driver.find_element_by_id('title-7176').text)
    # print(driver.find_element_by_id('text-block-7181').text)
    # print(driver.find_element_by_id('text-block-7191').text)
    print(driver.find_element_by_id('text-image-row-7186').text)
    print(driver.find_element_by_id('text-image-row-7196').text)
    print(driver.find_element_by_id('text-image-row-7201').text)
    print(driver.find_element_by_id('text-image-row-7206').text)
    print(driver.find_element_by_id('title-7211').text)
    # print(driver.find_element_by_id('text-block-7216').text)
    print(driver.find_element_by_id('info-grid-7236').text)
    print(driver.find_element_by_id('feature-row-7246').text)
    # print(driver.find_element_by_id('text-block-7251').text)
    # print(driver.find_element_by_id('text-block-7256').text)
    print(driver.find_element_by_id('basic-code-block-what-our-policyholders-say').text)
    # print(driver.find_element_by_id('feature-row-7266').text)
    # print(driver.find_element_by_id('feature-row-7311').text)
    print(driver.find_element_by_id('info-grid-7306').text)
    print(driver.find_element_by_id('feature-row-7316').text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]").text)
    # print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blockinfo-grid block--info-grid background-color-gray')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blockfeature')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'comparison-table etb spacing')]").text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]").text)
    time.sleep(3)
    print('GuidetoJewelryInsurance_Body - verifyied')
    return True
def body_homepage(driver):
    print('verifying homepage_Body containers')
    time.sleep(3)
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '//*[@id="block-jewelers-mutual-branding"]/a[1]')))

    # claimsatisfactionratecontent = driver.find_element_by_id('feature-row-2861')
    # print(claimsatisfactionratecontent.text)
    # claimsatisfactionrateimage = driver.find_element_by_id('image-container-8276').is_displayed()
    # print(claimsatisfactionrateimage, " Image is displayed")
    image_whatourpolicyholderssay = driver.find_element_by_id('image-container-8266').is_displayed()
    print(image_whatourpolicyholderssay, " Image is displayed")
    customercareicon = driver.find_element_by_xpath('//img[@alt="customer care graphic"]').is_displayed()
    print(customercareicon, "Icon customer care is displayed")
    print(driver.find_element_by_id('title-46').text)
    print(driver.find_element_by_id('info-grid-8871').text)
    print(driver.find_element_by_id('quote-widget-6401').text)
    print(driver.find_element_by_id('title-151').text)
    print(driver.find_element_by_id('info-grid-136').text)
    print(driver.find_element_by_id('image-container-8251').text)
    print(driver.find_element_by_id('feature-row-141').text)
    print(driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]").text)
    time.sleep(3)
    print('homepage_Body - verifyied')
    return True
def business_insurance_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4416")))

    heroimage = driver.find_element_by_xpath("//div[contains(@class, 'hero__content-wrapper hero-scheme-blue-black')]")
    print(heroimage.text)

    corepolicies = driver.find_element_by_id('title-4416')
    print(corepolicies.text)

    corepoliciesinfogid = driver.find_element_by_id('info-grid-4436')
    print(corepoliciesinfogid.text)

    addonstitle = driver.find_element_by_id('title-4441')
    print(addonstitle.text)

    addonscontent1 = driver.find_element_by_id('info-grid-4481')
    print(addonscontent1.text)

    addonsimage1 = driver.find_element_by_id('image-container-8286').is_displayed()
    print(addonsimage1, "Image is displayed")

    addonsimage2 = driver.find_element_by_id('image-container-8311').is_displayed()
    print(addonsimage2, "Image is displayed")

    addonscontent2 = driver.find_element_by_id('info-grid-8306')
    print(addonscontent2.text)

    # driver.find_element(by=By.XPATH, value="//div[contains(@class, 'title-bar content-lg spacing clearfix')]")
    customerstoriestitle = driver.find_element_by_css_selector("[class*='title-bar']")
    print(customerstoriestitle.text)

    customerstories = driver.find_element_by_id('text-block-4406')
    print(customerstories.text)

    customerstoriesvideomodal = driver.find_element_by_id('video-modal-4411').is_displayed()
    print(customerstoriesvideomodal, "Video modal is displayed")

    toolsforbusiness = driver.find_element_by_id('feature-row-4486')
    print(toolsforbusiness.text)

    jewelerresourcestitle = driver.find_element_by_id('title-8321')
    print(jewelerresourcestitle .text)

    jewelerresourcesrelatedcontent = driver.find_element_by_id('related-content-9086')
    print(jewelerresourcesrelatedcontent.text)

    contactanagenttitle = driver.find_element_by_id('title-8316')
    print(contactanagenttitle.text)

    salesforceiframe = driver.find_element_by_xpath("//div[contains(@class, 'block-layout-builder block--type-inline-blocksalesforce-form')]")
    print(salesforceiframe.text)

    navigationlinks = driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]")
    print(navigationlinks.text)

    element = driver.find_element_by_id('title-8316')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('claims_Body - verified')
    return True
def business_claims_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-4596")))

    # herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    # print(herocontent.text)

    startyourclaim = driver.find_element_by_id('text-image-row-4596')
    print(startyourclaim.text)

    minimizefurtherdamage = driver.find_element_by_id('text-image-row-4601')
    print(minimizefurtherdamage.text)

    meetyourclaimsexpert = driver.find_element_by_id('text-image-row-4606')
    print(meetyourclaimsexpert.text)

    backtobusiness = driver.find_element_by_id('text-image-row-4611')
    print(backtobusiness.text)

    claimssatisfactionrate = driver.find_element_by_id('feature-row-4616')
    print(claimssatisfactionrate.text)

    themostcommonclaims = driver.find_element_by_id('title-4646')
    print(themostcommonclaims.text)

    themostcommonclaimsinfogrid = driver.find_element_by_id('info-grid-4641')
    print(themostcommonclaimsinfogrid .text)

    faqaccordion = driver.find_element_by_id('accordion-4661')
    print(faqaccordion.text)

    startaclaimblock = driver.find_element_by_id('feature-row-4666')
    print(startaclaimblock.text)

    element = driver.find_element_by_id('feature-row-4666')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('claims_Body - verified')
    return True
def business_paymybill_body_validation(driver):
    print('verifying paymybill containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'lookupForm')))
    jmlogo = driver.find_element_by_class_name('jm-logo').is_displayed()
    print(jmlogo, "JM Logo is displayed")

    quickbillpaybody = driver.find_element_by_id('lookupForm')
    print(quickbillpaybody.text)

    element = quickbillpaybody
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    print(driver.find_element_by_id('continueButton').text)
    print(driver.find_element_by_id('recaptcha').text)
    print(driver.find_element_by_class_name('navbar').text)

    footer = driver.find_element_by_xpath("//div[contains(@class, 'col-md-8 col-sm-6 col-xs-12')]")
    print(footer.text)

    element = footer
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    privacyandterms = driver.find_element_by_xpath("//div[contains(@class, 'col-md-4 col-sm-6 col-xs-12')]")
    print(privacyandterms.text)

    time.sleep(3)
    print('Pay_My_Bill_Body - verified')
    return True
def business_zingplatform_body_validation(driver):
    print('Verifying Zing Platform containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-8466")))
    herocontainer = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(herocontainer.text)

    maximizingyourbusinesspotentialtitle = driver.find_element_by_id('title-8466')
    print(maximizingyourbusinesspotentialtitle.text)

    maximizingyourbusinesspotentialtext = driver.find_element_by_id('title-8471')
    print(maximizingyourbusinesspotentialtext.text)

    zingvideomodal = driver.find_element_by_id('video-modal-8476').is_displayed()
    print(zingvideomodal, 'Video modal is displayed')

    benefitsforyourjewelrybusiness = driver.find_element_by_id('title-8366')
    print(benefitsforyourjewelrybusiness.text)

    benefitsinfogrid = driver.find_element_by_id('info-grid-7956')
    print(benefitsinfogrid.text)

    benefitsimage = driver.find_element_by_id('image-container-8541').is_displayed()
    print(benefitsimage, 'Image is displayed')

    toolsforyourbusinesstitle = driver.find_element_by_id('title-8371')
    print(toolsforyourbusinesstitle.text)

    toolsforyourbusinessinfogrid = driver.find_element_by_id('info-grid-7981')
    print(toolsforyourbusinessinfogrid.text)

    howitworks = driver.find_element_by_id('related-content-9036')
    print(howitworks.text)

    seetheplatforminaction = driver.find_element_by_id('feature-row-8461')
    print(seetheplatforminaction.text)

    faq = driver.find_element_by_id('accordion-9066')
    print(faq.text)

    registernow = driver.find_element_by_id('feature-row-7986')
    print(registernow.text)

    element = driver.find_element_by_id('feature-row-7986')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('Zing Platform - verified')
    return True
def business_jm_shipping_solution_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-9266")))

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]")
    print(herocontent.text)

    shipjewelryonzingplatform = driver.find_element_by_id('text-image-row-9266')
    print(shipjewelryonzingplatform.text)

    howitworksvideomodal = driver.find_element_by_id('video-modal-12281').is_displayed()
    print(howitworksvideomodal, "Video modal is displayed")

    howitworksinfogrid = driver.find_element_by_id('info-grid-6906')
    print(howitworksinfogrid.text)

    benefitsforyourbusinessinfogrid = driver.find_element_by_id('info-grid-2291')
    print(benefitsforyourbusinessinfogrid.text)

    putthewholejewelryindustryatyourfingertips = driver.find_element_by_id('feature-row-9276')
    print(putthewholejewelryindustryatyourfingertips.text)

    getstarted = driver.find_element_by_id('title-2341')
    print(getstarted .text)

    salesforceiframe = driver.find_element_by_id('title-4191').is_displayed()
    print(salesforceiframe, "Salesforce iframe is displayed")

    element = driver.find_element_by_id('title-4191')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('jm_shipping_solution_Body - verified')
    return True
def business_jmcareplan_body_validation(driver):
    print('Verifying JM Care Plan - Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "text-image-row-11741")))

    jmcareplanlogo = driver.find_element_by_xpath('//img[@alt="JM Care Plan logo"]').is_displayed()
    print(jmcareplanlogo, "JM Care Plan image is displayed")

    carePlans = driver.find_element_by_id('text-image-row-11741')
    print(carePlans.text)

    careplansyoucantrusttext = driver.find_element_by_id('title-5396')
    print(careplansyoucantrusttext.text)

    careplansyoucantrustvideomodal = driver.find_element_by_id('video-modal-6706').is_displayed()
    print(careplansyoucantrustvideomodal, "Care plans video modal is displayed")

    whyjmcarelansproductsinfogrid = driver.find_element_by_id('info-grid-5416')
    print(whyjmcarelansproductsinfogrid.text)

    whatscoveredinfogrid = driver.find_element_by_id('info-grid-5431')
    print(whatscoveredinfogrid.text)

    whatscovereddetails = driver.find_element_by_id('details-block-5876')
    print(whatscovereddetails.text)

    howtheclaimsprocessworksinfogrid = driver.find_element_by_id('info-grid-5446')
    print(howtheclaimsprocessworksinfogrid.text)

    element = driver.find_element_by_id('info-grid-5446')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('JM Care Plan Body - Verified')
    return True
def business_appraisalsolution_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-11061")))

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content-wrapper hero-scheme-blue-black  ')]")
    print(herocontent.text)

    pagenavigationlinks = driver.find_element_by_xpath("//div[contains(@class, 'navigation__secondary-sticky--links text-center')]")
    print(pagenavigationlinks.text)

    jewelryappraisalsmadeeasy = driver.find_element_by_id('title-11061')
    print(jewelryappraisalsmadeeasy.text)

    zinglogo = driver.find_element_by_id('text-block-11056').is_displayed()
    print(zinglogo, "Zing logo is displayed")

    benefitsofthejewelryappraisaltitle = driver.find_element_by_xpath("//div[contains(@class, 'title-bar content-lg spacing clearfix')]")
    print(benefitsofthejewelryappraisaltitle.text)

    benefitsofthejewelryappraisalinfogrid1 = driver.find_element_by_id('info-grid-11081')
    print(benefitsofthejewelryappraisalinfogrid1.text)

    benefitsiamge = driver.find_element_by_id('image-container-11066').is_displayed()
    print(benefitsiamge, "Image is displayed")

    benefitsofthejewelryappraisalinfogrid2 = driver.find_element_by_id('info-grid-11101')
    print(benefitsofthejewelryappraisalinfogrid2.text)

    seethejewelryappraisalvideomodal = driver.find_element_by_id('video-modal-11111').is_displayed()
    print(seethejewelryappraisalvideomodal, "Video modal is displayed")

    seethejewelryappraisalsolution = driver.find_element_by_id('title-11116')
    print(seethejewelryappraisalsolution.text)

    getstarted = driver.find_element_by_id('title-11126')
    print(getstarted.text)

    getstartediframe = driver.find_element_by_id('title-11131').is_displayed()
    print(getstartediframe, "Get started iframe is displayed")

    whatisthezingplatform = driver.find_element_by_id('feature-row-11121')
    print(whatisthezingplatform.text)

    element = driver.find_element_by_id('feature-row-11121')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('Appraisal Solution Body - Verified')
    return True
def business_jewelerprograms_body_validation(driver):
    print('verifying business_insurance_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-2751")))

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-left')]")
    print(herocontent.text)

    whatsinitforyou = driver.find_element_by_id('title-2751')
    print(whatsinitforyou.text)

    # whatsinitforyouinfogrid = driver.find_element_by_id('info-grid-2776')
    # print(whatsinitforyouinfogrid.text)

    # customercareicon = driver.find_element_by_xpath('//img[@alt="customer care graphic"]').is_displayed()
    # print(customercareicon, "Icon customer care is displayed")

    # easyclaimpaymenticon = driver.find_element_by_xpath('//img[@alt="chart graphic"]')
    # print(easyclaimpaymenticon, "Icon easy claim payments care is displayed")

    # flexibilityicon = driver.find_element_by_xpath('//img[@alt="flexibility graphic"]')
    # print(flexibilityicon, "Icon flexibility care is displayed")

    # growyourbusinessicon = driver.find_element_by_xpath('//img[@alt="trophy graphic"]')
    # print(growyourbusinessicon, "Icon grow your business care is displayed")

    strengthencustomerrelationsimage = driver.find_element_by_id('image-container-9251').is_displayed()
    print(strengthencustomerrelationsimage, "Image is displayed")

    strengthencustomerrelations = driver.find_element_by_id('feature-row-2786')
    print(strengthencustomerrelations.text)

    # therearemoreadvantages = driver.find_element_by_id('feature-row-2791')
    # print(therearemoreadvantages.text)

    requesttobepartoftheprogram = driver.find_element_by_id('title-9256')
    print(requesttobepartoftheprogram.text)

    requestiframe = driver.find_element_by_id('title-4246').is_displayed()
    print(requestiframe, "Request to be part of the program iframe is displayed")

    element = driver.find_element_by_id('title-4246')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('jewelerprograms_Body - verified')
    return True
def business_pawnbrokers_body_validation(driver):
    print('verifying Pawnbrokers_Body containers')
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-4546")))

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(herocontent.text)

    protectyourbusinesstitle = driver.find_element_by_id('title-4546')
    print(protectyourbusinesstitle.text)

    protectyourbusinessleftblock = driver.find_element_by_id('details-block-4571')
    print(protectyourbusinessleftblock.text)

    comprehensivecoverageicon = driver.find_element_by_xpath('//img[@alt="Coverage Icon"]').is_displayed()
    print(comprehensivecoverageicon, "Icon comprehensive coverage is displayed")

    jmshippingsolutionicon = driver.find_element_by_xpath('//img[@alt="Shipping Icon"]').is_displayed()
    print(jmshippingsolutionicon, "Icon JM shipping solution is displayed")

    personaljewelryinsuranceicon = driver.find_element_by_xpath('//img[@alt="Money Icon"]').is_displayed()
    print(personaljewelryinsuranceicon, "Icon personal jewelry insurance is displayed")

    getapersonalizedrisk = driver.find_element_by_id('feature-row-4551')
    print(getapersonalizedrisk.text)

    getapersonalizedriskform = driver.find_element_by_id('basic-code-block-hubspot-form-for-pawnbrokers-page').is_displayed()
    print(getapersonalizedriskform, "Form is displayed")

    element = driver.find_element_by_id('basic-code-block-hubspot-form-for-pawnbrokers-page')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('Pawnbrokers_Body - verified')
    return True
def aboutus_aboutus_body_validation(driver):
    print('verifying aboutus_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-2461")))

    herocontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    print(herocontent.text)

    herosubcontent = driver.find_element_by_xpath("//div[contains(@class, 'hero__tout hero__tout--blue')]")
    print(herosubcontent.text)

    wehavejewelryinourname = driver.find_element_by_xpath("//div[contains(@class, 'layout layout--twocol-section layout--twocol-section--50-50')]")
    print(wehavejewelryinourname.text)

    wehavejewelryvideomodal = driver.find_element_by_id('video-modal-6136').is_displayed()
    print(wehavejewelryvideomodal, "Video modal is displayed")

    partnerships = driver.find_element_by_id('title-2461')
    print(partnerships.text)

    partershipsinfogrid = driver.find_element_by_id('info-grid-2506')
    print(partershipsinfogrid.text)

    givingbackbrilliantly = driver.find_element_by_id('feature-row-2511')
    print(givingbackbrilliantly.text)

    leadership = driver.find_element_by_id('title-2516')
    print(leadership.text)

    executiveofficers = driver.find_element_by_id('text-block-2526')
    print(executiveofficers.text)
    executiveofficersinfogrid = driver.find_element_by_id('info-grid-2566')
    print(executiveofficersinfogrid.text)

    ourboardofdirectors = driver.find_element_by_id('text-block-2636')
    print(ourboardofdirectors.text)

    ourboardofdirectorsinforid = driver.find_element_by_id('info-grid-2696')
    print(ourboardofdirectorsinforid.text)

    alittlemoreaboutus = driver.find_element_by_id('title-2701')
    print(alittlemoreaboutus.text)

    whatsinaname = driver.find_element_by_id('text-image-row-2706')
    print(whatsinaname.text)

    whatsinanameimage = driver.find_element_by_xpath('//img[@alt="storefront illustration"]').is_displayed()
    print(whatsinanameimage, "Image is displayed")

    welovejewelry = driver.find_element_by_id('text-image-row-2711')
    print(welovejewelry.text)

    welovejewelryimage = driver.find_element_by_xpath('//img[@alt="jeweler\'s workstation illustration"]').is_displayed()
    print(welovejewelryimage, "Image is displayed")

    lovejewelrytoo = driver.find_element_by_id('text-image-row-2716')
    print(lovejewelrytoo.text)

    trustpilotblock = driver.find_element_by_id('basic-code-block-trustpilot-about-us-horizontal')
    print(trustpilotblock.text)

    element = driver.find_element_by_id('text-image-row-2716')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(3)
    print('aboutus_Body - verified')
    return True
def aboutus_socialresponsibility_body_validation(driver):
    print('verifying socialresponsibility_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "title-5316")))
    heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__image-container hero__image-container--no-mobile-image')]")
    print(heroContent.text)
    bandTogetherCampaign = driver.find_element_by_id('title-5316')
    print(bandTogetherCampaign.text)
    bandTogetherInfogrid = driver.find_element_by_id('info-grid-5311')
    print(bandTogetherInfogrid.text)
    kidsInNeedImage = driver.find_element_by_xpath('//img[@alt="Kids in Need Foundation"]').is_displayed()
    print(kidsInNeedImage, "Kids in Need Foundation image is displayed.")
    feedingAmerica = driver.find_element_by_xpath('//img[@alt="Feeding America"]').is_displayed()
    print(feedingAmerica, "Feeding America image is displayed.")
    standUpToCancerImage = driver.find_element_by_xpath('//img[@alt="Stand Up To Cancer"]').is_displayed()
    print(standUpToCancerImage, "Stand Up To Cancer image is displayed.")
    supplyATeacher = driver.find_element_by_xpath("//div[contains(@class, 'layout layout--twocol-section layout--twocol-section--50-50')]")
    print(supplyATeacher.text)
    supplyATeacherImage = driver.find_element_by_xpath('//img[@alt="Supply a Teacher"]').is_displayed()
    print(supplyATeacherImage, "Supply a Teacher image is displayed.")
    strengtheningTheJewelryIndustry = driver.find_element_by_id('text-image-row-2361')
    print(strengtheningTheJewelryIndustry .text)
    strengtheningImage = driver.find_element_by_xpath('//img[@alt="diamond heart illustration"]').is_displayed()
    print(strengtheningImage, "Strengthening the Jewelry Industry image is displayed.")
    helpingOurEmployeesHelpOthers = driver.find_element_by_id('title-2366')
    print(helpingOurEmployeesHelpOthers.text)
    helpingInfogrid = driver.find_element_by_id('info-grid-2391')
    print(helpingInfogrid .text)
    #ICONS
    learnMoreAboutUs = driver.find_element_by_id('feature-row-2411')
    print(learnMoreAboutUs.text)
    element = driver.find_element_by_id('feature-row-2411')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('socialresponsibility_Body - verified')
    return True
def aboutus_careers_body_validation(driver):
    print('verifying careers_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "info-grid-1736")))
    # heroContent = driver.find_element_by_xpath("//div[contains(@class, 'hero__content hero__content-align-center')]")
    # print(heroContent.text)
    # ourPeopleAreOurGreatestAssetTitle = driver.find_element_by_id('feature-row-1716')
    # print(ourPeopleAreOurGreatestAssetTitle.text)
    ourPeopleAreOurGreatestAssetInfogrid = driver.find_element_by_id('info-grid-1736')
    print(ourPeopleAreOurGreatestAssetInfogrid.text)
    officeCaroussel = driver.find_element_by_id('carousel-1776').is_displayed()
    print(officeCaroussel, "Office caroussel is displayed.")
    # ourBenefits = driver.find_element_by_id('feature-row-1781')
    # print(ourBenefits.text)
    # ourBenefitsIcon = driver.find_element_by_xpath('//img[@alt="diamond"]').is_displayed()
    # print(ourBenefitsIcon, "Our Benefits icon is displayed.")
    benefits = driver.find_element_by_id('tab-section-4286')
    print(benefits.text)
    #    ourAwards = driver.find_element_by_id('feature-row-8151')
    #    print(ourAwards.text)
    ourAwardsInfogrid = driver.find_element_by_id('info-grid-8146')
    print(ourAwardsInfogrid.text)
    testimonialCaroussel = driver.find_element_by_id('carousel-1946').is_displayed()
    print(testimonialCaroussel, "Testimonial caroussel is displayed.")
    #    hiringProcess = driver.find_element_by_id('feature-row-1816')
    #   print(hiringProcess.text)
    hiringProcessTabs = driver.find_element_by_id('tab-section-4311')
    print(hiringProcessTabs.text)
    #    ourLocations = driver.find_element_by_id('feature-row-4801')
    #    print(ourLocations.text)
    #    eVerify = driver.find_element_by_id('feature-row-4796')
    #    print(eVerify.text)
    contact = driver.find_element_by_id('contact-ribbon-1876')
    print(contact.text)
    talkToUsForm = driver.find_element_by_id('webform-submission-careers-contact-form-block-content-771-form-ajax').is_displayed()
    print(talkToUsForm, "Talk to us form is displayed.")
    map = driver.find_element_by_id('basic-code-block-google-map').is_displayed()
    print(map, "Map is displayed.")
    element = driver.find_element_by_id('basic-code-block-google-map')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('careers_Body - verified')
    return True
def aboutus_newsroom_body_validation(driver):
    print('verifying newsroom_Body containers')
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "block-newsheroblock")))
    herocontent = driver.find_element_by_id('block-newsheroblock')
    print(herocontent.text)
    newsroomContent = driver.find_element_by_id('block-jewelers-mutual-content')
    print(newsroomContent.text)
    element = driver.find_element_by_id('text-block-8926')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(3)
    print('newsroom_Body - verified')
    return True