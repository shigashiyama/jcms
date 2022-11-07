# A Japanese Corpus of Many Specialized Domains (JCMS)

## Overview

The JCMS consists of 32,310 sentences annotated with word boundary and POS tag 
information for 27 specialized domains.
The corpus adopted two segmentation criteria (and corresponding POS tag sets): 
- short unit word (SUW), which was designed by the NINJAL, and
- SUW-SC, which we defined by separating conjugate words into stems and conjugation 
  endings.

The corpus statistics is as follows.

|Source          |ID   |Domain                            |Domain            |#Sent.
|----------------|-----|----------------------------------|------------------|-----:
|ASPEC           |AGR  |Agriculture, forestry, fisheries  |農林水産          |   900
|ASPEC           |BIO  |Biology                           |生物科学          | 1,000
|ASPEC           |CHE-B|Basic chemstry                    |基礎化学          | 1,700
|ASPEC           |CHE-E|Chemical eng.                     |化学工学          |   750
|ASPEC           |CHE-I|Chemical industry                 |化学工業          |   950
|ASPEC           |CON  |Construction eng.                 |建設工学          | 1,700
|ASPEC           |ELC  |Electrical eng.                   |電気工学          | 2,000
|ASPEC           |ENE  |Energy eng.                       |エネルギー工学    | 1,360
|ASPEC           |ENV  |Environmental eng.                |環境工学          |   870
|ASPEC           |ETH  |Earth and space eng.              |地球惑星科学      | 1,000
|ASPEC           |INF  |Information eng.                  |情報工学          |   900
|ASPEC           |MAN  |Eng. management                   |経営工学          | 1,500
|ASPEC           |MEC  |Mechanical eng.                   |機械工学          | 1,750
|ASPEC           |MED  |Medicine                          |医学              | 1,300
|ASPEC           |MIN  |Mining eng.                       |鉱山工学          |   640
|ASPEC           |NUC  |Nuculear eng.                     |原子力工学        |   800
|ASPEC           |PHY  |Physics                           |物理学            | 1,000
|ASPEC           |SYS  |System control eng.               |システム・制御工学| 1,500
|ASPEC           |THM  |Thermal eng.                      |熱工学            | 1,500
|ASPEC           |TRA  |Traffic and transportation eng.   |運輸交通工学      | 1,430
|NTCIR-8 PatentMT|PAT  |Patent                            |特許明細書        | 1,000
|NTCIR-11 MedNLP2|EMR  |Electronic medical record         |電子カルテ        | 1,362
|BCCWJ           |LAW  |Law (OL)                          |法律              | 1,060
|BCCWJ           |DIE  |Diet minute (OM)                  |国会議事録        |   650
|BCCWJ           |PRM  |PR magazine (OP)                  |広報紙            | 1,238
|BCCWJ           |TBK  |Textbook (OT)                     |教科書            | 1,650
|BCCWJ           |VRS  |Verse (OV)                        |韻文              | 1,000


## Data Sources

The JCMS consists of sentences from the following corpora.

- ASPEC <http://lotus.kuee.kyoto-u.ac.jp/ASPEC/>
- BCCWJ <https://pj.ninjal.ac.jp/corpus_center/bccwj/subscription.html>
- NTCIR-9 PatentMT test collection <http://research.nii.ac.jp/ntcir/permission/ntcir-9/perm-ja-PatentMT.html>
- NTCIR-11 MedNLP2 test collection <http://research.nii.ac.jp/ntcir/permission/ntcir-11/perm-ja-MedNLP.html>

To use the JCMS, it is required to sign the data use agreements and obtain the 
original data of BCCWJ, ASPEC, and NTCIR-9 PatentMT and NTCIR-11 MedNLP2 test 
collectins.

## Requirements

- The original data of ASPEC, BCCWJ, NTCIR-9 PatentMT test collection, and NTCIR-11
  MedNLP2 test collection
- Python 3
- sed
- awk
- zenhan <https://pypi.org/project/zenhan/0.5/>

## Files

~~~~
+-- data_source      ... Directory for placing original data
+-- script           ... Scripts for generating annotated data
+-- suw              ... SUW anntation data
| +-- mask           ... Annotated data with masked words 
| +-- proc           ... Processed annotated data will be placed here.
+-- suw-sc           ... SUW-SC annotation data
| +-- proc           ... Processed annotated data will be placed here.
+-- text             ... Raw text data
  +-- org            ... Raw text data extracted from original data will be placed here.
  +-- proc           ... Processed text data will be placed here.
  +-- tmp            ... Temporary directory
~~~~

## How to Use

The following steps generate the complete JCMS data from the original text data and 
masked JCMS data. This requires 300MB of disk space, but step 6 deletes 200MB of data.

1. Create aliases in `data_source`  
   ~~~~
   ln -s /path/to/ASPEC          data_source/ASPEC
   ln -s /path/to/BCCWJ          data_source/BCCWJ
   ln -s /path/to/NTCIR_PatentMT data_source/NTCIR_PatentMT
   ln -s /path/to/NTCIR_MedNLP2  data_source/NTCIR_MedNLP2
   ~~~~

2. Extract text from original data and save it in `text/org`  
   ~~~~
   ./script/extract_text_ASPEC.sh
   ./script/extract_text_BCCWJ.sh
   ./script/extract_text_PatentMT.sh
   ./script/extract_text_MedNLP.sh
   ~~~~

3. Generate SUW-SC annotated data from text and masked data, and save it in `suw-sc/proc`
   ~~~~
   ./script/restore_suw-sc_data.sh
   ~~~~

4. Generate SUW annotated data from SUW-SC data and save it in `suw/proc`
   ~~~~
   ./script/restore_suw_data.sh
   ~~~~

5. Generate raw text data from SUW-SC data and save it in `text/proc`.  
   The resulting data differs from the data in `text/org` w.r.t.  
   character normalization and character error correction.
   ~~~~
   ./script/extract_text_from_suw-sc_data.sh
   ~~~~

6. Remove unnecessary data (Optional)
   ~~~~
   rm -r text/tmp/*
   ~~~~


## Contact

Shohei Higashiyama  
National Institute of Information and Communications Technology (NICT), Seika-cho, Kyoto, Japan  
shohei.higashiyama [at] nict.go.jp


## Acknowledgements
Part of this work was supported by the collaborative research between NICT and Fujitsu.
We used the Asian Scientific Paper Excerpt Corpus, NITCIR-9 PatentMT test collection, NTCIR-11 MedNLP-2 test collection, and Balanced Corpus of Contemporary Written Japanese to construct the JCMS.


## Citation

Please cite the following paper.

~~~~
@inproceedings{higashiyama2022,
    title = {A Japanese Corpus of Many Specialized Domains for Word Segmentation and Part-of-Speech Tagging}
    author = {Higashiyama, Shohei and Ideuchi, Masao and Utiyama, Masao and Oida, Yoshiaki and Sumita, Eiichiro}
    booktitle = {Proceedings of the 3rd Workshop on Evaluation and Comparison of NLP Systems (Eval4NLP)}
    month = Nov,
    year = 2022,
}
~~~~
