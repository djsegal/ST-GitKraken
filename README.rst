SublimeTextGitKraken
===============

Very simple plugin to open GitKraken (http://gitkraken.com/) from Sublime Text 2 and 3 (http://www.sublimetext.com/).

Installing
----------

**Using Git:** Clone the repository in your Sublime Text Packages directory and restart Sublime Text:

    git clone https://github.com/djsegal/SublimeTextGitKraken

**Using the Package Control plugin:** The easiest way to install SublimeTextGitKraken is through Package Control,
which can be found at http://wbond.net/sublime_packages/package_control .

Once you install Package Control, restart Sublime Text 2 and open the Command Palette.

Select "Package Control: Install Package", wait while Package Control fetches the latest package list,
then select SublimeTextGitKraken when the list appears.

The advantage of using this method is that Package Control will automatically keep this plugin up to date.

Usage
-----

Open GitKraken and enable terminal usage by clicking on the GitKraken menu and then on ``Enable Terminal Usage...``;
GitKraken will create an executable named ``gitkraken`` inside ``/usr/local/bin``.

Open the command palette and execute the ``GitKraken: Open GitKraken`` command to open the GIT repository
in which the currently opened file is located.

Sample user key binding to execute the command::

    { "keys": ["super+."], "command": "gitkraken_open" }

Configuration
-------------

Additional settings can be configured in the User File Settings:

``gitkraken_path``: the path to the ``gitkraken`` executable (default: ``"/usr/local/bin/gitkraken"``)

Changelog
---------
v0.1 (01-04-2011):

* Initial version

v0.2.0 (01-16-2014):

* Updated README about ST3 compatibility

License
-------
See the LICENSE.txt file.
