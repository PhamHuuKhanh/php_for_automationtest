from appium.webdriver.common.mobileby import MobileBy



class HomeScreen:
    # define locators
    textview_title = (MobileBy.ID, "txtTitle")
    btn_signin = (MobileBy.ID, "btnSignIn")
    btn_continueasguest = (MobileBy.ID, "btnContinueAsGuest")

    #Home Tab
    txtview_welcome = (MobileBy.ID, "tvHello")
    txtview_title_localisation = (MobileBy.ID, "tvTitleSelect")
    btn_delivery = (MobileBy.ID, "cvDelivery")
    btn_collection = (MobileBy.ID, "cvCollection")
    link_viewmenu = (MobileBy.ID, "tvHotDealViewMenu")


class Signin_Screen():
    btn_back = (MobileBy.ID,"ivBack")
    txtfield_email = (MobileBy.ID,"etEmail")
    txtfield_password = (MobileBy.ID, "etPassword")
    txtlink_forgotpass = (MobileBy.ID,"tvForgotPassword")
    btn_signin = (MobileBy.ID,"btnLogin")
    btn_signup = (MobileBy.ID,"btnSignUp")


