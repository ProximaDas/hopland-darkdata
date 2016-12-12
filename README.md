# hopland-darkdata

This is the code repository for extracting information from historic research documents at Hopland. These code files form a part of the information extraction process that was used to extract entities, concepts and keywords from research documents that potentially were going 'dark'.
The workflow for the process consists of the following major steps:

* Convert PDF files into text using an OCR tool (we used Google Tesseract here)
* Use IBM Watson's Natural Language Processing API to extract higher level concepts and entities from text
