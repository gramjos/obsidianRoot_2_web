import os, sys
from pathlib import Path
from md_2_html.Main import markdown_to_html

def is_valid_dir(path:Path) -> bool:
    for item in path.iterdir():
        b=item.name.lower().startswith('readme')
        bb=item.name.lower().endswith('.md')
        if item.is_file() and b and bb: return True
    return False

def generate_site(root_dir: Path):
    """
    Generate a static website from markdown files in an Obsidian-style folder structure.
    root_dir: Path to the root directory containing markdown files.
    """
    if not isinstance(root_dir, Path): sys.exit(0)
   # am I a valid directory ? is there a README
    if is_valid_dir(root_dir):
        # create homepage based on README with either links(s) to pages and/or other valid directories 
        rm = root_dir / 'README.md'
        print(type(rm))
        c = rm.read_text(encoding='utf8') # get README(homepage) content and prepare to embed it

        # prepare a list of final destinations (terminal) sites
        r = list(root_dir.glob('*.md'))
        terminal_sites = []
        for md_site in r:
            n = md_site.name
            if n != "README.md":
                terminal_sites.append(n)

        # prepare a list of links to valid directories
        dirs_ = []
        for p in root_dir.iterdir():
            if p.is_dir() and is_valid_dir(p):
                dirs_.append(p.name)

        
        # drop variable `c` into SECTION 1
        # drop variable `r` into SECTION 2 as hypllinks
        # drop variable `dirs_` into SECTION 3 as hyperlinks
        rm_text = rm.read_text(encoding="utf8")
        x = markdown_to_html(rm_text, md_home_pg=rm, 
                              terminal_sites=terminal_sites, 
                              valid_dirs=dirs_, 
                              root_dir=root_dir)
        # print(x)
    else: # prune
        print(f"Invalid directory: {root_dir}. No README.md found or no markdown files.")
        return
    

if __name__ == "__main__":
    p=Path('/Users/gramjos/Documents/try_hosting_Vault')
    generate_site(p)
    print(f"Static site generated at {p=}")

