from sets import Set
from insta_scraper_methods import *
from os.path import join, dirname
from dotenv import load_dotenv
import json
import pdb

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# opening file to write to
# f is the file it's gonna write to
def grab_user_post(f, driver):
    dict = {}

    if get_like_element(driver):
        dict['likes_count'] = get_number_of_likes(driver)
    else: 
        dict['views_count'] = get_number_of_views(driver)

    dict['user'] = get_user_name(driver)
    dict['post_time'] = get_post_time(driver)
    dict['post_location'] = get_user_location(driver)
    show_all_comments(driver)
    dict['comments'] = get_comments(driver)

    f.write(json.dumps(dict))
    f.write('\n')
# ----------------------------

# Define driver
chromedriver = os.environ['chromedriver_path']
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(1)
# ----------------------------

# THIS IS THE ALGORITHM!!!!!!
username = os.environ['username']
password = os.environ['password']

open_instagram(driver)
time.sleep(2)
login(driver, username, password)
time.sleep(5)


# Search based on tag
visible_element(driver, r"""//input[@placeholder='Search']""")

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
# ----------------------------

# Finds the TOTAL number of hashtags
stop = driver.find_element_by_xpath('//span[@class="'+'_bkw5z'+'"]').text
stop = stop.replace(',', '')
stop = int(stop)
stop -= 1
print 'stopCount = {}'.format(stop)
# ----------------------------


# Click "Load More" button
driver.find_element_by_xpath('//a[@class="'+'_oidfu'+'"]').click()
time.sleep(1)
# ----------------------------


# new algo for grabbing images
with open('acl_instagram_testand.txt', 'a') as f:
    post_src_set = Set()
    # get image paths
    while(len(post_src_set) < stop):
        nodes = driver.find_elements_by_xpath('//div[@class="'+'_ovg3g'+'"]')
        # get last element of selected nodes
        node_count = len(nodes)
        node_count_offset = 1 
        node = nodes[node_count - node_count_offset]
        node.click()
        time.sleep(0.5)
        # check get image src value
        post_src_value = get_post_src_value(driver)

        while((post_src_value not in post_src_set) and (node_count_offset <= node_count)):
            post_src_set.add(post_src_value)
            grab_user_post(f, driver)
            click_left_arrow(driver)
            time.sleep(0.5)
            post_src_value = get_post_src_value(driver)
            node_count_offset += 1
       	click_exit_button(driver)
        scroll_until_more_loaded(driver)
