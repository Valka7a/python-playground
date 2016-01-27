import feedparser

python_wiki_rss_url = "http://www.python.org/cgi-bin/moinmoin/" \
                        "RecentChanges?action=rss_rc"
feeds = feedparser.parse( python_wiki_rss_url )

print(feeds)

entires = []
for feed in feeds:
    entires.append(feed)

print(entires)


# 1. izvadi vsichki novini ot toq feed i gi printi nice v console
# 2. zadacha e da generirash json file s pyrvite pyrvata stranica
#
# rss feed-a e nai-chesto edin link na koito prez nqkvo vreme se update-va sydyrjanieto
# i e v xml format ti trqbva da go parsirash i da go obrabotish
#
# 3ta zadacha s povishena trudnost python script-a
# na vseki 10 min da proverqva dali ima neshto novo i ako
# ima da ti prashta mail
# i da ti kazva glei kvo stava tuka
# izpusnal si tva
#
# http://feeds.reuters.com/reuters/technologyNews