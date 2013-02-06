import sublime
import sublime_plugin
import urllib2
from urllib import urlencode


class SendToPastepmCommand(sublime_plugin.TextCommand):

    def run(self, view):

        for region in self.view.sel():

            text = self.view.substr(region).encode('utf-8')
            payload = {'content': text}

            if not text:
                sublime.status_message("Error sending to paste.pm: Nothing selected")
            else:
                response = "http://paste.pm"
                try:
                    response += urllib2.urlopen("http://paste.pm/post", data=urlencode(payload)).read()
                    sublime.set_clipboard(response)
                    sublime.status_message("Paste.pm url copied to clipboard: " + response)
                except urllib2.URLError:
                    sublime.status_message("Error: Cannot reach http://paste.pm")
