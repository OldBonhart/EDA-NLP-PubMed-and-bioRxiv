# EDA-NLP-PubMed-and-bioRxiv

## Rapid analysis of scientific papers from bioRxiv and PubMed
This repository contains the source code for asynchronously scraping science papers from the [**bioRxiv**](https://www.biorxiv.org/) and [**PubMed**](https://www.ncbi.nlm.nih.gov/pubmed), for subsequent conversion of this data into word embeddings Word2Vec for semantic and syntactic similarity words from this data, relations with other words, etc., followed by visualization of hight-dimensional Word2Vec word embeddings using t-SNE.

Expected Input - links to an articles of the format:

Pubmed
+ "https://www.ncbi.nlm.nih.gov/pubmed/?term=connectome"

bioRxiv
+ https://www.biorxiv.org/search/connectome%20numresults%3A75%20sort%3Arelevance-rank?page="

Expected Output - images with visualization and scraped data recorded in [**PDF format**](https://www.ncbi.nlm.nih.gov/pubmed/?term=connectome).
## Quick start
[demo.ipynb](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/demo.ipynb)[<img src="https://colab.research.google.com/assets/colab-badge.svg" align="center">](https://colab.research.google.com/drive/1DcpwqJVSZ8xVWM3RaVYmW_ramRl5zxq0)<br>
[EDA-NLP-PubMed-and-bioRxiv.ipynb](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EDA_NLP_bioRxiv_and_PubMed.ipynb)[<img src="https://colab.research.google.com/assets/colab-badge.svg" align="center">](https://colab.research.google.com/drive/1kqvGYRZZimVV4DtI-2TIbQp3NyOkqtaI)<br>
#### [How to use]()


# Examples

## Connectome 

**PubMed - https://www.ncbi.nlm.nih.gov/pubmed/?term=connectome**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/bioRxiv.pdf)

**2,372 Results.**

**bioRxiv - https://www.biorxiv.org/search/Connectome**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/bioRxiv.pdf)

**4568 Results.**

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**PubMed** &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp;&emsp; &emsp;&emsp; &emsp; &emsp; &emsp;&emsp;&emsp;&emsp;**bioRxiv**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/t-sne/pubmed_3d.gif" width="430" height="380">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/t-sne/biorxiv_3d.gif" width="430" height="380">
  </p>


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Words Cloud**


<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/words_cloud/pubmed_worldcloud_with_mask%20(3).png" width="430" height="360">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/words_cloud/biorxiv_worldcloud_with_mask.png" width="430" height="360">
  </p>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Similar Words**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/similar_words/similar_words.png" width="430" height="360">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/connectome/similar_words/similar_words_biorxiv.png" width="430" height="360">
  </p>



## Coronavirus 2019-nCoV 

**42 Results.**

**PubMed - https://www.ncbi.nlm.nih.gov/pubmed/?term=coronavirus+2019-nCoV**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/coronovirus/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/Connectome/PubMed.pdf)

**bioRxiv - https://www.biorxiv.org/search/coronavirus%252B2019-nCoV**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/coronovirus/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/Connectome/bioRxiv.pdf)

**72 Results.**

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**PubMed** &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp;&emsp; &emsp;&emsp; &emsp; &emsp; &emsp;&emsp;&emsp;&emsp;**bioRxiv**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/coronovirus/t-sne/pubmed_3d%20(1).gif" width="430" height="380">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/coronovirus/t-sne/biorxiv_3d%20(1).gif" width="430" height="380">
  </p>


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Words Cloud**


<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/coronovirus/words_cloud/pubmed_worldcloud_with_mask.png" width="430" height="360">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/coronovirus/words_cloud/biorxiv_worldcloud_with_mask.png" width="430" height="360">
  </p>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Similar Words**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/coronovirus/similar_words/pubmed_similar_words.png" width="430" height="360">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/coronovirus/similar_words/biorxiv_similar_words.png" width="430" height="360">
  </p>
  
  
## Schizophrenia

**PubMed - https://www.ncbi.nlm.nih.gov/pubmed/?term=Schizophrenia**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/PubMed.pdf)


**5,000 out of 141,489 Results.**

**bioRxiv - https://www.biorxiv.org/search/Schizophrenia**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/bioRxiv.pdf)

**4,102 Results.**

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**PubMed** &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp;&emsp; &emsp;&emsp; &emsp; &emsp; &emsp;&emsp;&emsp;&emsp;**bioRxiv**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/t-sne/pubmed_3d.gif" width="430" height="380">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/t-sne/biorxiv_3d.gif" width="430" height="380">
  </p>


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Words Cloud**


<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/words_cloud/pubmed_worldcloud_with_mask.png" width="430" height="360">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/words_cloud/biorxiv_worldcloud_with_mask.png" width="430" height="360">
  </p>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Similar Words**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/similar_words/pubmed_similar_words.png" width="430" height="360">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/shizoprhenia/similar_words/biorxiv_similar_words%20(1).png" width="430" height="360">
  </p>
  
  
## Raspberry Pi


**PubMed - https://www.ncbi.nlm.nih.gov/pubmed/?term=raspberry+pi**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/PubMed.pdf)


**143 Results.**

**bioRxiv - https://www.biorxiv.org/search/raspberry%252Bpi**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/bioRxiv.pdf)

**184 Results.**

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**PubMed** &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp;&emsp; &emsp;&emsp; &emsp; &emsp; &emsp;&emsp;&emsp;&emsp;**bioRxiv**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/t-sne/pubmed_3d.gif" width="430" height="380">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/t-sne/biorxiv_3d.gif" width="430" height="380">
  </p>


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Words Cloud**


<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/words_cloud/pubmed_worldcloud_with_mask.png" width="430" height="360">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/words_cloud/biorxiv_worldcloud_with_mask.png" width="430" height="360">
  </p>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Similar Words**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/similar_words/pubmed_similar_words.png" width="430" height="360">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/raspberry_pi/similar_words/biorxiv_similar_words.png" width="430" height="360">
  </p>
  
  
## Electroactive Polymers  

**PubMed - https://www.ncbi.nlm.nih.gov/pubmed/?term=Electroactive+Polymers**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/PubMed.pdf)

**860 Results.**

**bioRxiv - https://www.biorxiv.org/search/Electroactive%252BPolymers%252B**

[![Foo](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/pdf_logo.png)](https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/bioRxiv.pdf)

**13 Results.**


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**PubMed** &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp;&emsp;&emsp; &emsp;&emsp; &emsp; &emsp; &emsp;&emsp;&emsp;&emsp;**bioRxiv**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/t-sne/pubmed_3d.gif" width="430" height="380">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/t-sne/biorxiv_3d.gif" width="430" height="380">
  </p>


&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Words Cloud**


<img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/words_cloud/pubmed_worldcloud_with_mask.png">

<img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/words_cloud/biorxiv_worldcloud_with_mask.png">
 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;**Similar Words**

<p>
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/similar_words/pubmed_similar_words.png" width="430" height="360">
    <img src="https://github.com/OldBonhart/EDA-NLP-PubMed-and-bioRxiv/blob/master/EAPs/similar_words/biorxiv_similar_words.png" width="430" height="360">
  </p>


