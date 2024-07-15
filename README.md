# graphrag-biomedical
Implement GraphRAG on Bio-Medical Text Corpus

## Pre-Requisities :-
1. OpenAI API Key ( Or Groq API Key )
2. LM Studio ( For Embedding Model to run locally )
   
## Execute the following Commands to setup GraphRAG :

python -m pip install graphrag
mkdir input

## To Import Medical Text in PDF Format to Text :
python -m pip install pymupdf
python parse_pdf.py

## Initialise GraphRAG in the directory :
python -m graphrag.index --init --root .
[ Setup settings.yaml file according to API Specifications & Input Data ]

## GraphRAG Indexing :
python -m graphrag.index --root .
[ Indexer is cached, as a result Rate Limit API Errors can be handled ]

## Run a GraphRAG Query :
python -m graphrag.query --root . --method global "What is the main focus of the paper?"
python -m graphrag.query --root . --method local "Explain the methods explored in this paper about breast cancer ?"
