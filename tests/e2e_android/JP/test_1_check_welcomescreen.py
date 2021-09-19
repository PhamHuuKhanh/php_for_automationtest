from src.app_android.JP.screens_jp import *
from src.app_android.action_android import *

def test_changelaguage():
    current_language = get_text(Welcome_Screen.txtview_language)
    if(current_language == "日本語"):
        assert get_text(Welcome_Screen.textview_title) == "アカウントを使って始めましょう"
        tap_on(Welcome_Screen.btn_changelaguage)
        tap_on(Welcome_Screen.language_en)
        assert get_text(Welcome_Screen.textview_title) == "Use your account to get started"
    elif(current_language == "English"):
        assert get_text(Welcome_Screen.textview_title) == "Use your account to get started"
        tap_on(Welcome_Screen.btn_changelaguage)
        tap_on(Welcome_Screen.language_jp)
        assert get_text(Welcome_Screen.textview_title) == "アカウントを使って始めましょう"
        tap_on(Welcome_Screen.btn_changelaguage)
        tap_on(Welcome_Screen.language_en)
def test_btn_signinsignup():
    tap_on(Welcome_Screen.btn_signin_signup)
    assert get_text(Signin_Screen.txtlink_forgotpass) == "Forgot your password?-"
def test_btn_getcoupon():
    tap_on(Signin_Screen.btn_back)
    tap_on(Welcome_Screen.btn_getcpupon)
    assert get_text(Mycoupon_Screen.txtview_message) == "Please log in or create a new account to enjoy coupon(s)"
def test_btn_gotomenu():
    tap_on(Mycoupon_Screen.btn_back)
    tap_on(Welcome_Screen.btn_gotomenu)

