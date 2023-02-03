# Python for Linguists 2023

## 27. Advanced regular expressions (groups)

Effort profile: `(▄▅▁▁▂▁▁▁▂▂▁▁▁▂▁)` 




----

🦉 **_This entire section is OPTIONAL!_**

----


**27.1.** ⭐⭐ The following function takes an iterator over (or iterable of) matches, and returns the original text with brackets `[..]` around the matching substrings. For some input it _almost_ works (e.g., call it with, as its `matches` argument, the result of `re.finditer(r'abc', 'abc abc abc')`), but for other input it gives an error (e.g., `re.finditer(r'abc', 'abc abc def')`). Can you fix it?

```python
def contextualize_matches(matches):
    matches = list(matches)
    text = matches[0].string
    bracketed_text = []
    for i in range(len(text)):
        if matches[0].span()[0] == i:
            bracketed_text.append('[')
        bracketed_text.append(text[i])
        if matches[0].span()[1] == i:
            bracketed_text.append(']')
            matches.pop(0)
    return ''.join(bracketed_text)
```


**27.2.** Use the (now corrected) function `contextualize_matches` to review the outcome of some of the previous exercises (Section 24), e.g., all definite and indefinite articles in `example_string`:
```python
example_string = 'The famous Dr. Freud hastily acquired a magenta T-shirt and an old sweater for 24.95EUR. He then very very eagerly left the H&M at 1am... It was, as the doctor said, "a necessity".'
indefinite_regex = r'\b[Aa]n?\b'
definite_regex = r'\b[Tt]he\b'
articles_regex = indefinite_regex + '|' + definite_regex
```

**27.3.** You may wonder why the method for obtaining the matched substring is called `group`. Explore why, with the help of the regular expression `(\w+)ly`, in which the parentheses define a _group_ (containing just `\w+`). Use `re.finditer` to find all its matches on the `example_string` from earlier, and for each match object print both `match.group()` and `match.group(1)`.

- - - - - -
**Something to keep in mind:** Parentheses in a regular expression define **capture groups**, and a `Match` object will provide a matching substring for each separate group. Thus, `match.group(1)`, `match.group(2)` etc. are substrings matching what's in the first set of parentheses, the second set of parentheses, etc. Call `match.group()` to get the substring matching the entire regular expression.
- - - - -

**27.4.** ⭐ Define a regular expression containing a capture group, that lets you retrieve all vowel sequences (single vowels or multiple consecutive vowels) that are preceded by a consonant. Use the capture group to specifically print only the vowel part of each match.

**27.5.** What happens if your regular expression contains no round parentheses (i.e., no capture groups defined), and on a given match you call `match.group(1)`? What about `match.group(0)`? Explain the relation to `match.group()` in terms of the notion of 'default value'.

**27.6.** Does the `span` method of a `Match` object likewise take an integer argument? Does it do what you would expect?

**27.7.** Recall from the start of this section that `re.findall` returns the matching substrings directly, so no `Match` objects with groups and spans. How does `re.findall` (and hence your helper function from Section 24, `test_regexes`) handle capture groups? Investigate this by matching the regular expressions `ab`, `(a)b`, `(a)(b)` and `((a)b)` against a simple string such as `'abab'`.

**27.8.** ⭐ Although round parentheses `(...)` have a special meaning in regular expressions, namely capture groups, they are also still used for governing **operator precedence**. Explain which patterns the following regular expressions match (some may match the same). (To avoid confusion, use `finditer` to test these expressions, not `findall`, because of how the latter implicitly handles capture groups.) 
 - `(ab)+` 
 - `a+b+` 
 - `ab+` 
 - `(ab+)` 
 - `a(b+)`

**27.9.** ⭐ Recall your mathematical expression from a while back (for summation, subtraction, etc.). Generalize it to also accept floating point numbers (e.g., `0.151 + 6512.36432`). (Note that only a single period per number is permitted, e.g., not `0.52.312 * 65.1543`). Compose your regular expression from simpler building blocks using a format string literal (`f'...'`).

**27.10.** If your regular expression defines a capture group, you can invoke it in the same regular expression with a backslash-number, e.g., `\1` refers to the substring matched by group 1. Do you expect `(\w)\1` to match anything on `example_string`? Test your understanding.

**27.11.** Could the regular expression `(h[aeio])\1+` be used to detect grammatically well-formed laughter?

**27.12.** Can you predict what `(\b\w+\b)\s\1` will match? Test it on `example_string` (again, `finditer` is advised, given the way `findall` implicitly handles capture groups). To check your understanding of the 'greedy' nature of regular expression matching (see earlier), can you predict the number of matches it will have on the string `test test test`?

**27.13.** ⭐ Let's take another look at a text of your choice (e.g., from Project Gutenberg). What are the most frequently reduplicated words?

**27.14.** Compare the following two regular expressions, intended for a simple sentence tokenizer using `re.split`, and verify your understanding of the difference by reading in the Python documentation how `re.split` is supposed to handle capture groups (e.g., `help(re.split)`). Can you conceive of a scenario (e.g., research or application) for which the second sentence tokenizer might be more convenient than the first? 
 - `[.!?]+` 
 - `([.!?]+)`


