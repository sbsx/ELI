# import required libraries
import sys
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def main(argv):
    # argv is a list of twitter links
    print("---------------------------------------")

    print('Number of arguments:', len(argv), 'arguments.')
    print('Argument List:', str(argv))
    print("---------------------------------------")
    with open('data.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            ["Author Name", "Published Date", "Article Content"])

        for url in argv:
            # get url with webdriver
            wd = webdriver.Chrome()
            wd = webdriver.Chrome()
            wd.get(url)
            time.sleep(2)

            # run webdriver and scroll to bottom to load entire html
            wd.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            # get html
            html = BeautifulSoup(wd.page_source, "html.parser")

            # with open('data.csv', 'a', newline='') as file:
            # writer = csv.writer(file, delimiter=',',
            #                     quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # writer.writerow(
            #     ["Author Name", "Published Date", "Article Content"])
            # get author name

            print("   ")
            author = html.find('meta', attrs={'name': 'author'})
            author_name = author["content"]
            print(author_name)

            print("    ")
            publish_date = html.find(
                'meta', attrs={'property': 'article:published_time'})
            date = publish_date["content"].split('T')[0]
            print(date)

            print("    ")
            paragraphs = html.find_all("p", "pw-post-body-paragraph")
            content = ""
            for paragraph in paragraphs:
                content += paragraph.get_text()
                content += '\n'

            print(content)

            row = [str(author_name), str(date), str(content)]
            writer.writerow(row)


    #'date', 'title', 'subtitle', 'claps', 'responses', 'author_url', 'story_url', 'reading_time (mins)',
if __name__ == "__main__":
    main(sys.argv[1:])
