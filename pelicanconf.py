#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ray Alez'
SITENAME = 'Rational Fiction'
SITEURL = ''                    # http://rationalfiction.io'

PATH = 'content'
STATIC_PATHS = [
    'images',
    ]


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml' #None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Menu
MENUITEMS = [('Forum', '/'), ('Articles', '/articles')]

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# articles on subpage?
# nope  INDEX_SAVE_AS = 'articles.html'

ARTICLE_URL = 'post/{slug}'
ARTICLE_SAVE_AS = 'post/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_SAVE_AS = 'article-categories.html'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', ) #'about'

TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

THEME = "/home/ray/projects/rationalfiction/blog/themes/rationalfiction"

# Plugins
PLUGIN_PATHS = ['/home/ray/projects/rationalfiction/blog/pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook']

EXTRA_HEADER = open('_nb_header.html').read() #.encode('utf-8')
