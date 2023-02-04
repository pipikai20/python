# Scrapy settings for dangdangwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dangdangwang'

SPIDER_MODULES = ['dangdangwang.spiders']
NEWSPIDER_MODULE = 'dangdangwang.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'dangdangwang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Cookie': 'ddscreen=2; __permanent_id=20201225221223687428842630081187064; __visit_id=20201225221223688712904722174364479; __out_refer=; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; permanent_key=20201225221415625154699163d653ff; __rpm=s_112100...1608905653450%7Clogin_page.login_password_div..1608905676002; USERNUM=D930hrYbWQosyBwJxM432g==; login.dangdang.com=.AYH=2020122522141612165387137&.ASPXAUTH=cYOVsMG1t27kkEmt3+x05uLsD3lN3hPcq53RAQHFpu2UhV8fwRlliQ==; dangdang.com=email=MTc3MDkzNTI1NDIzNzEzMUBkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname=&display_id=3908454307627&customerid=ZaMtnF1tG3t7J6MLB9kDBQ==&viptype=saCR2Pu2/G0=&show_name=177%2A%2A%2A%2A2542; ddoy=email=1770935254237131%40ddmobilphone__user.com&nickname=&agree_date=1&validatedflag=0&uname=17709352542&utype=1&.ALFG=on&.ALTM=1608905677; sessionID=pc_104514eabe9b231b2ad2418c10715b1e1b5aed54d075d0807277ae9e9f4e0cb4; __dd_token_id=20201225221437336152975753cec768; search_passback=6237d527093726a5cef3e55ffc01000024236700ccf3e55f; LOGIN_TIME=1608905678625; __trace_id=20201225221438635468955891871230342; pos_9_end=1608905678783; pos_0_start=1608905678892; pos_0_end=1608905678899; ad_ids=4343831%2C3644144%2C3379105%7C%233%2C3%2C1'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'dangdangwang.middlewares.DangdangwangSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'dangdangwang.middlewares.DangdangwangDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'dangdangwang.pipelines.DangdangwangPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

