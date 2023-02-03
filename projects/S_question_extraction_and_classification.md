# Python for Linguists 2023

## Mini-project S: Question extraction and classification

**_Finish [Section 28](../exercises/28_advanced_text_processing.md) before attempting this project._**



**S.1.** ⭐ Use a regular expression to extract _questions_ from a text of your choice (namely: sentences ending in a question mark), and write a function that takes these questions and categorizes them based on the wh-words they contain (such as _who_, _what_, _where_). Your categorization should also reflect multiple-wh-questions (e.g., assign the category 'who-what' to a multiple-wh-question like 'Who did what?'), and have a category 'yesno' for 'yes/no questions', i.e., that lack a wh-word. 

**S.2.** Feed the categories you find into a Counter and inspect your findings. Try to identify some shortcomings of your approach, especially ones where you think some of the linguistic features computed by spaCy might help.

**S.3.** ⭐⭐⭐ To overcome some of the shortcomings you likely identified, define an auxiliary function `extract_wh_word` that takes a spaCy analysis for a given question, and loops through its tokens to find the question's wh-word (if any). Some complexities it should handle (start simple, then try to solve these one at a time):
 - The wh-word is not necessarily the first token in a sentence (e.g., 'And what product did you buy?', 'And you bought what?', 'You went where?'). 
 - Conversely, not every wh-word makes for a wh-question (e.g., 'What John did was bad?', 'Did you like what you bought?', 'Did you see who called?'); these do _not_ count as wh-words (for our purposes). 
 - For an extra challenge, try to handle multiple-wh questions ('Who bought what?'), representing their category by a _tuple_ of wh-words.

 As a starting point, compile a list of challenging questions (e.g., the examples above) and use spaCy and `print_tokens` to inspect their linguistic features, to hopefully come up with plausible rules for detecting genuine wh-words (i.e., ones that make it a wh-question, see above). (Hint 1: Your earlier function `get_path_to_root` may be useful here. Hint 2: spaCy itself can make mistakes, just accept this as a source of error and don't spend too much effort on trying to correct or bypass spaCy.)

**S.4.** ⭐⭐ Write another auxiliary function, this time for categorizing **non-wh-questions** in a meaningful way. In particular: 
 - Distinguish _interrogative_ non-wh-questions (e.g., 'Did you run?') from so-called _rising declaratives_ (declarative syntax but used as a question, typically indicated by rising intonation, e.g., 'You arrived yesterday?'). 
 - Depending on your source text, you may also encounter many _elliptical questions_, where, e.g., the auxiliary is omitted ('You arrive yesterday?', the tenselessness indicating missing auxiliary 'Did...') or even the main verb (e.g., 'That guy?', meaning 'Is that guy the famous artist you mentioned?'). Assign such verb-elliptical, non-wh-questions to a separate category.

**S.5.** ⭐ Combine both auxiliary functions into one that takes a question (as a string) and returns its category (or categories), represented as a (tuple of) short string(s) (e.g., the question's wh-word(s) `.lemma_`, or a label like `DECL` for rising declaratives, etc.).

**S.6.** ⭐ Apply your categorization function to questions extracted from a text (in a spaCy-supported language of choice), and manually go through the assigned categories. Refine your system where needed (and possible), and in the end inspect a random sample to assess the **accuracy** of your system: What proportion of questions is correctly categorized? Which of your categories is the most heterogeneous, hence, could benefit from a further subdivision?

- - - - - -
**Something to keep in mind:** Whenever you automate part of your linguistic analysis, you must assess its quality. This is typically done by comparing the system's outputs to an expert-annotated **gold standard**. _Accuracy_, or the proportion of responses that are correct, is one metric for quantifying quality. Other common metrics are per-category _precision_ (% of responses of a category X that are correct) and _recall_ (% of actual category X items that are detected).
- - - - -

**S.7.** With the help of the `Counter` class, determine which categories of questions are the most common. _Optional:_ consider creating a _barplot_ of the counts, one bar for each question category. A suitable web query could be 'Python barplot from Counter'.

