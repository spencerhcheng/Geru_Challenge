## INFO

This directory contains standalone functions for Challenge #1, namely `get_quote(<quote_number>)` and `get_quotes()`.

## USAGE

This project was written in `ZSH` on `Ubuntu 14.04 LTS` using `python3` (`version 3.4.3`).

### Command Line

```
./get_quotes.py

Here are all quotes available:
{0: 'Beautiful is better than ugly.', 1: 'Explicit is better than implicit.', 2: 'Simple is better than complex.', 3: 'Complex is better than complicated.', 4: 'Flat is better than nested.', 5: 'Sparse is better than dense.', 6: 'Readability counts.', 7: "Special cases aren't special enough to break the rules.", 8: 'Although practicality beats purity.', 9: 'Errors should never pass silently.', 10: 'Unless explicitly silenced.', 11: 'In the face of ambiguity, refuse the temptation to guess.', 12: 'There should be one-- and preferably only one --obvious way to do it.', 13: "Although that way may not be obvious at first unless you're Dutch.", 14: 'Now is better than never.', 15: 'Although never is often better than *right* now.', 16: "If the implementation is hard to explain, it's a bad idea.", 17: 'If the implementation is easy to explain, it may be a good idea.', 18: "Namespaces are one honking great idea -- let's do more of those!"}
```
```
./get_quote.py 5
Quote #5:
Sparse is better than dense.
```

### REPL
```
>>> import get_quote
>>> get_quote.get_quote(3)
'Complex is better than complicated.'

>>> import get_quotes
>>> get_quotes.get_quotes()
{0: 'Beautiful is better than ugly.', 1: 'Explicit is better than implicit.', 2: 'Simple is better than complex.', 3: 'Complex is better than complicated.', 4: 'Flat is better than nested.', 5: 'Sparse is better than dense.', 6: 'Readability counts.', 7: "Special cases aren't special enough to break the rules.", 8: 'Although practicality beats purity.', 9: 'Errors should never pass silently.', 10: 'Unless explicitly silenced.', 11: 'In the face of ambiguity, refuse the temptation to guess.', 12: 'There should be one-- and preferably only one --obvious way to do it.', 13: "Although that way may not be obvious at first unless you're Dutch.", 14: 'Now is better than never.', 15: 'Although never is often better than *right* now.', 16: "If the implementation is hard to explain, it's a bad idea.", 17: 'If the implementation is easy to explain, it may be a good idea.', 18: "Namespaces are one honking great idea -- let's do more of those!"}
```
