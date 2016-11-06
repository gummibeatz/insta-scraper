from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


# Open Instagram
def open_instagram(driver):
	driver.get("https://www.instagram.com/")
	driver.implicitly_wait(5000) 
# ----------------------------


# Log in as "Miskuoted"
def login(driver):
	iguserelem = driver.find_element_by_name("username")
	iguserelem.send_keys("miskuoted")
	igpwelem = driver.find_element_by_name("password")
	igpwelem.send_keys("v4nhalen")
	igpwelem.send_keys(Keys.RETURN)
	driver.implicitly_wait(5)
# ----------------------------


# Wait until element is visible
def visible_element(driver, xpath, timeout=10):
	WebDriverWait(driver, timeout).until(
	    EC.visibility_of_element_located(
	        (By.XPATH, xpath)
	    )
	)

# Checks to see if there are likes
def get_like_element(driver): 
    try:
        return driver.find_element_by_xpath('//div[@class="'+'_iuf51 _oajsw'+'"]')
    except:
        return None
# ----------------------------


# Gets number of likes
def get_number_of_likes(driver):
    like_element = get_like_element(driver)
    return like_element.text
# ----------------------------


#Checks to see if these are the views
def get_view_element(driver):
    try:
        return driver.find_element_by_xpath('//div[@class="'+'_iuf51 _3sst1'+'"]')
    except:
        return None
# ----------------------------


# Gets the number of views
def get_number_of_views(driver):
    view_element = get_view_element(driver)
    return view_element.text
# ----------------------------


# Checks to see if this is an image
def get_image_element(driver): 
    try:
        return driver.find_element_by_xpath('//div[@class="_jjzlb"]/img[@src]')
    except:
        return None
# ----------------------------


# Checks to see if this is a video
def get_video_element(driver): 
    try:
        return driver.find_element_by_xpath('//div[@class="_2tomm"]/img[@src]')
    except:
        return None
# ----------------------------


# Gets image src element
def get_element_src_value(element):
    return element.get_attribute('src')
# ----------------------------


# Gets post src element
def get_post_src_value(driver):
	image_element = get_image_element(driver)
        video_element = get_video_element(driver)
	if image_element:
		return get_element_src_value(image_element)
	else:
		return get_element_src_value(video_element)
# ----------------------------


# Gets last pImage id
def get_last_p_image_tag(driver): 
    pImage = driver.find_elements_by_xpath('//div[@class="_jjzlb"]/img[@id]')[-1]
    return pImage.get_attribute('id')
# ----------------------------


# Checks to see if there is a user location
def get_location_element(driver):
    try:
        return driver.find_element_by_xpath('//a[@class="'+'_kul9p _rnlnu'+'"]')
    except:
        return None
# ----------------------------

# Gets the user location
def get_user_location(driver):
    location_element = get_location_element(driver)
    if location_element:
        return location_element.text
    else: 
        return None
# ----------------------------

#Clicks "Show more comments" button
def show_all_comments(driver):
    try:
        while driver.find_element_by_xpath('//button[@class="'+'_l086v _ifrvy'+'"]'):
            driver.find_element_by_xpath('//button[@class="'+'_l086v _ifrvy'+'"]').click()
            time.sleep(0.5)
    except:
        return None
# ----------------------------


# Gets all of the comments
def get_comments(driver):
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
        comment_dicts.append(comment)

    return comment_dicts
# ----------------------------

#Gets the post time
def get_post_time(driver):
    return driver.find_element_by_xpath('//time[@class="'+'_379kp'+'"]').get_attribute("datetime")
# ----------------------------


# Gets the OP username
def get_user_name(driver):
    return driver.find_element_by_xpath('//a[@class="'+'_4zhc5 notranslate _ook48'+'"]').text
# ----------------------------


# Scrolls down
def scroll_down(driver):
    print 'scrolling down'
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
# ----------------------------

# Scrolls up
def scroll_up(driver):
    print 'scrolling up'
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
# ----------------------------


# CLICK right arrow
def click_next_arrow(driver):
	driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()
# ----------------------------


# PRESS right arrow
def right_arrow_press(driver):
	right_arrow = driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]')
	right_arrow.send_keys(Keys.ARROW_RIGHT)
# ----------------------------


# CLICK left arrow
def click_left_arrow(driver):
	driver.find_element_by_xpath('//a[@class="'+'_qdy3e coreSpriteLeftPaginationArrow'+'"]').click()
# ----------------------------


# CLICK exit button
def click_exit_button(driver):
	driver.find_element_by_xpath('//button[@class="'+'_3eajp'+'"]').click()
# ----------------------------


# Scrolls until more images are loaded
def scroll_until_more_loaded(driver):
    last_p_image_tag = None
    current_p_image_tag = get_last_p_image_tag(driver)
    while(current_p_image_tag == last_p_image_tag):
        last_p_image_tag = current_p_image_tag
        scroll_up(driver)
        scroll_down(driver)
        current_p_image_tag = get_last_p_image_tag(driver)
# ----------------------------

