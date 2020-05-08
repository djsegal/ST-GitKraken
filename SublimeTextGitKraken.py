import locale
import os
import subprocess
import sublime, sublime_plugin

class GitKrakenCommand():
    def get_path(self):
        if self.window.active_view():
            return self.window.active_view().file_name()
        elif self.window.folders():
            return self.window.folders()[0]
        else:
            sublime.status_message(__name__ + ': No place to open GitKraken to')
            return False

class GitkrakenOpenCommand(sublime_plugin.WindowCommand, GitKrakenCommand):
    def is_enabled(self):
        return True

    def run(self, *args):
        path = self.get_path()
        if not path:
            return
        if os.path.isfile(path):
            path = os.path.dirname(path)

        settings = sublime.load_settings('Base File.sublime-settings')
        gitkraken_path = settings.get('gitkraken_path', '/usr/local/bin/gitkraken')

        if not os.path.isfile(gitkraken_path):
            mac_path = '/Applications/GitKraken.app'
            if os.path.isdir(mac_path):
                gitkraken_path = mac_path
            else:
                gitkraken_path = None

        if gitkraken_path in ['', None]:
            sublime.error_message(__name__ + ': gitkraken executable path not set, incorrect or no gitkraken?')
            return False

        if gitkraken_path.endswith(".app"):
            subprocess.call(['open', '-a', gitkraken_path, path])
        else:
            try:
                encoding = locale.getpreferredencoding(do_setlocale=True) or 'UTF-8'
                p = subprocess.Popen([gitkraken_path], cwd=path.encode(encoding), shell=True)
            except Exception as e:
                sublime.error_message(__name__ + ' Error launching gitkraken ' + e.message)
