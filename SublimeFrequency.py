"""
Sublime Text 3 plugin that shows the frequency of each line in a document
"""


import json
import pprint
import collections

import sublime
import sublime_plugin


class LineFrequencyCommand(sublime_plugin.TextCommand):
    def get_content(self):
        """
        Return the content of current selection(s), or the content of the current document
        """
        content = "".join([self.view.substr(region) for region in self.view.sel()])
        if content == "":
            content = self.view.substr(sublime.Region(a=0,b=self.view.size()))
        return content

    def run(self, edit):
        ### Get selected/full text from current file, and split into lines
        lines = self.get_content().splitlines()
        
        ### Do frequency counting of lines
        freq = {}
        for line in lines:
            freq.update({line:freq.get(line,0)+1})

        ### Sort by value, and by key for items having same value
        freq = collections.OrderedDict(
            sorted(
                sorted(freq.items(), key=lambda i:i[0]),
                key=lambda i:i[1], reverse=True
            )
        )
        
        ### Convert to JSON
        content = json.dumps(freq, indent=4)

        ### Open a new window and print content
        scratch = self.view.window().new_file()
        scratch.set_scratch(True)
        scratch.set_syntax_file('Packages/JavaScript/JSON.sublime-syntax')
        scratch.run_command('insert_content', {'content': content})


class InsertContentCommand(sublime_plugin.TextCommand):
    def run(self, edit, content):
        self.view.insert(edit, 0, content)
