from selenium import webdriver

def refuse_to_connect(url):
    try:
        driver = webdriver.Chrome()  # Or any other webdriver you prefer
        driver.get(url)
    except Exception as e:
        print("Error:", e)
    finally:
        print("Refused to connect")

if __name__ == "__main__":
    website_url = "http://example.com"  # Replace with the URL you want to refuse to connect to
    refuse_to_connect(website_url)
