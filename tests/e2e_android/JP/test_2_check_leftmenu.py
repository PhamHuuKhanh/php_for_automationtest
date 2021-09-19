from src.app_android.JP.screens_jp import *
from src.app_android.action_android import *

def test_leftmenu_home():
    tap_on(Home_Screen.btn_leftmenu)
    tap_on(Left_Menu.txtview_home)
    assert get_text(Home_Screen.btn_viewmenu) == "View Pizza Menu"
def test_leftmenu_sigin():
    tap_on(Home_Screen.btn_leftmenu)
    tap_on(Left_Menu.txtview_signin)
    assert get_text(Signin_Screen.txtlink_forgotpass) == "Forgot your password?"
def test_leftmenu_language():
    tap_on(Signin_Screen.btn_back)
    tap_on(Home_Screen.btn_leftmenu)
    tap_on(Left_Menu.txtview_language) # the currently, it is English
    tap_on(Language_Screen.btn_jp) # change language from english to japanese
    assert get_text(Welcome_Screen.textview_title) == "アカウントを使って始めましょう"
    tap_on(Home_Screen.btn_leftmenu)
    tap_on(Left_Menu.txtview_language_jp)
    tap_on(Language_Screen.btn_en)





