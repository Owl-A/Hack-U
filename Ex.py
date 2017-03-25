from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
file = open("Database.txt","w")

driver = webdriver.Chrome()
driver.get("http://moodfuse.com/")

def select_mood(mood):
	file.write(mood)
	drop_down = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id("mood"))
	Select(drop_down).select_by_visible_text(mood)

def select_genre(genre):
	file.write(genre+ " ")
	drop_down = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id("style"))
	Select(drop_down).select_by_visible_text(genre)

def get_songs():
	button = driver.find_element_by_id("submit")
	button.click()
	songl = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="playlist"]/div[1]'))
	song = songl.text
	s = '//*[@id="playlist"]/div['
	for i in range(2,11):
		file.write(song+", ")
		s = s+str(i)+']'
		song = driver.find_element_by_xpath(s).text
		s = '//*[@id="playlist"]/div['
	file.write("\n")
		
select_mood("angry")
select_genre("Hip-Hop")
get_songs()
select_mood("sad")
select_genre("Punk Metal")
get_songs()
select_mood("happy")
select_genre("Pop/Rock")
get_songs()
select_mood("calming")
select_genre("Jazz")
get_songs()
driver.quit()


