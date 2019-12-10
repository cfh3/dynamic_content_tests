import pytest
from selenium.webdriver import Chrome
from dynamic_content_page import DynamicContentPage

@pytest.fixture
def browser():
  driver = Chrome()
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

def test_word_lengths(browser):
    word_length = 10
    word_of_specified_length_exists = False
    
    dynamic_content = DynamicContentPage(browser)
    dynamic_content.load()
    
    p1 = dynamic_content.get_paragraph_one_text()
    p2 = dynamic_content.get_paragraph_two_text()
    p3 = dynamic_content.get_paragraph_three_text()
    
    all_words_string = p1.replace('.', ' ') + p2.replace('.', ' ') + p3.replace('.', ' ')

    all_words_list = all_words_string.split()
    
    for word in all_words_list:
        if len(word) >= word_length:
            word_of_specified_length_exists = True
            break
    
    assert word_of_specified_length_exists, f"FAIL: no words of length {word_length} or greater"
    
    all_words_dict = {}
    for word in all_words_list:
        all_words_dict[word] = len(word)

    longest_word = max(all_words_dict, key=all_words_dict.get)
    print(f"The longest word is {longest_word} and is {len(longest_word)} characters")