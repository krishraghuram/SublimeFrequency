import sublime
import sublime_plugin

# s = {}

# def plugin_loaded():
#     global s
#     s = sublime.load_settings('SublimeHist.sublime-settings')

class HistLinesCommand(sublime_plugin.TextCommand):
    """
    Logic:
    Get full text from current file
    Do frequency counting of lines
    Open a new window, and print frequency counts as csv/tsv
    """
    def run(self, edit):
        # print(vars(self.view.selection))
        # print(str(self.view.selection))
        
        # print(self.view.substr(0))
        # print(self.view.line(0))
        # print(self.view.substr(self.view.line(0)))
        
        print(self.view.substr(sublime.Region(a=0,b=self.view.size())))
        self.view.insert(edit, self.view.size(), "\n\t\tHello World")