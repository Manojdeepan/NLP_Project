# date_time_extractor.py

import spacy
import dateparser

# Load spaCy's English language model
nlp = spacy.load('en_core_web_sm')

def extract_dates_and_times(text):
    """
    Extracts date and time entities from input text using spaCy and dateparser.

    Args:
        text (str): Input text containing date/time information.

    Returns:
        List[dict]: A list of dictionaries containing details about each detected entity.
    """
    doc = nlp(text)
    extracted_entities = []

    # Extract entities labeled as DATE or TIME using spaCy
    for ent in doc.ents:
        if ent.label_ in ['DATE', 'TIME']:
            parsed_time = dateparser.parse(ent.text)
            extracted_entities.append({
                'entity_text': ent.text,
                'entity_label': ent.label_,
                'start_position': ent.start_char,
                'end_position': ent.end_char,
                'parsed_time': parsed_time
            })

    # Additional relative date phrases not always recognized by spaCy
    relative_phrases = [
        "tomorrow", "next day", "day before yesterday", "yesterday", 
        "next week", "last week", "next month", "last month", 
        "next year", "last year", "in two days", "in three days", 
        "last Monday"
    ]

    # Manually check for relative date phrases in the text
    for phrase in relative_phrases:
        if phrase in text.lower():
            parsed_time = dateparser.parse(phrase)
            extracted_entities.append({
                'entity_text': phrase,
                'entity_label': 'RELATIVE_DATE',
                'parsed_time': parsed_time
            })

    return extracted_entities

# Example usage
if __name__ == "__main__":
    sample_text = """
    Meet Greg tomorrow at 5 PM. We need to review last week’s project.
    The report was submitted the day before yesterday, and the meeting is next Monday at 10 AM.
    """

    results = extract_dates_and_times(sample_text)

    for entity in results:
        print(f"Entity: {entity['entity_text']}, Label: {entity['entity_label']}, Parsed: {entity['parsed_time']}")
