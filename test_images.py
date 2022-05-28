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
  punisher = 'https://the-internet.herokuapp.com/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg'
  punisher_exists = False

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

  if image1 == punisher:
    print(f"Punisher is image1")
    punisher_exists = True
  if image2 == punisher:
    print(f"Punisher is image2")
    punisher_exists = True
  if image3 == punisher:
    print(f"Punisher is image3")
    punisher_exists = True
  if not punisher_exists:     
    print("Punisher is NOT present")

  assert not punisher_exists, "FAIL: punisher image exists"
