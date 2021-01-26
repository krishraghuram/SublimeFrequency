# Notes.md

```
# Commands to install package locally, for development
rsync -azP ../SublimeFrequency /home/raghuram/.config/sublime-text-3/Packages
while true; do date && rsync -azP ../SublimeFrequency /home/raghuram/.config/sublime-text-3/Packages && sleep 2; done

# Tagging Releases
git add -A
git commit --amend
git tag -d st3-0.1.0
git tag -a st3-0.1.0 -m "Initial Release"
git push -f origin master
git push origin :refs/tags/st3-0.1.0
git push origin --tags
```
