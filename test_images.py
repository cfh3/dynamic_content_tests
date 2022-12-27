import pytest, time
from selenium.webdriver import Chrome
from dynamic_content_page import DynamicContentPage

@pytest.fixture
def browser():
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

def test_images(browser):
  storm_trooper = 'https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-6.jpg'
  storm_trooper_exists = False

  dynamic_content = DynamicContentPage(browser)
  dynamic_content.load()

  # This isn't necessary but allows you to see the images
  time.sleep(3)

  image1 = dynamic_content.get_image_one()
  image2 = dynamic_content.get_image_two()
  image3 = dynamic_content.get_image_three()
    
  print(f"src 1: {image1}")
  print(f"src 2: {image2}")
  print(f"src 3: {image3}")

  if image1 == storm_trooper:
    print(f"storm_trooper is image1")
    storm_trooper_exists = True
  if image2 == storm_trooper:
    print(f"storm trooper is image2")
    storm_trooper_exists = True
  if image3 == storm_trooper:
    print(f"storm trooper is image3")
    storm_trooper_exists = True
  if not storm_trooper_exists:     
    print("storm trooper is NOT present")

  assert not storm_trooper_exists, "FAIL: storm trooper image exists"
