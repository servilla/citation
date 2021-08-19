#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod: harness

:Synopsis:

:Author:
    servilla

:Created:
    7/22/21
"""
from scholarly import scholarly
from scholarly._navigator import MaxTriesExceededException

import time


def main():

    citations = list()

    for year in range(2013, 2022):
        try:
            search_query = scholarly.search_pubs(query="10.6073/pasta", year_low=year, year_high=year)
            total_results = search_query.total_results
            print(f"{year}, {total_results}")
            for citation in search_query:
                time.sleep(1.0)
                citations.append(
                    (
                        citation["bib"]["title" if "title" in citation["bib"] else None],
                        ", ".join(citation["bib"]["author"]) if "author" in citation["bib"] else None,
                        citation["bib"]["pub_year"] if "pub_year" in citation["bib"] else None,
                        citation["bib"]["venue"] if "venue" in citation["bib"] else None,
                        citation["bib"]["journal"] if "journal" in citation["bib"] else None,
                        citation["bib"]["volume"] if "volume" in citation["bib"] else None,
                        citation["bib"]["number"] if "number" in citation["bib"] else None,
                        citation["bib"]["pages"] if "pages" in citation["bib"] else None,
                        citation["bib"]["publisher"] if "publisher" in citation["bib"] else None,
                        citation["pub_url"] if "pub_url" in citation else None,
                        citation["eprint_url"] if "eprint_url" in citation else None
                    )
                )
        except MaxTriesExceededException as e:
            print(e)
            break
    with open("citations.csv", "w") as f:
        header = "title,author(s),pub_year,venue,journal,volume,number,pages,publisher,pub_url,eprint_url\n"
        f.write(header)
        for _ in citations:
            line = f'"{_[0]}","{_[1]}","{_[2]}","{_[3]}","{_[4]}","{_[5]}","{_[6]}","{_[7]}","{_[8]}","{_[9]}","{_[10]}"\n'
            f.write(line)
    return 0


if __name__ == "__main__":
    main()
