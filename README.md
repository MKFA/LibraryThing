# LibraryThing
Scripts to extract FMP IDs for exhibitions and artworks out of a LibraryThing tsv export.

1. LT-FMPid-Extract.py This script creates one row per FMP ID and repeats the Book ID as many times as necessary.
2. FMPid3column.py This script has one row per Book ID and three columns for FMP IDs: Art ID, Exhibition ID, Artwork ID.

Note:
1. TSV exports use pipes to delimit some multivalue field values (Secondary Authors) and commas for others (Language). 
2. Paragraph breaks sometimes, but not always export as "[Return]"
3. Diacritics don't always export correctly and need manual correction ("Fonds régional d'art contemporain" exports as "Fonds reÃÂgional d'art contemporain")

# How to run
You can run these scripts on a MacBook Pro, by following these steps:

1. **Open Terminal**: You can find Terminal in the Applications folder under Utilities, or you can use Spotlight (Command + Space) and search for "Terminal".

2. **Navigate to the directory containing your Python script**: You can use the `cd` command to change directories. For example, if your script is located in the Documents folder, you can navigate there like this:
   ```
   cd Documents
   ```

3. **Run the script**: Once you're in the directory containing your Python script, you can run it by typing `python` followed by the name of your script. For example:
   ```
   python your_script.py
   ```

If you're using Python 3, you might need to use `python3` instead of `python` depending on your system configuration. 

For example:
   ```
   python3 your_script.py
   ```

Make sure you have Python installed on your Mac. macOS usually comes with Python 2.7 installed by default, but it's recommended to use Python 3.x for new development. You can install Python 3 using tools like Homebrew or by downloading it directly from the Python website.

That's it! Your Python script should now run in the Terminal window. Any output or errors will be displayed in the Terminal.
