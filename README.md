# International-Phonetics
Using Wikipedia IPA Data for various languages to find the most common phonemes.

## Process
Wikipedia has various pages labelled as IPA:Help for various languages. These IPA Pages contain the phonemes in each particular language.

Using Python to scrape the data of specifically the phonetic consonants, it was cleaned and formatted into a CSV file.

The data in the CSV file was then read and used to create plots using R's ggplot package.

### Results

Pie Chart
![Top Phonemes Wikipedia Data Rplot](https://github.com/anthonyjk/International-Phonetics/assets/41717689/be1f5e1d-5723-434d-a3f9-efde18bbea64)

Bar Graph
![commonest phonemes rPlot](https://github.com/anthonyjk/International-Phonetics/assets/41717689/2cfee6d5-6b93-4f88-a28d-1fde974516cf)

### Notes
Data is only about Phonetic Consonants, does not include Vowels.

Data may not be 100% accurate (Scraping issues?)

This project was just for fun and should not be seen as a valid source!
