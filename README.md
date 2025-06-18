### Host an Obsidian vault as a static website

This project converts an Obsidian-style folder tree into a static site that can
be served from any web host.

Run the site generator by pointing it at the root of your vault:

```bash
python x.py /path/to/your/vault
```

Each directory must contain a `README.md` to be included. Markdown files are
converted to HTML using a minimal parser and written next to the originals.
An `index.html` is created from the README with links to pages and valid
sub‑directories.

