# -*- coding: utf-8 -*-
import os
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class VehiclesSpider(CrawlSpider):
    name = 'vehicles_spider'
    allowed_domains = ['https://www.sunarp.gob.pe/']
    start_urls = [
        'https://www.sunarp.gob.pe/seccion/servicios/detalles/0/c3.html'
        ]


    def __init__(self):

        rutaFX = os.environ['FIREFOX_HOME']
        print(rutaFX + r'\firefox.exe')
        # Ubicacion del firefox.exe
        binary = FirefoxBinary(rutaFX + r'\firefox.exe')
        # Nombre del archivo a exportar
        profile = webdriver.FirefoxProfile()
        profile.set_preference("dom.disable_beforeunload", True)
        options = Options()
        options.add_argument("--headless")
        profile.set_preference("browser.tabs.remote.autostart", False)
        profile.set_preference("browser.tabs.remote.autostart.1", False)
        profile.set_preference("browser.tabs.remote.autostart.2", False)
        profile.set_preference("browser.tabs.remote.force-enable", False)
        self.driver = webdriver.Firefox(firefox_options=options,
                                        firefox_profile=profile,
                                        firefox_binary=binary,
                                        executable_path='../geckodriver.exe')

    def parse_item(self, response):
        self.driver.get(response.url)
        next = self.driver.find_element_by_xpath("//a")
        try:
            next.click()
        except:
            print("closing driver")
            self.driver.close()
        i = {}
        return i
