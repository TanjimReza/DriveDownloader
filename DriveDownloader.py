import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

direct_dl_links = []


def create_download_links():
    global direct_dl_links
    try:
        with open('links.txt') as f:
            links = f.readlines()
            links = [x.strip() for x in links]
            direct_dl_links = []
            for i, link in enumerate(links, start=1):
                direct_dl_link = f"https://drive.google.com/uc?export=download&id={link.split('id=')[1]}"
                direct_dl_links.append(direct_dl_link)
                print(
                    f"\rPreparing download links {i} out of {len(links)}", end="")
    except Exception as e:
        print(f"Error: {e}")


chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=C:/Users/Tanjim/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--profile-directory=Profile 1")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)


def download_files():
    try:
        for i, link in enumerate(direct_dl_links, start=1):
            driver.get(link)
            time.sleep(3)
            print(
                f"\rDownloaded {i} out of {len(direct_dl_links)} files", end="")
        driver.quit()
    except Exception as e:
        print(f"Error: {e}")


start_time = time.time()
print(":: Creating download links")
create_download_links()
print("\n:: Download links created")
download_files()
print("\n== All files downloaded ==")
print(f"\nTotal time taken: {time.time() - start_time:.2f} seconds")
