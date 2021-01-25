"""
Sublime command to print frequency of lines (and words)

TODO:
* Add commands for separators like "," and " " and "\t"
* Allow arbitrary separators
* Sort JSON output by key (to make it easier for user to quickly lookup a word/line)
* Sort JSON output by value (to easily see which words/lines are occuring most)
"""

import json
import pprint
import collections

import sublime
import sublime_plugin

class LineFrequencyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ### Get full text from current file
        lines = self.view.substr(sublime.Region(a=0,b=self.view.size())).splitlines()
        
        ### Do frequency counting of lines
        freq = {unique_line:0 for unique_line in set(lines)}
        for line in lines:
            freq[line] += 1
        ### Sort by value
        # freq = collections.OrderedDict(sorted(freq.items(), key=lambda i:i[1], reverse=True))
        ### Sort by key
        # freq = collections.OrderedDict(sorted(freq.items(), key=lambda i:i[0]))
        content = json.dumps(freq, indent=4)
        ### Sort by key inside json.dumps
        # content = json.dumps(freq, indent=4, sort_keys=True)

        ### Open a new window, and print frequency counts as csv/tsv
        scratch = self.view.window().new_file()
        scratch.set_scratch(True)
        scratch.set_syntax_file('Packages/JavaScript/JSON.sublime-syntax')
        scratch.run_command('insert_content', {'content': content})

class InsertContentCommand(sublime_plugin.TextCommand):
    def run(self, edit, content):
        self.view.insert(edit, 0, content)
