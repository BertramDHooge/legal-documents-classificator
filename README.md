<h2 align="center">Legal document classification usecase</h2>
<p align="center"><a href="https://becode.org/">
<img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200"></a></p>
<h3 align="center"> Legal document classification usecase at <a href="https://github.com/becodeorg"><strong>BeCode</strong></a></h3>
<h3 align="center"> Forked from <a href="https://github.com/IrinaSing/legal-documents-classificatior"><strong>legal-documents-classificatior</strong></a></h3>
<h3 align="center"> Contributors: <a href="https://github.com/saifalbaghdadi"> Saif Malkshahi</a>, <a href="https://github.com/IrinaSing"> Irina Singh</a>, <a href="https://https://github.com/BertramDHooge"> Bertram D'Hooge</a> </h3><br>

  
## The timeline of the project: 
**1/06/2022 - 15/06/2022*

## Project flow

This was a group project where we tackled a usecase provided by KPMG. For this usecase we were challenged to automatically classify legal documents from the Belgian Gazette. As we had not worked with NLP in depth yet a lot of time was spent exploring different algoritms and approaches for this project. We spent some time trying out LDA but ended up using BERTopic to extract topics. We also used BERT to summarize and the googletrans api to translate the articles. 

The final result allows to insert an article into a streamlit app and this app will then attempt to extract the key topics, summarize and will return some articles with similar topic disribution. Alternatively you can search a keyword and the app will attempt to match this keyword to the extracted topics and return some articles according to this keyword.

## Next steps

Due to the time pressure the final result was very rushed and had many unnecessary files and unorderly code. The final result worked argely as desired, but needs to be intensively cleaned up before it can be used properly.

## Objectives of the project: 
* Building an application to classify legal documents

## Usage:
* The project can currently not be cleanly run as desired.

## Project outline:

* [x] Scraping the articles from the Belgian Gazette using the given dataset
* [x] Cleaning up the scraped articles
* [x] Translating the cleaned articles and potentially summarizing them as well
* [x] Using an unsupervised algoritm to extract the topics
* [x] Using the extracted topics, finding a way to classify or otherwise go through the articles


## Dataset details:
[Dataset](https://github.com/BertramDHooge/legal-documents-classificator/blob/main/data/KPMG%20Tax%20Case%20-%20Data%20Set.csv) contains the following columns :

 - [x] considered relevant for this project
 - [ ] not considered relevant for this project
 
* [x] Date; 
* [x] Numac;
* [ ] Link FR;
* [ ] Link NL;

Originally we tried to scrape using the links provided, but these led to pages that were quite difficult to scrape due to how the data was loaded, so in the end it turned out to be easier to use the date and numac with string.format() in a default link.
