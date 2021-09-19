from appium.webdriver.common.mobileby import MobileBy

class Welcome_Screen():
    # change laguage:
    btn_changelaguage  = (MobileBy.ID,"clLanguageSelector")
    txtview_language = (MobileBy.ID,"tvLanguage")
    language_en = (MobileBy.XPATH,"//android.view.ViewGroup[@index=1]") # English
    language_jp = (MobileBy.XPATH, "//android.view.ViewGroup[@index=0]")  # Japan
    # Option: text view, Signin/Singup, Menu, Coupon
    textview_title = (MobileBy.ID, "tvUseYourAccountToGetStarted")
    btn_signin_signup = (MobileBy.ID, "btnSignInSignUp")
    btn_gotomenu = (MobileBy.ID, "btnMenu")
    btn_getcpupon = (MobileBy.ID, "btnGetCoupon")

class Signin_Screen():
    btn_back = (MobileBy.ID,"ivBack")
    txtfield_email = (MobileBy.ID,"etEmail")
    txtfield_password = (MobileBy.ID, "etPassword")
    txtlink_forgotpass = (MobileBy.ID,"tvForgotPassword")
    btn_signin = (MobileBy.ID,"btnLogin")
    btn_signup = (MobileBy.ID,"btnSignUp")


class Mycoupon_Screen():
    btn_back = (MobileBy.ID, "toolbar_back")
    txtview_message = (MobileBy.ID,"tvMessage")
    btn_signin = (MobileBy.ID,"btnSignIn")
    btn_createnewaccount = (MobileBy.ID,"btnCreateAccount")

class Home_Screen():
    btn_leftmenu = (MobileBy.ID,"ivLeftMenu")
    txtview_helloname = (MobileBy.ID,"tvWelcome")
    btn_delivery = (MobileBy.ID,"selection_left")
    btn_collection = (MobileBy.ID, "selection_right")
    btn_viewcoupon = (MobileBy.ID,"btnViewCoupons")
    btn_viewmenu = (MobileBy.ID,"btnViewPromotions")

class Left_Menu():
    txtview_home = (MobileBy.XPATH,"//android.widget.TextView[@text ='Home']")
    txtview_signin = (MobileBy.XPATH, "//android.widget.TextView[@text ='Sign In']")
    txtview_language = (MobileBy.XPATH, "//android.widget.TextView[@text ='Language/言語']")
    txtview_language_jp = (MobileBy.XPATH, "//android.widget.TextView[@text ='言語/Language']")
    txtview_askquestion = (MobileBy.XPATH, "//android.widget.TextView[@text ='FAQ\'s']")
    txtview_customerservice = (MobileBy.XPATH, "//android.widget.TextView[@text ='Customer service']")
    txtview_privacypolicy = (MobileBy.XPATH, "//android.widget.TextView[@text ='Privacy Policy']")
    txtview_membership = (MobileBy.XPATH, "//android.widget.TextView[@text ='Membership T&C']")

class Language_Screen():
    btn_back = (MobileBy.ID, "toolbar_back")
    txtview_navigation = (MobileBy.ID,"toolbar_title")
    btn_jp = (MobileBy.XPATH,"//android.widget.TextView[@text = '日本語']")
    btn_en = (MobileBy.XPATH,"//android.view.ViewGroup[@index = 1]")





