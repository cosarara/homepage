#!/usr/bin/env python3
""" generate firefox homepage from bookmarks """

#import mako
#from mako.template import Template
from base64 import b64encode
from mako.lookup import TemplateLookup
import sqlite3
import glob
import os.path
import re
from collections import namedtuple

DB = glob.glob(os.path.expanduser('~/.mozilla/firefox/') +
               '*.default/places.sqlite')[0]

Bookmark = namedtuple('Bookmark', ['name', 'url', 'mime', 'data'])

def dname(url):
    m = re.search(r"://(?:www\.)?(.*?)\.(?:.*?)/", url)
    #m = re.search(r"://(.*?)/", url)
    if m is None:
        return url
    return m.group(1)

def get_bookmarks(cur, parent):
    cur.execute("select moz_bookmarks.title, moz_places.title, moz_places.url, mime_type, data "
                "from moz_places "
                "join moz_bookmarks on moz_bookmarks.fk=moz_places.id "
                "left join moz_favicons on moz_favicons.id=moz_places.favicon_id "
                "where moz_bookmarks.parent=:parent and moz_bookmarks.type=1",
                {"parent": parent})
    bookmarks = cur.fetchall()
    bookmarks = [Bookmark(name or name2 or dname(url), url, mime,
                          b64encode(data).decode('utf8') if data else "")
                 for name, name2, url, mime, data in bookmarks]
    return bookmarks

def get_dirs(cur):
    cur.execute("select id, title "
                "from moz_bookmarks "
                "where parent=3 and type=2")
    dirs = cur.fetchall()
    return dirs

def get_conn():
    uri = "file:{}?mode=ro".format(DB)
    conn = sqlite3.connect(uri, uri=True)
    return conn

def get_stuff():
    conn = get_conn()
    cur = conn.cursor()

    # I don't know if that's the proper way to do SQL
    bookmarks = get_bookmarks(cur, 3)
    dirs = [(title, get_bookmarks(cur, str(dir_id))) for dir_id, title in get_dirs(cur)]
    return [('Home', bookmarks)] + dirs

def render(bookmarks):
    lookup = TemplateLookup(directories=['.'], strict_undefined=True)
    return lookup.get_template("template.mako").render(bmarks=bookmarks)

if __name__ == "__main__":
    print(render(get_stuff()))

