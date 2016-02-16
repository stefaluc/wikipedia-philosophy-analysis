# wikipedia-philosophy-analysis
GettingToPhilosophy.py is a basic web crawler that crawls Wikipedia in accordance to following [phenomenom](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy):
>Clicking on the first lowercase link in the main text of a Wikipedia article, and then repeating the process for subsequent articles, usually eventually gets one to the Philosophy article. As of May 26, 2011, 94.52% of all articles in Wikipedia lead eventually to the article Philosophy. The remaining 100,000 (approx.) links to an article with no wikilinks or with links to pages that do not exist, or get stuck in loops (all three are equally probable).[1] The median link chain length to reach philosophy is 23. It takes 15 clicks to get to Philosophy from this page.

The script begins at a [random article](https://en.wikipedia.org/wiki/Special:Random) and navigates to the first link on every subsequent until the page [Philosophy](https://en.wikipedia.org/wiki/Philosophy) is reached.

![Test Run](https://raw.githubusercontent.com/stefaluc/wikipedia-philosophy-analysis/master/example.gif)

Minor bug fixes in webcrawling are still required for this script (not every trial run is successful), as well as further data analysis.
