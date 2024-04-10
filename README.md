# SMearch
This Social Media Search Engine, or SMearch, key word searches through the discovered items provided by snscrape and allows a filtering for specific types, ex: posts or profile names. The UI will then provide it's results in a search engine results format.
Project Roadmap:

- [x] Find related repository and evaluate it
- [ ] Test repository
- [ ] Document how it works
- [ ] Optimize the key word search to be more beneficial to the user
- [ ] Create a UI for it
- [ ] Test it



# snscrape Notes:
* Instagram: user profiles, hashtags, and locations
* Mastodon: user profiles and toots (single or thread)
* Reddit: users, subreddits, and searches (via Pushshift)
* Telegram: channels
* Twitter: users, user profiles, hashtags, searches (live tweets, top tweets, and users), tweets (single or surrounding thread), list posts, communities, and trends
* VKontakte: user profiles
* Weibo (Sina Weibo): user profiles

Requirements
* snscrape requires Python 3.8 or higher. The Python package dependencies are installed automatically when you install snscrape.
* Note that one of the dependencies, lxml, also requires libxml2 and libxslt to be installed.
