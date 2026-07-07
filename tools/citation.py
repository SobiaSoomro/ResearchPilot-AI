def get_first_author(authors):

    if not authors:
        return "Unknown"

    return authors.split(",")[0].strip()


def get_year(date):

    if not date:
        return "Unknown"

    return date[:4]


# ======================================
# APA
# ======================================

def generate_apa(paper):

    author = get_first_author(paper.get("authors", ""))
    year = get_year(paper.get("published", ""))

    return (
        f"{author}. ({year}). "
        f"{paper['title']}. "
        "arXiv."
    )


# ======================================
# IEEE
# ======================================

def generate_ieee(paper):

    author = get_first_author(paper.get("authors", ""))
    year = get_year(paper.get("published", ""))

    return (
        f"{author}, "
        f"\"{paper['title']},\" "
        f"arXiv, {year}."
    )


# ======================================
# MLA
# ======================================

def generate_mla(paper):

    author = get_first_author(paper.get("authors", ""))
    year = get_year(paper.get("published", ""))

    return (
        f"{author}. "
        f"\"{paper['title']}.\" "
        f"arXiv, {year}."
    )


# ======================================
# BibTeX
# ======================================

def generate_bibtex(paper):

    author = get_first_author(paper.get("authors", ""))
    year = get_year(paper.get("published", ""))

    key = author.lower().replace(" ", "") + year

    return f"""@article{{{key},
  title={{{paper['title']}}},
  author={{{paper['authors']}}},
  year={{{year}}},
  journal={{arXiv}}
}}"""