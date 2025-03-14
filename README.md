Multithreaded Web Crawler
=========================

Overview
--------
This is a Python-based Multithreaded Web Crawler that efficiently fetches and parses web pages using multiple threads. It speeds up web scraping by making concurrent HTTP requests.

Features
--------
- **Multithreading:** Fetch multiple pages concurrently.
- **Efficient Data Extraction:** Extracts links, text, and other data.
- **Customizable Depth:** Control how deep the crawler explores.
- **Domain Handling:** Manages crawling across multiple domains.

Installation
------------
1. Clone the Repository:
   git clone https://github.com/SANJAYSS-SRM-26/Multithreaded-Web-Crawler.git
   cd Multithreaded-Web-Crawler

2. Set Up a Virtual Environment:
   python -m venv env
   source env/bin/activate  (Windows: env\Scripts\activate)

3. Install Dependencies:
   pip install -r requirements.txt

Usage
-----
1. Modify `config.py` to set:
   - Start URL
   - Crawl depth
   - Number of threads

2. Run the Crawler:
   python crawler.py

3. View Results:
   - Output is saved in the `output/` directory.

Project Structure
-----------------
Multithreaded-Web-Crawler/
├── crawler.py           # Main crawler implementation
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── output/              # Directory for crawl results
└── README.txt           # Project documentation

Technologies Used
-----------------
- Python
- Multithreading (threading module)
- Requests (for HTTP requests)
- BeautifulSoup (for HTML parsing)

Contributing
------------
Contributions are welcome! Fork this repository, improve the crawler, and submit a pull request.

License
-------
This project is licensed under the MIT License.

GitHub Repository: https://github.com/SANJAYSS-SRM-26/Multithreaded-Web-Crawler
