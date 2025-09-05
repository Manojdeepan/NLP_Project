# Date and Time Extractor (NLP Project)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  
![spaCy](https://img.shields.io/badge/spaCy-NLP-green.svg)  
![dateparser](https://img.shields.io/badge/dateparser-TimeParsing-orange.svg)  
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## Project Overview
This repository contains a Natural Language Processing (NLP) project that extracts date and time expressions from text using **spaCy** and **dateparser**.  
The system identifies explicit dates and times (e.g., *"5 PM"*, *"10 AM, 3rd September"*) as well as relative references (e.g., *"tomorrow"*, *"last week"*, *"day before yesterday"*), and converts them into structured datetime objects.

## Key Features
- **Named Entity Recognition (NER):** Uses spaCy to detect entities labeled as `DATE` or `TIME`.  
- **Date Parsing:** Integrates dateparser to convert extracted text into Python datetime objects.  
- **Relative Date Handling:** Recognizes phrases like *"yesterday"*, *"next week"*, *"last Monday"* that spaCy may miss.  
- **Entity Metadata:** Provides details such as entity text, label, character positions, and parsed datetime.  

## Repository Contents
- `date_time_extractor.py` – Python script implementing the extractor.  
- `README.md` – Project documentation.  

## Sample Input
```text
Meet Greg tomorrow at 5 PM.  
We need to review last week’s project.  
The report was submitted the day before yesterday, and the meeting is next Monday at 10 AM.
