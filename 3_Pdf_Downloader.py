import re
import time
import os
from playwright.sync_api import Playwright, sync_playwright, expect
import sys
sys.stdout.reconfigure(encoding='utf-8')

file_name = 'PDF_URLs_5567.txt'

# Read the content of the text file into a list
with open(file_name, 'r') as file:
    url_list = [line.strip() for line in file.readlines()]

for index, url in enumerate(url_list, start=1):
    if index < 71:
        print(index)

    else:
        website = url
        # website = 'https://www.itb.com/en/itb-berlin-for-visitors/exhibitor-list/#/detail/007traveller--31462307'
        # save_path = r'C:\Users\SIVA RANJJAN\PycharmProjects\pythonLearning\ITB-pdf_downloadMethod\traveller.pdf'
        # save_path = os.path.normpath(save_path)

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                        '110.0.0.0 Safari/537.36'
        }


        def run(playwright: Playwright) -> None:
            browser = playwright.chromium.launch(headless=False, slow_mo=50)
            context = browser.new_context()
            page = context.new_page()
            page.goto(website)
            page.get_by_test_id("uc-accept-all-button").click()
            time.sleep(2)
            element_text = page.inner_text(".gwt-HTML.EWP5KKC-y-tc.EWP5KKC-y-eb")
            cleaned_element = re.sub(r'[^\w\s]', '', element_text)
            print(index, "-", element_text)
            with page.expect_download() as download_info:
                page.locator(".EWP5KKC-Q-b > div").first.click()
            download = download_info.value
            time.sleep(5)
            save_path = r'C:\Users\SIVA RANJJAN\PycharmProjects\pythonLearning\ITB-pretiffy_VsCode\PDF_Files\{}.pdf'.format(cleaned_element)
            save_path = os.path.normpath(save_path)
            download.save_as(save_path)

            # ---------------------
            time.sleep(5)
            context.close()
            browser.close()


        with sync_playwright() as playwright:
            run(playwright)

print("All PDF files downloaded")
# Find all <a> tags with href attributes that end with ".pdf"
# pdf_links = response.html.find(".gwt-HTML EWP5KKC-Q-f")
# print(len(pdf_links))
# for links in pdf_links:
#     print(links)
