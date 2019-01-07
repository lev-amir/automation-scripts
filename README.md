# automation-scripts
Scripts I developed during my work at the Ehud Cohen lab, which automated some
of the processes that surround wet-lab research, literature review, and
analysis.

# Contents
## convert-lifespan-to-GraphPad
When monitoring the lifespans of *C. elegans*, the usual format is to log for
each timepoint the number of censored, dead, and alive animals.
Yet the statistical plotting software GraphPad Prism, which is used to test and
plot the survival of the animals, takes in as input one animal per row, with an
indication of whether it is dead (1) or censored (0) (detailed instructions in
the software documentation).  
To convert between the manual input format and the required GraphPad Prism
format, one can input (or copy from any spreadsheet software) the measurements
of the animals survival into the file `lifespanTemplatePasteDataHere.csv`
according to the example data already present in the file. The four columns are:

| Day	#          | Missing	#     | dead           | treatment      |
| :------------- | :------------- | :------------- | :------------- |
| 5              | 2              | 3              | EV             |

After saving the csv file, can run the script `lifespanFormatToGraphPad.py` in
the terminal:
```
python lifespanFormatToGraphPad.py
```
or
```
py lifespanFormatToGraphPad.py
```
The converted data will be saved in the file `lifespanReformattedOutput.csv`,
which can be transferred to GraphPad Prism.

## convert-paralysis-to-GraphPad
Mostly the same as the lifespan case above, but with an adjustment to the
order of the variables. In the output file 1 is paralyzed.

## cross-ref-lists
A multi-phrase search function. I found myself in need of crossing between two
sources of gene lists. Usually I had a clean list of genes and I needed to find
which of these genes are present in a table or a web-page, etc. This script
takes in a clean list of phrases (e.g. genes) `MyGenes.txt` and a messy
copy-pasted text from whatever source the list needs to be crossed with
`ScreenList.txt`, and returns the phrases that exist in both of the text files.
To get the results run in the terminal:
```
python CompareGenes.py
```
or
```
py CompareGenes.py
```
## pubmed-journal-search-terms
Helper function that converts a list of journal to the search-term format that
PubMed takes it. This was done in order to search for search terms only in a
range of specific journals.

**Example**
Input:
```
Aging Cell
Ageing Research Reviews
Journals of Gerontology - Series A Biological Sciences and Medical Sciences
Neurobiology of Aging
```
Output:
```
"Aging Cell"[ta] OR "Ageing Research Reviews"[ta] OR "J Gerontol A Biol Sci Med Sci"[ta] OR "Neurobiology of Aging"[ta]
```
