# keyword-mining

`suggest.py` reads Google and YouTube autocomplete for a seed. No key and no bill. The endpoint is the public suggest service.

Search terms are a stand-in for what people type when they have a problem. The script groups them into pain, comparison, purchase intent, and question.

```bash
python3 ferramentas/keyword-mining/suggest.py "<seed>" ["<seed2>" ...] \
  [--lang en] [--no-alpha] [--sleep 0.3] [--out terms.md]
```

- `--no-alpha` skips the a-z sweep. Use it by default.
- `--lang` defaults to `en` in this template. Pass the creator's content language too when it differs.
- `--sleep` pauses between requests (default 0.4s).
- Without `--out`, markdown goes to stdout.

For each seed it queries the seed, question modifiers, comparison modifiers, pain modifiers, and intent modifiers, on Google and on YouTube. Output sections: pains, questions, comparisons, intent, related.
