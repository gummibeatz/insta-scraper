from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import json


chromedriver="/Users/Kenneth/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.instagram.com/")

driver.implicitly_wait(5000) 

iguserelem = driver.find_element_by_name("username")
iguserelem.send_keys("miskuoted")

igpwelem = driver.find_element_by_name("password")
igpwelem.send_keys("v4nhalen")
igpwelem.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

searchbox = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")
    )
)

driver.get("https://www.instagram.com/explore/tags/acl/")

searchbox = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")
    )
)
WebDriverWait(driver, 10)
element = driver.find_element_by_tag_name('div').find_element_by_tag_name('a').find_element_by_tag_name('div').find_element_by_tag_name('div').find_element_by_tag_name('img')
actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
WebDriverWait(driver, 10)
# Picture has been clicked

# Getting number of likes


# Get Likes-------------------
def get_like_element(): 
	try:
		return driver.find_element_by_xpath('//div[@class="'+'_iuf51 _oajsw'+'"]')
	except:
		return None

def get_number_of_likes():
	like_element = get_like_element()
	return like_element.text


# Get Views-----------------------
def get_view_element():
	try:
		return driver.find_element_by_xpath('//div[@class="'+'_iuf51 _3sst1'+'"]')
	except:
		return None

def get_number_of_views():
	view_element = get_view_element()
	return view_element.text


# Get User Location------------------
def get_location_element():
	try:
		return driver.find_element_by_xpath('//a[@class="'+'_kul9p _rnlnu'+'"]')
	except:
		return None

def get_user_location():
	location_element = get_location_element()
	if location_element:
		print location_element.text
	else: 
		print None

def show_all_comments():
	try:
		while driver.find_element_by_xpath('//button[@class="'+'_l086v _ifrvy'+'"]'):
			print "clicking load more"
			driver.find_element_by_xpath('//button[@class="'+'_l086v _ifrvy'+'"]').click()
			time.sleep(1)
	except:
		return None



def get_comments():
	user_comment_list = []

	users = driver.find_elements_by_xpath('//li[@class="'+'_nk46a'+'"]//a[@class="'+'_4zhc5 notranslate _iqaka'+'"]')
	for u in users:
		user_comment_list.append([u.text])

	comments = driver.find_elements_by_xpath('//li[@class="'+'_nk46a'+'"]//span')
	idx = 0
	for c in comments:
		user_comment_list[idx].append(c.text)
		idx+=1

	comment_dicts = [] 
	for uc in user_comment_list:
		comment = {}
		comment['user'] = uc[0]
		comment['comment'] = uc[1]
		comment_dicts.append(post)

	return comment_dicts





def get_user_name():
	print driver.find_element_by_xpath('//a[@class="'+'_4zhc5 notranslate _ook48'+'"]').text

def click_next_arrow():
	driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# opening file to write to
with open('acl_instagram.txt', 'a') as f:

	for i in xrange(2):
		dict = {}

		if get_like_element():
			dict['likes_count'] = get_number_of_likes()
		else: 
			dict['views_count'] = get_number_of_views()

		get_user_name()
		get_user_location()
		show_all_comments()
		dict['comments'] = get_comments()
		f.write(json.dumps(dict))
		f.write('\n')
		click_next_arrow()
		time.sleep(2)



driver.quit()





# like_element = driver.find_element_by_xpath('//span[@class="'+'_9jphp'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# like_element = driver.find_element_by_xpath('//span[@class="'+'_9jphp'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# like_element = driver.find_element_by_xpath('//span[@class="'+'_tf9x3'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# # Pull views

# like_element = driver.find_element_by_xpath('//span[@class="'+'_9jphp'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# like_element = driver.find_element_by_xpath('//span[@class="'+'_tf9x3'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# like_element = driver.find_element_by_xpath('//span[@class="'+'_tf9x3'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# # Pull non-numbered likes

# like_element = driver.find_element_by_xpath('//div[@class="'+'_iuf51 _oajsw'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()


# like_element1 = driver.find_element_by_xpath('//a[@class="'+'_tf9x3'+'"]')
# print like_element1

# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()



#element_list = len(like_element.find_elements_by_tag_name("span"))
# print element_list


# driver.find_element_by_id('pImage_0').click()

#.Click "xpath=//input[contains(@data-reactid, '$0.0.0.0.0.1.0')]"
#   .Type "xpath=//input[contains(@data-reactid, '$0.0.0.0.0.1.0')]", "5720 lansdowne ave Philadelphia, PA" 


#driver = webdriver.Firefox()
#driver.get("https://protonmail.com/")
#protonelem = driver.find_element_by_name("u")
#protonelem.send_keys("josiejosiejosie123")
#protonelem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source

#driver.implicitly_wait(5)

#loginelem = driver.find_element_by_name("password")
#loginelem.send_keys("v4nhalen")

#logincelem = driver.find_element_by_name("passwordc")
#logincelem.send_keys("v4nhalen")

#mailelem = driver.find_element_by_name("MBpassword")
#mailelem.send_keys("v4nhalen")

#mailcelem = driver.find_element_by_name("MBpasswordc")
#mailcelem.send_keys("v4nhalen")
#mailcelem.send_keys(Keys.RETURN)

#driver.implicitly_wait(5)

#recaptcha1elem = driver.find_element_by_name("11").click()

#driver.implicitly_wait(5)



#driver.get("https://docs.google.com/spreadsheets/d/1xIPLd7UgMcnmocbFfQRsOI58N1SOeDsy0pmsn2P5eAs/edit#gid=0");
#gmailelem = driver.find_element_by_name("Email")
#gmailelem.send_keys("kashmir276@gmail.com")
#gmailelem.send_keys(Keys.RETURN)

#driver.implicitly_wait(5)

#passwordelem = driver.find_element_by_name("Passwd")
#passwordelem.send_keys("Wordsworth69!")
#passwordelem.send_keys(Keys.RETURN)
#driver.findElement(By.xpath("//tr[@id='0-r-column-head-section$3']/td[4]")).click();
#driver.findElement(By.xpath("//table/tbody/tr/td[3]/div/div/div")).click();
#driver.findElement(By.xpath("//table/tbody/tr/td[3]/div/div/div")).sendKeys("Hello World!");
#driver.findElement(By.xpath("//tr[@id='0-r-column-head-section$3']/td[5]")).click();
