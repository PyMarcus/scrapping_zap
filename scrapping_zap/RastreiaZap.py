from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class RastreiaZap:

    # atributo de classe
    __site = "https://web.whatsapp.com/"

    # construtores
    def __init__(self, novo_site=__site):
        self.__novo_site = novo_site

    def __int__(self):
        pass

    @property
    def novo_site(self):
        return self.__novo_site

    @novo_site.setter
    def novo_site(self, new):
        self.__novo_site = new

    # métodos de classe
    @classmethod
    def start(cls):
        """Método que pesquisa os números que não foram adicionados"""
        global set
        path = Service('./chromedriver')
        driver = webdriver.Chrome(service=path)
        try:
            driver.get(RastreiaZap.__site)
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "app")))
            finally:
                set = set()
                time.sleep(15)
                driver.find_element(By.XPATH, "//div[@role='textbox']").click()
                time.sleep(1)
                # roda scroll do zap para ir atualizando o javascript
                for n in range(0, 50, 2):
                    driver.find_element(By.XPATH, "//div[@role='textbox']").send_keys(f"{Keys.DOWN}" * n)
                    for _numeros in driver.find_elements(By.XPATH, "//div[@class='zoWT4']//span[@dir='auto']"):
                        string = str(_numeros.text)
                        if string.startswith("+55"):  # filtra números de telefone
                            set.add(string)  # adiciona números em set para não repetí-los
                    time.sleep(5) # de 5segundos ele gira o scroll
                time.sleep(1)

                print(set)
                return set

        except NoSuchElementException:
            print("Erro no tempo da página")
            return None


if __name__ == '__main__':
    run = RastreiaZap()
    retorno = run.start()
