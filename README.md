# connected-components-of-collabaration-graph-of-DBLP-dataset
This repo is developed to find the connected components in the collabaration graph of DBLP dataset. More specifically, I consider all publications from 1936 to 2014.
## Dataset acquisition
Since the dataset is too large, I refer you to the url https://dblp.org/xml/release/ for the "dblp.xml" file used in my code. The file I used is *dblp-2015-03-02.xml.gz*.
## About code
First all authors are gathered in an index file call "authors.txt". Then the collabaration relationships are generated as links of the collaboration graph in "collaboration.txt". Finally, all connected components are found.