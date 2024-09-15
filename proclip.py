import os, sys, csv, time
#import pyperclip as clip
import tkinter, tkinter.filedialog
#import signal

import gi
gi.require_version('Gdk', '4.0')
gi.require_version('Gtk', '4.0')
from gi.repository import Gdk, Gtk, GLib
from gi.repository import AppIndicator3
from time import sleep

def paste_text():
    clipboard = Gdk.Display.get_default().get_clipboard()
    clipboard.read_text_async(None, on_paste_text)
    sleep(1)

    clipboard.set('RR54fdanbhsuy_A[ponz2mdkmajmjsdmksdnkndskhnnsakjk2213328932178378$---£hsdushsusnkjsishsauyswnhq99383478473hfos9£hsdushsusnkjsishsauyswnhq99383478473hfos9£hsdushsusnkjsishsauyswnhq99383478473hfos9£hsdushsusnkjsishsauyswnhq99383478473hfos9òòòshasuasjusa')
    sleep(1)
    
def on_paste_text(clipboard, result):
    text = clipboard.read_text_finish(result)
    if text is not None:
        print(text)

    main_loop.quit()


main_loop = GLib.MainLoop.new(None, True)
paste_text()
main_loop.run()