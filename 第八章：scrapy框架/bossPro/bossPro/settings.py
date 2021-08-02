# Scrapy settings for bossPro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bossPro'

SPIDER_MODULES = ['bossPro.spiders']
NEWSPIDER_MODULE = 'bossPro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71'

LOG_LEVEL = 'ERROR'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   'Cookie': '_bl_uid=7zk0hq3m00m79zmdI9XwgaXw9qy9; __zp_seo_uuid__=451adcaa-633d-4c9a-93d3-bab7eb417c72; sid=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1627441702; lastCity=100010000; __g=sem; __l=r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Furl%3Da00000KEJeCxDFezE_JaHSdcqc-Haz5Eq2zOsfLcG25emnzN9V428csrOavzpQ_KhLdn4_3CbnQy_WwlfH93G6Y9QNZCtmHeeDuU1Th-E2SSOd_x6WiQWgDKRosPG6eV_ehz_rZ7D_ZJUraSBaMqnntlasA0eObUqwsKMClNnT3TJBXBs8d47rP-9vyC9DoudHr3vjX-Hs6OJ_E6vJNbO5-Kau3q.Db_NR2Ar5Od663rj6t8AGSPticrZA1AlaqM766WHGek3hcYlXE_sgn8mE8kstVerQKMks4OgSWS534Oqo4yunOogEOtZV_zyUr1oWC_knmx5I9LtTrzEj4SrZuEse59sSX1jexo9vxQ5jWl3cMYAn5M8seSrZug9tOZj_L3IMs4t5MEseQnrOv3x5kseS1jeIMgVHC3ZHgng8WWlsk8sHfGmEIjfEl1F8xnhA6kNfCm3t5Zv3TMds45osTZK4TPHtU3b2pMpRt85R_nYQZuvU2S-f0.U1Yk0ZDqmhq1TsKspynqn0KY5yFETLn0pyYqnWcd0ATqUvNsT100Iybqmh7GuZR0TA-b5H60mv-b5Hnsn6KVIjYknjD4g1DsnHIxn1Dzn7t1nj0zg1DsnWPxn1msnfKopHYs0ZFY5HTsn0KBpHYkPH9xnW0Yg1ckPdtdnjn0UynqnH6vn1DLnWmdn-tkrH03rjbYP1TYg1Dsn-tknjFxnNts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qnHnknHRknW0LP0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1QyIlUMn0pywW5R9rf6KspZw45fKYmgFMugfqPWPxn7tkPH00IZN15HDsPWDsP1cYPHmdPHc4nH0zPWcv0ZF-TgfqnHmzP1fYnHm4PH6YnsK1pyfqmWRvPWFWrAmsnj0snyR4m6KWTvYqfWn1f17AnbwDwDu7nW0knfK9m1Yk0ZK85H00TydY5H00Tyd15H00uANYgvPsmHYs0ZGY5H00UyPxuMFEUHYsg1Kxn7tknjfvg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1KxPjnknjb4PNtYn1DsrHbdg1Kxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0A-1mvsqn0K9uAu_myTqnfK_uhnqn0KbmvPb5Hb1PW-Arjmkf1PAfWTYPW61nD7aPDuanRPjPHN7P1T3wj6LwDR4fWNKwb9nwDkcwRFnH0KYTh7buHYLPW0znjc0mhwGujYswHfdrRf3fYDLwDP7njT1nHDkPbnLwHf4fWmznbNarfKEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYzc10WnH0WnBn1PjmkrHnkn10WnH0snanknj0sQW0snj0snankc1cWnanVc108nHf4njf3c108rHDLrH0s0Z7xIWYsQWb3g108njKxna3sn7tsQW6Yg108PWFxni3sn7tsQW03g1Dzr0KBTdqsThqbpyfqn0KzUv-hUA7M5HD0mLmq0A-1gvPsmHYs0APs5H00ugPY5H00mLFW5HD4nWDk%26us%3Dnewvui%26word%3D%26ck%3D5273.14.94.413.176.306.208.76%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26wd%3D%26bc%3D110101&l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-pc-BOSS-JD02-B19KA02084%26plan%3D%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D-cp%26unit%3D%25E5%2593%2581%25E7%2589%258C-%25E9%2580%259A%25E7%2594%25A8%26keyword%3Dboss%26bd_vid%3D8233269182427230599%26csource%3Dboctb&s=3&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-pc-BOSS-JD02-B19KA02084%26plan%3D%25E5%2593%2581%25E7%2589%258C%25E8%25AF%258D-cp%26unit%3D%25E5%2593%2581%25E7%2589%258C-%25E9%2580%259A%25E7%2594%25A8%26keyword%3Dboss%26bd_vid%3D8233269182427230599%26csource%3Dboctb&friend_source=0&s=3&friend_source=0; __zp_stoken__=67becGm8WIylXO2gWaW8BAD48bGNbc00IAnM2fGdZACEIbzFSbwFLfSV3IwFLaz4FWi5KeyUDNyZEe2MtBDAjKQdafQ4QGRQzNi0VRywBRSM3dQQwaCgXGS8eNyIcV3p4ag1aRkQMQw08bXkN; acw_tc=0bdd342a16274545209521280e01ca760a7979114e031e14fd27218103d72c; __c=1627441702; __a=59205928.1623892406.1623892406.1627441702.11.2.8.8; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1627454520',
#
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bossPro.middlewares.BossproSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'bossPro.middlewares.BossproDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'bossPro.pipelines.BossproPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
