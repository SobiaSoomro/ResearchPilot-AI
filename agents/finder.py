from tools.arxiv_tool import search_papers


def paper_finder(topic):

    papers = search_papers(topic)

    if not papers:
        return []

    topic_words = set(topic.lower().split())

    relevant = []

    for paper in papers:

        text = (
            paper["title"] + " " + paper["summary"]
        ).lower()

        score = sum(
            1 for word in topic_words
            if word in text
        )

        relevance = round(
            (score / len(topic_words)) * 100
        )

        if relevance >= 50:

            paper["relevance"] = relevance

            relevant.append(paper)

    # Highest relevance first
    relevant.sort(
        key=lambda x: x["relevance"],
        reverse=True
    )

    return relevant[:10]