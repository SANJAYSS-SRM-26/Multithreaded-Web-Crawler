import multiprocessing
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
import requests

def worker():
    print("Child process is running.")

class MultiThreadedCrawler:

    def __init__(self, seed_url, max_pages=50):
        self.seed_url = seed_url
        self.root_url = '{}://{}'.format(urlparse(self.seed_url).scheme, urlparse(self.seed_url).netloc)
        self.pool = ThreadPoolExecutor(max_workers=5)
        self.scraped_pages = set([])
        self.crawl_queue = Queue()
        self.crawl_queue.put(self.seed_url)
        self.max_pages = max_pages
        self.pages_crawled = 0

    def get_website_info(self):
        try:
            res = requests.get(self.seed_url, timeout=(3, 30))
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                title = soup.title.string if soup.title else "No title found"
                meta_description = soup.find("meta", attrs={"name": "description"})
                description = meta_description.get("content") if meta_description else "No description found"

                print(f'\n <---Website Information--->\n')
                print(f'Title: {title}')
                print(f'Description: {description}\n')

        except requests.RequestException as e:
            print(f'Error retrieving website information: {e}')

    def parse_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        Anchor_Tags = soup.find_all('a', href=True)
        for link in Anchor_Tags:
            url = link['href']
            if url.startswith('/') or url.startswith(self.root_url):
                url = urljoin(self.root_url, url)
                if url not in self.scraped_pages:
                    self.crawl_queue.put(url)

    def scrape_info(self, html):
        soup = BeautifulSoup(html, "html5lib")
        web_page_paragraph_contents = soup('p')
        text = ''
        for para in web_page_paragraph_contents:
            if not ('https:' in str(para.text)):
                text = text + str(para.text).strip()
        print(f'\n <---Text Present in The WebPage is --->\n', text, '\n')
        return

    def post_scrape_callback(self, res):
        result = res.result()
        if result and result.status_code == 200:
            self.parse_links(result.text)
            self.scrape_info(result.text)

    def scrape_page(self, url):
        try:
            res = requests.get(url, timeout=(3, 30))
            return res
        except requests.RequestException:
            return

    def run_web_crawler(self):
        while self.pages_crawled < self.max_pages:
            try:
                print("\n Name of the current executing process: ",
                      multiprocessing.current_process().name, '\n')
                target_url = self.crawl_queue.get(timeout=60)
                if target_url not in self.scraped_pages:
                    print("Scraping URL: {}".format(target_url))
                    self.current_scraping_url = "{}".format(target_url)
                    self.scraped_pages.add(target_url)
                    job = self.pool.submit(self.scrape_page, target_url)
                    job.add_done_callback(self.post_scrape_callback)

            except Empty:
                return
            except Exception as e:
                print(e)
                continue

    def info(self):
        print('\n Seed URL is: ', self.seed_url, '\n')
        print('Scraped pages are: ', self.scraped_pages, '\n')


if __name__ == '__main__':
    user_input_url = input("Enter the website URL to be crawled: ")
    max_pages_to_crawl = 10
    cc = MultiThreadedCrawler(user_input_url, max_pages_to_crawl)

    # Start the child process
    child_process = multiprocessing.Process(target=worker)
    child_process.start()

    cc.get_website_info()  # Retrieve website information before crawling
    cc.run_web_crawler()
    cc.info()

    # Wait for the child process to finish
    child_process.join()


