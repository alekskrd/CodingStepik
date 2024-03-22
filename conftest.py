import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)  # autouse будет использоваться автоматически для каждого теста, нам не надо ее нигде вызывать, прописывать.
# scope Будет создаваться каждый раз экземпляр. т.е.браузер для каждого теста будет создаваться отдельно
def driver(request):
    options = Options()
    options.add_argument("--headless")  #без интерфейса
    options.add_argument("--no--sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()
