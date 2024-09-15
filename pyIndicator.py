#-- https://askubuntu.com/questions/770036/appindicator3-set-indicator-icon-from-file-name-or-gdkpixbuf
#!/usr/bin/env python3
import os
import signal
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, AppIndicator3

currpath = os.path.dirname(os.path.realpath(__file__))

class Indicator():
    def __init__(self):
        self.app = 'show_proc'
        iconpath = currpath+"/nocolor.png"
        # after you defined the initial indicator, you can alter the icon!
        self.testindicator = AppIndicator3.Indicator.new(self.app, iconpath, AppIndicator3.IndicatorCategory.OTHER)
        self.testindicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.testindicator.set_menu(self.create_menu())

    def create_menu(self):
        menu = Gtk.Menu()
        item_quit = Gtk.MenuItem(label='Quit')
        item_quit.connect('activate', self.stop)
        item_green = Gtk.MenuItem(label='Green')
        item_green.connect('activate', self.green)
        item_purple = Gtk.MenuItem(label='Purple')
        item_purple.connect('activate', self.purple)
        menu.append(item_quit)
        menu.append(item_green)
        menu.append(item_purple)
        menu.show_all()
        return menu

    def stop(self, source):
        Gtk.main_quit()

    def green(self, source):
        self.testindicator.set_icon(currpath+"/green.png")

    def purple(self, source):
        self.testindicator.set_icon(currpath+"/purple.png")

Indicator()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
