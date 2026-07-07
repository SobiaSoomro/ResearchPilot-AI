import arxiv


def search_papers(query, max_results=5):

    client = arxiv.Client()

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []

    for result in client.results(search):

        papers.append({
            "title": result.title,
            "authors": ", ".join(author.name for author in result.authors),
            "summary": result.summary,
            "published": result.published.strftime("%Y-%m-%d"),
            "pdf_url": result.pdf_url
        })

    return papers