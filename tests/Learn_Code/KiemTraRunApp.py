
from appium import webdriver
import time

desired_cap = {
    'platformName': 'Android',
    'platformVersion': '9',
    # 'deviceName': 'R58N958WQMN', Samsung os 11
    'deviceName': '179998977d26',  # Remi
    # app universal
    #'appPackage': 'com.phdv.universal.sit',
    #'appActivity': 'com.phdv.universal.feature.main.MainActivity'

    'appPackage': 'com.pizzahut.jp',
    'appActivity': 'com.pizzahut.jp.view.splash.SplashActivity'
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
print("---trial---")
time.sleep(5)
abc= driver.find_element_by_id("tvLanguage").text
print(abc + " ahihi")

abc= driver.find_element_by_id("tvUseYourAccountToGetStarted").text
print(abc + " ssss")

print("-------")

