# Python for Linguists 2023

## 28. Advanced text processing

Effort profile: `▂▂▁▁▁▁▂▂▁▁▁▁▂▂▄▅▂▂▂▂▁▁▄▅▂▄▅▂▂▁▄▅▄▅▁▂▁▄▅` 



**28.1.** ⭐ The first step for text processing is typically tokenization. Use web search to compile your own list of possible Python approaches to **tokenization**. Summarize your findings. (What were your search queries?)

**28.2.** ⭐ Chances are you found the **spaCy** library, which we will use in the exercises of this section. From the spaCy website, extract an overview of the main functionalities offered by this library.

**28.3.** Which languages does spaCy (claim to) support? Would it be fair to complain that the field of Natural Language Processing (or Artificial Intelligence more generally) does not currently benefit everyone equally? Consider both arguments for and against the validity of this complaint.

**28.4.** What is meant by a 'pipeline' in natural language processing in general, and spaCy in particular? What is the role of a `Doc` object in spaCy?

- - - - - -
**Something to keep in mind:** A pivotal programmers' skill is translating your own problems into those which other people have likely had to solve before you. Concretely, this often means finding a relevant library and learning to use it, by browsing documentation, looking at the library's source code, and searching forums such as StackOverflow. This will also be necessary for the exercises in this section.
- - - - -

**28.5.** If you haven't already, install the spaCy library. This might be as simple as typing `import spacy` in a `.py` file and waiting for PyCharm to offer installing it for you. If that fails, look for the official spaCy installation instructions.

**28.6.** The spaCy library provides an interface to various _models_, each specialized in a certain language or a certain type of processing task. These models can be quite large (in terms of disk space, download time), and so must be downloaded separately. This can be done within PyCharm by typing, in the _Terminal_ tab (not the Python Console): `python -m spacy download en_core_web_sm`, for instance, to download the English 'core model' trained on web text, small version. Try this, and try to resolve any problems you encounter with the help of the documentation and web search.

**28.7.** ⭐ Use spaCy to process a number of example strings (for a spaCy-supported language of choice), and find a way to inspect its sentence segmentation. Can you construct examples that _trick_ spaCy into a faulty sentence segmentation (recall from the previous section what kinds of examples can trick the simple approach of splitting on punctuation)?

**28.8.** ⭐ Find a way to inspect spaCy's word tokenization for a given string. Can you construct example strings that trick spaCy into a faulty word tokenization?

**28.9.** Write code to access, say, the third token of a spaCy `Doc`.

**28.10.** What type of object is a token in Spacy? What attributes/methods does it offer (e.g., use `help` or `dir`)? Two attributes of tokens are `i` and `idx`. From trying `doc[3].i` and `doc[3].idx`, can you guess what these numbers represent? Verify your understanding by consulting the documentation.

**28.11.** Write code to access, say, the third _sentence_ of a spaCy `Doc`. Since `Doc.sents` returns a generator, you need to collect its elements in a `list` before you can access them by index. What type of object is a sentence? What attributes and methods does it offer? 


**28.12.** Can you also select a _span_ of tokens (say, the span consisting of tokens 3 to 6), simply by using slicing on the `doc` as we did with lists? Check what type of object this creates, and what attributes and methods it offers.


**28.13.** ⭐ The spaCy tokenizer is likely better than our own earlier attempts. But how does it work, anyway? Have a look here for the basics: https://spacy.io/usage/linguistic-features#tokenization. Explain in your own words how it identifies the token _N.Y._ in the example, _She said: "Let's go to N.Y.!"_. (For a more detailed understanding, click on "Algorithm details: How spaCy's tokenizer works" and scroll down to the 11-step summary.)

**28.14.** ⭐ The spaCy **source code** is in part Python and freely available. Have a look at https://github.com/explosion/spaCy/blob/master/spacy/lang/en/tokenizer_exceptions.py, and scroll through it. Try to understand, if not the exact functioning, at least the relevance of the various portions of code it contains, and appreciate the amount of detail that goes into a library like spaCy, even for something as (seemingly) elementary as tokenization (and for just one language). (Perhaps interesting to note: in some places spaCy relies on regular expressions, e.g., here: https://github.com/explosion/spaCy/blob/master/spacy/lang/en/punctuation.py).


<br>**_Named entities, parts of speech, dependencies_**

**28.15.** ⭐⭐ Write a function `print_tokens` that takes a spacy-processed document as input, and prints all its tokens, one per line, each accompanied by its _lemma_ (i.e., standardized, inflectionless form), _part of speech_, _dependency_ and _head_, and its _named entity_ label. For instance, for the sentence 'Bob thinks Mary likes him', it should print (among other tokens) `Bob <Bob> (PROPN, nsubj of thinks) [PERSON]` and `likes <like> (VERB, ccomp of thinks) []`. Use this function to inspect spaCy's analysis for a number of simple sentences.

**28.16.** ⭐ Write a function that takes a spaCy-processed document as input, and returns a `Counter` of all **parts of speech**. In a text of your choice, what are the most common parts of speech?


**28.17.** ⭐ Write a function that takes a spaCy `Doc` object as input, and returns a Counter of all **named entity** types in the document. In a text of your choice, what are the most common named entity types? Do you expect this to differ between genres?

**28.18.** ⭐ Read the spaCy documentation about **dependency parses** (https://spacy.io/usage/linguistic-features#dependency-parse). Dependency structure is a framework for syntax that tends to be a bit friendlier toward cross-linguistic generalization and computational applications than _constituency structure_ (the type of syntax you are likely familiar with). Describe in your own words how dependency structure relates to (and differs from) constituency structure.

**28.19.** ⭐ As a warming-up with dependency parses, use your `print_tokens` function from earlier to inspect the dependency structure of various simple syntactic structures. Try to draw the corresponding dependency trees on a piece of paper.

**28.20.** The root of the dependency tree for a given sentence (or other span, e.g., a noun phrase) is accessible with `.root`. Use it to print the root (typically the main verb) of an example sentence. Note that this requires that you access a _sentence_ in the `Doc`, using the `.sents` attribute. Why is there no `.root` attribute on a `Doc` object?

**28.21.** Because of the foregoing, you may find it convenient (for testing some code on a single sentence) to have a function `spacy_sent` that takes a single sentence (as a string), applies spaCy to it, and returns spaCy's analysis of that single sentence directly (instead of the `Doc` object containing it). Define such a function.

- - - - - -
**Something to keep in mind:** In general when programming, but especially when learning to use a new library, it is crucial to keep in mind _what type of object are you working with?_ A string? A spacy `Doc`? A spacy `Span`, such as a sentence? A single token? And also: _what type of object do you need_, in order to solve the task? Different objects offer different methods. Don't hold back on inserting `print(type(...))` statements frequently (during development and debugging) to check what you are dealing with.
- - - - -



-------

**_Homework exercises for week 14 end here, now do Mini-project [P](../projects/P_extracting_dialogues_from_a_book.md) (and don't forget to submit! ✉️)._**

-------


**28.22.** ⭐⭐ Write a function `get_verb_frame` that takes a single spaCy-processed sentence as input and returns a tuple of the main verb with its direct `nsubj` and `dobj` descendants, if present (this is a simplification of all possible verb frames, of course). Note that for sentences with multiple verbs, e.g., 'John noticed that Mary was sad.', only the arguments of the main verb (in this case 'noticed') should be returned.

**28.23.** ⭐ Consider the function below, and note that it _calls itself_, i.e., it is a **recursive definition**. For a given `sentence` for which you drew a dependency tree earlier (based on the info from `print_tokens`), try to predict the exact order in which that sentence's tokens would get printed by `print_dependency_tree(sentence.root)`. Then test your prediction and verify your understanding. (How come the function calling itself does not result in an infinite loop?)

```python
def print_dependency_tree(token):
    print(f'{token.dep_}: {token.text}')
    for child in token.children:
        print_dependency_tree(child)
```


**28.24.** ⭐⭐ For increased readability, modify the above function in such a way that each printed token is indented (i.e., prefixed with whitespace) one level further than its parent.

**28.25.** ⭐ For a text of your choice, find all sentences where a subject precedes the verb, and all places where a verb precedes the subject.   


**28.26.** ⭐ For a text of a (spaCy-supported) language of your choice, write a program to determine which aspectual structure is more common: progressive ('be <verb>+ing' in English) or perfect ('have <verb>+ed').


**28.27.** If you haven't already, check the spaCy documentation about **morphology** (https://spacy.io/usage/linguistic-features#morphology) and enrich your `print_tokens` function from earlier, to print also the `morph` feature of each token. Use it to inspect some progressive and perfect example sentences. Can you use `morph` to improve your solution to the previous exercise?



**28.28.** ⭐⭐ Write a function `get_path_to_root` that takes a spaCy-processed sentence (not a full `doc`, which does not have a _root_) and a token from that sentence, and returns the dependency path from that token back to the sentence's root. It should return the path as a list of tokens, the first being the start token and the last being the root. (This function will likely be useful for the mini-adventure below.) In case you're stuck, try to formulate intuitively how one would search for a path to the root, e.g., something like 'As long as the current node is not yet the root node, do ...', and then translate this into code. 


**28.29.** ⭐⭐ Write a function that takes a spaCy-processed `Doc` as input and returns all _embedded clauses_ (e.g., the italicized parts of 'John knows _that Mary is old_', 'John wonders _if Mary likes him_'). As before, first apply `print_tokens` to a couple of relevant examples, to know what you need to be looking for. (Another tip: for a given token `tok`, use `list(tok.subtree)` to obtain the subtree headed by that token.) Do the results of your function include reported speech (e.g. '_I'm not happy_ he said')? Infinitival complements (e.g., 'I love _to go running with my boyfriend_')?



**28.30.** SpaCy tokens, spans (e.g., sentences) and docs all have an attribute `vector`, which stores a (kind of) distributional semantic vector representation of the word/span/doc. Retrieve the vector of a token of choice and inspect it. What does it look like if you `print` it? What `type` of object is it? When regarded as a point in high-dimensional space, how many dimensions does the space have in which Spacy's vectors live? (Don't just manually count vector values to answer this; there has to be a better way...) Can you add the vectors of two or more words together? 

**28.31.** ⭐ Does the vector of a token depend on the context (e.g., neighboring tokens) in which that token occurs? Test this with code. As it turns out, the answer to this question can depend on which model you use. Consider comparing `en_core_web_sm` to `en_core_web_md`, as well as to `en_core_web_trf` (a so-called 'transformer' model; if your computer can handle it). Do you think such context-dependence is a desirable feature?

**28.32.** Write code to test whether the vector that spaCy assigns to a sentence, is equivalent to the average of the vectors it assigns to the tokens. You can probably find this in the documentation, but writing your own test is a useful exercise.

**28.33.** ⭐⭐ Write code that processes a text with spaCy and then asks (e.g., with `input`) for a sentence from the user. It should then retrieve a sentence from the text, whose vector is _most similar_ to the vector of the query sentence. Search the web for instance for `cosine similarity on numpy arrays` to see how you can compute vector similarity. Consider placing everything from `input` onwards in a `while`-loop, to easily test multiple queries on the same text without it having to re-process the entire text all over again each time. Assess the behavior of your 'similar sentence search engine', e.g., does it reflect semantic similarity, syntactic similarity, or both -- or neither? Consider using a larger model (e.g., `en_core_web_md` or even `en_core_web_trf`) if the smaller model yields poor results.

- - - - - -
**Something to keep in mind:** SpaCy is a powerful and versatile computational tool for linguists, and more so than this section can show. In case you want to learn more, besides browsing the documentation, be sure to check also the free, online spaCy course: https://course.spacy.io/ .
- - - - -



-----

**_🐧 You are now ready for [Mini-project Q](../projects/Q_gender_bias.md)!_**

-----

**_🐧 You are now ready for [Mini-project R](../projects/R_similarity.md)!_**

-----

**_🐧 You are now ready for [Mini-project S](../projects/S_question_extraction_and_classification.md)!_**