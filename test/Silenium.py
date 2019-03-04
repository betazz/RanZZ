from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def one_arg():
	binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')
	driver = webdriver.Firefox(executable_path = '/Users/zingarazbarragan/Downloads/geckodriver',firefox_binary=binary)
	driver.get("http://www.python.org")
	assert "Python" in driver.title
	elem = driver.find_element_by_name("q")
	elem.clear()
	elem.send_keys("pycon")
	elem.send_keys(Keys.RETURN)
	assert "No results found." not in driver.page_source
	driver.close()
	

if __name__ == '__main__':
	one_arg()
 

