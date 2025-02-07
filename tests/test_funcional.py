from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True # Executar em modo headless
    driver = webdriver.Firefox(options=options)
    # Iniciar o webdriver usando geckodriver
    driver.set_page_load_timeout(5)
    yield driver

    driver.quit()
    process.kill()


def test_app_opens(driver):
    # verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(5)



