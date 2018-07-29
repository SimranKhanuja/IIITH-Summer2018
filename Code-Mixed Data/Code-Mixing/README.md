## Format for Input

### SampleHindi and SampleEnglish---->

* File with aligned sentences in both Hindi and English
* Hindi file to be parsed by the shallow Hindi Parser and given as input to the FormatHindiParse file
* English File to be parsed by the Stanford Parser and given to the EnglishHeadChunkExtraction file in a format as specified by the FormatForInputToEnglishHeadCode file

### HindiParsed and EnglishParsed---->
* These two files should be produced by running the above codes
* Files of this format to be given as input to NP_Replacement_Hindi(Hindi matrix language) and NP_Replacement_English(English Matrix Language)
* Code-mixed sentences produced in CodeMixedHindi and CodeMixedEnglish respectively!

### NiceSortEng.txt and NiceSortHin.txt---->
* These two files contain the giza++ alignments of the words after a simple post-processing.
* This post-processing involved sorting the file in descending order of probabilties grouped by each English word and then removing the word pairs with probabilities below 10% to reduce complexity and redundancy
