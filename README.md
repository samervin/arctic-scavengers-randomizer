# arctic-scavengers-randomizer

A resource similar to [these sort of Dominion websites(http://www.hiwiller.com/dominion/), but for the board game Arctic Scavengers.

Written in Python using PyCharm and virtualenv and MongoDB.

A note on `mongod.conf`: you may find it convenient, as I did, to run `git update-index --assume-unchanged mongod.conf` so that Git will never find changes in the file (since you'll have to update the `dbPath` to something sane). To double-check this and view all files Git knows about, you can always use `git ls-files -v`. [[Source.](http://stackoverflow.com/questions/3319479/git-can-i-commit-a-file-and-ignore-the-content-changes)]
