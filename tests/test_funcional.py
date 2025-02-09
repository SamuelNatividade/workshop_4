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


def test_check_title_is(driver):
    driver.get("http://localhost:8501")
    sleep(2)
    page_title = driver.title

    expected_title = "Validador de Schema Excel"
    assert page_title == expected_title

def test_check_streamlit_h1(driver):
    driver.get("http://localhost:8501")

    sleep(2)

    h1_element = driver.find_element(By.TAG_NAME, "h1")
    excepted_text = "Insira o arquivo Excel que deseja validar"
    assert h1_element.text == excepted_text
    






