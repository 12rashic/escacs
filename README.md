# Escacs

Library for chess fun

## Install

Clone the repo and install the package

``` shell
git clone git@github.com:lferran/escacs.git
make develop
```

Then you can run the CLI GUI with

``` shell
venv/bin/python gui/cli.py
```

and play!

``` shell
  a b c d e f g h   black: 0
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 8
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 7
6                 6
5                 5
4     ♙           4
3                 3
2 ♙ ♙   ♙ ♙ ♙ ♙ ♙ 2
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 1
  a b c d e f g h   white: 0
[black] >>> a1a3
Invalid move! Try again...

```

## Development

``` shell
# Clone the repository
git clone git@github.com:lferran/escacs.git
cd escacs

# Configure python version
pyenv local 3.8.2

# Install
make develop

# Run tests
make tests
```
