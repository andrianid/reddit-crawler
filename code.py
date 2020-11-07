from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chromedriver = "D:/2nd/SMM/Assignment1/chromedriver_win32/chromedriver"
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
driver.implicitly_wait(60)
driver.get("http://www.reddit.com")

search_bar = driver.find_element_by_id("header-search-bar")
search_bar.send_keys("Covid-19")
search_bar.send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[1]/div/div/a[2]""").click()
driver.find_element_by_id("search-results-sort").click()
driver.find_element_by_xpath("""/html/body/div[4]/div/a[2]/button""").click()

with open("result.xml", "w", encoding="utf-8") as writer:
    posts = driver.find_elements_by_class_name("_eYtD2XCVieq6emjKBH3m")
    writer.write("<xml>\n")
    for i in range(0,3):
        writer.write("  <post>\n")
        writer.write("    <title>" + posts[i].text + "</title>\n")
        posts[i].click()

        try:
            body = driver.find_element_by_class_name("_3xX726aBn29LDbsDtzr_6E_1Ap4F5maDtT1E1YuCiaO0r D3IL3FD0RFy_mkKLPwL4")
            writer.write("    <content>" + body + "</content>\n")

            comments = driver.find_elements_by_class_name("_1qeIAgB0cPwnLhDF9XSiJM")

            for j in range(0,3):
                writer.write("    <comment>" + comments[j].text + "</comment>\n")
            driver.find_element_by_xpath("""//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div/div[1]/div/div[2]/button""").click()
            writer.write("  </post>\n")

        except NoSuchElementException:
            writer.write("    <content></content>\n")
            comments = driver.find_elements_by_class_name("_1qeIAgB0cPwnLhDF9XSiJM")

            for j in range(0,3):
                writer.write("    <comment>" + comments[j].text + "</comment>\n")
            driver.find_element_by_xpath("""//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[3]/div/div[1]/div/div[2]/button""").click()
            writer.write("  </post>\n")

    writer.write("</xml>\n")