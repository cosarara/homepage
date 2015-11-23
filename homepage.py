#!/usr/bin/env python3
""" generate firefox homepage from bookmarks """

#import mako
#from mako.template import Template
from base64 import b64encode
from mako.lookup import TemplateLookup
import sqlite3
import glob
import os.path

DB = glob.glob(os.path.expanduser('~/.mozilla/firefox/') +
               '*.default/places.sqlite')[0]

def get_stuff():
    uri = "file:{}?mode=ro".format(DB)
    conn = sqlite3.connect(uri, uri=True)

    cur = conn.cursor()

    # I don't know if that's the proper way to do SQL
    cur.execute("select moz_bookmarks.title, moz_places.title, moz_places.url, mime_type, data "
                "from moz_places "
                "join moz_bookmarks on moz_bookmarks.fk=moz_places.id "
                "join moz_favicons on moz_favicons.id=moz_places.favicon_id "
                "where moz_bookmarks.parent=3 and moz_bookmarks.type=1")

    bookmarks = cur.fetchall()
    bookmarks = [(name or name2, url, mime, b64encode(data).decode('utf8'))
                 for name, name2, url, mime, data in bookmarks]
    return bookmarks

def render(bookmarks):
    lookup = TemplateLookup(directories=['.'], strict_undefined=True)
    return lookup.get_template("template.mako").render(bmarks=bookmarks)

if __name__ == "__main__":
    print(render(get_stuff()))

