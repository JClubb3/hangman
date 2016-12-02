from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
actions = ActionChains(driver)

# "dryad", "grimrog", "blood_priest", "astronomer", "herald_of_insight",
# "psychopomp", "alchemist", "stormcaller", "seeker", "engineer", "nomad"
# "gunner", "igniter", "sentinel", "metal_warden", "guardian", "thorn"
# "inhibitor", "vanguard", "glutton", "headhunter", "reaver", "stalker"
# "ravener", "ranid_assassin", "spear_master"

bloodlines = ["harbinger"]

for bloodline in bloodlines:
    icons = []
    boxes = []
    url = "https://web.archive.org/web/20130420063334/http://www.bloodlinechampions.com/bloodline_{0}.php".format(bloodline)
    driver.get(url)
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bloodline_flash_object")))
    
    icons = driver.find_elements_by_class_name('bl_ability_tooltip')
    boxes = driver.find_elements_by_class_name('ability_tooltip')
    title = driver.title
    with open('bloodlines.txt', 'a') as open_file:
        open_file.write("\n")
        open_file.write(title[35:])
        open_file.write("\n")

    x = 0
    for icon in icons:
        actions.move_to_element(icon)
        actions.move_to_element_with_offset(boxes[0],0,0)
        actions.perform()
        toprint = boxes[x].text
        x += 1
        with open('bloodlines.txt', 'a') as open_file:
            open_file.write(toprint)
            open_file.write("\n")
        if x == 7:
            break
    print("{0} done.".format(bloodline.title()))
    driver.close()

