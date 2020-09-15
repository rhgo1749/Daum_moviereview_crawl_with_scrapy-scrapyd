# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bigcrawler'

SPIDER_MODULES = ['bigcrawler.spiders']
NEWSPIDER_MODULE = 'bigcrawler.spiders'

# Url 크롤링시 Pipeline 설정
ITEM_PIPELINES = {'bigcrawler.pipelines.TextPipeline': 300, }

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

LOG_LEVEL = 'INFO'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1024
FEED_EXPORT_ENCODING = 'utf-8'

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.05

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1024
CONCURRENT_REQUESTS_PER_IP = 1024

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
RETRY_ENABLED = False
DOWNLOAD_TIMEOUT = 30
REDIRECT_ENABLED = False
AJAXCRAWL_ENABLED = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'crawler (+http://www.yourdomain.com)'
