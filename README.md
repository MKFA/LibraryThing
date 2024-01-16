# LibraryThing
Scripts to extract FMP IDs for exhibitions and artworks out of a LibraryThing tsv export.

1. LT-FMPid-Extract.py This script creates one row per FMP ID and repeats the Book ID as many times as necessary.
2. FMPid3column.py This script has one row per Book ID and three columns for FMP IDs: Art ID, Exhibition ID, Artwork ID.

Note:
1. TSV exports use pipes to delimit some multivalue field values (Secondary Authors) and commas for others (Language). 
2. Paragraph breaks sometimes, but not always export as "[Return]"
3. Diacritics don't always export correctly and need manual correction ("Fonds régional d'art contemporain" exports as "Fonds reÃÂgional d'art contemporain")

