# Date and Time Extractor (NLP Project)

## Project Overview
This repository contains a Natural Language Processing (NLP) project that extracts date and time expressions from text using **spaCy** and **dateparser**.  
The system identifies explicit dates and times (e.g., *"5 PM", "10 AM, 3rd September"*) as well as relative references (e.g., *"tomorrow", "last week", "day before yesterday"*), and converts them into structured datetime objects.

## Key Features
- **Named Entity Recognition (NER):** Uses spaCy to detect entities labeled as `DATE` or `TIME`.  
- **Date Parsing:** Integrates `dateparser` to convert extracted text into Python `datetime` objects.  
- **Relative Date Handling:** Recognizes phrases like *"yesterday", "next week", "last Monday"* that spaCy may miss.  
- **Entity Metadata:** Provides details such as entity text, label, character positions, and parsed datetime.  

## Repository Contents
- `date_time_extractor.py` – Python script implementing the extractor.  
- `README.md` – Project documentation.  



python date_time_extractor.py

Sample Input
Meet Greg tomorrow at 5 PM. We need to review last week’s project.  
The report was submitted the day before yesterday, and the meeting is next Monday at 10 AM.

Sample Output
Entity: tomorrow, Label: DATE, Parsed: 2025-09-06 17:00:00
Entity: last week, Label: RELATIVE_DATE, Parsed: 2025-08-29 00:00:00
Entity: day before yesterday, Label: RELATIVE_DATE, Parsed: 2025-09-03 00:00:00
Entity: next Monday, Label: RELATIVE_DATE, Parsed: 2025-09-08 10:00:00
Entity: 5 PM, Label: TIME, Parsed: 2025-09-05 17:00:00
Entity: 10 AM, Label: TIME, Parsed: 2025-09-08 10:00:00

## Usage

Clone or download this repository.

Install dependencies:
  pip install spacy dateparser
python -m spacy download en_core_web_sm


Run the script:

  python date_time_extractor.py

Modify the sample_text variable in the script to test custom input.

Tools and Technologies

Python 3.x

spaCy (en_core_web_sm model)

dateparser

Author

Manoj Deepan M


