from  selenium import webdriver
import pytest

class Testhtml():
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="")