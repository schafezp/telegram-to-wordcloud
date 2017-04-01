# telegram-to-wordcloud

This utility provides a convenient way to turn telegram conversations into wordclouds.

This project uses [telegram-cli](https://github.com/vysheng/tg) [telegram-history-dump](https://github.com/tvdstaaij/telegram-history-dump) and [word_cloud](https://github.com/amueller/word_cloud)

First use telegram-history-dump to create jsonl backups of your telegram conversation. Then pass on of the fil
es as the argument to generate.py.
```bash
python3 generate.py path-to-file

```
