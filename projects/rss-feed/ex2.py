import feedparser
   2
   3 python_wiki_rss_url = "http://www.python.org/cgi-bin/moinmoin/" \
   4                       "RecentChanges?action=rss_rc"
   5
   6 feed = feedparser.parse( python_wiki_rss_url )