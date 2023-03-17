# Python for Linguists 2023

## 21. Iterators, generators, and memory usage

Effort profile: `(▁▁▁▁▁▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▂▄▅▁▂▁▂▁▂)` 



----

🦉 **_This entire section is OPTIONAL!_**

----


This section introduces some new keywords and built-ins, but it mainly serves to increase your understanding of Python constructs that you are already using a lot, such as for-loops. The section is a bit dry, but it also has practical applications: if you need to process a large amount of data, using iterators and generators can help prevent clogging up your computer's memory.

**21.1.** Python's `yield` keyword can appear inside a function, much like `return`, but it does something different. Check what type of object the following function returns.

```python
def count_to_three():
    yield 1
    yield 2
    yield 3
```



**21.2.** Assign the object that is returned by the above function to a variable; call it, for instance, `my_counter`. Next, can you predict what the following code does? What do you think will be the values of `a` and `b`? Verify your prediction. 
```python
a = next(my_counter)
b = next(my_counter)
```



**21.3.** What happens if you keep calling `next` on the object stored in `my_counter`? By looking at the original function definition, do you understand why?


**21.4.** Previously you noticed that an Exception is raised (i.e., an error occurs) if the generator runs out of values to generate. What happens if you call the function `count_to_three` again? Does it create a fresh generator? Or does it continue and/or reset the one you already had? How can you tell?

**21.5.** What do you expect the following code to print? Check your prediction and make sure you understand the result.
```python
print(count_to_three())
print(count_to_three())
print(count_to_three())
```

**21.6.** Verify that the following function behaves exactly the same as `count_to_three`:
```python
def count_to_three_new():
    for n in [1, 2, 3]:
        yield n
```

**21.7.** We have seen that `yield`-functions return a `generator` object, which then, each time `next` is called on it, returns the yielded elements one at a time. Instead of manually calling `next` several times, demonstrate with code that we can also loop over the returned generator (same syntax as if you would loop over a list). (Remember to create a new generator, in case the previous one is 'used up'.)

**21.8.** What do you expect will happen here? Check your prediction.
```python
counter = count_to_three()
for number in counter:
    print(number)

print('Let\'s do that again:')

for number in counter:
    print(number)
```

**21.9.** What about this variant? Why?
```python
for number in count_to_three():
    print(number)

print('Let\'s do that again:')

for number in count_to_three():
    print(number)
```

**21.10.** Do generators have a length, i.e., can you call `len` on them? Why might this be, conceptually?

**21.11.** ⭐ Write a `yield` function (a 'generator function') that returns a generator which lets you iterate through the alphabet (recall that you can do `import string` to access `string.ascii_lowercase`).


**21.12.** Write a generator function that takes a list of numbers as input, and yields the square of each number one at a time. Does this function also work if you give it a generator of numbers as input, instead of a list of numbers?


**21.13.** `yield`-functions are not the only way to create generators: the expression inside a **list comprehension**, recall, likewise creates a generator object (whose elements are then collected in a list). Verify this by checking the type of `new_list_generator` below. (To isolate the generator object, simply omitting the square list brackets does not work, it requires round parentheses, that's just how Python's syntax is defined.) Does this generator work as you would expect, given what you have learned about the kinds of generators returned by `yield`-functions?
```python
some_list = [1, 2, 3, 4, 5]
list_generator = (n * 2 for n in some_list)     # compare: [n * 2 for n in some_list]
```

**21.14.** Recall that the keyword `return` can be used with and without a value-to-be-returned; without a value, the function simply finishes (strictly speaking returning `None`, but that is more a technicality). Can `yield` similarly be used without a value? What behavior would you expect of such a function, e.g., when you call `next` on the returned generator? Test your expectation.

**21.15.** The verb 'to yield' could mean to give/produce something, but it can also mean _to give way_, allowing other code to be executed first. Python's `yield` keyword is arguably mainly the latter (the yielded value being optional): it interrupts execution of the function's body, 'yielding' to the rest of the program, until it is asked to proceed (`next`). This is especially clear if you use several yields without a value, and print statements in between. To illustrate, call the following function to obtain a generator, and then call `next` on the generator repeatedly.
```python
def print_with_yields_in_between():
    print('Hello.')
    yield
    print('I am very polite.')
    yield
    print('I will yield until I am allowed to continue.')
    yield 
    print('See?')
```

**21.16.** In a function with multiple yields, are the variables that get defined before a `yield` statement still available after that `yield` statement?

**21.17.** Can a function contain both `yield` and `return`? If so, can you figure out what happens with the generator when the `return` statement is reached? What happens if with any returned value? Can you predict what happens if a `yield` appears after a `return`?

**21.18.** Remember that many keywords, operators and built-in functions are shorthands for methods that live on objects? For instance, the operator `+` is shorthand for the `__add__` method implemented by (among others) int, float, str and list objects. Calling the built-in function `next` on an object is shorthand for a `__next__` method -- hence it only works on objects that have such a method. Verify that generator objects have a `__next__` method, and check whether calling it behaves the same as calling `next` on the generator.

- - - - - -
**Something to keep in mind:** Objects that implement a `__next__` method, hence on which `next` can be called, are called _iterators_. Generators are a type of iterator.
- - - - -

**21.19.** Since we can loop over lists, strings, etc., would you expect them to be iterators? Test this with code.

**21.20.** Lists, strings, etc., are not themselves iterators, but they can be iterated over: they are _iterable_. An object is _iterable_ if it implements the `__iter__` method. Verify that lists and strings have such a method, and call it; what type of object does this method return? Is the built-in function `iter` shorthand for `__iter__`, just like `next` is for `__next__`?

**21.21.** ⭐ What happens if you define a list, obtain an iterator over that list (i.e., call `iter` on it), do `next` a couple of times, and then append some new value to the original list? Will the iterator go only as far as the original list, or will it also yield the newly appended value? (Start with a new iterator:) What happens if you delete an element from the list which the iterator had not yet reached? What if you delete an element that the iterator has already reached?

**21.22.** ⭐⭐ As it turns out, `for`-loops are also a kind of shorthand, namely for the following two-step process:
1. First call `iter` (hence `__iter__`) on the object being looped over (e.g., a list, range, dictionary, to obtain an _iterator_ for the object;
2. Then repeatedly call `next` (i.e., `__next__`) on the obtained iterator, each time assigning the value to the variable from the header of the `for`-clause (`for <variable> in <iterable>: ...`) and then executing the body of the `for`-clause, until elements run out (the exception that you would normally get by continuing to call `next` after elements run out, is _caught_ by the for-loop, so it does not show up and the for-loop simply exits gracefully).

Use the foregoing to emulate a for-loop _without_ using the keyword `for`, by combining explicit `iter` and `next` with a `while` loop. It is fine if your loop exits with a StopIteration exception (when the iterator's elements run out), but for an extra challenge you can also try to use the keywords `try` and `except` combined with `break` (check the documentation if needed) to handle this exception silently and exit the loop more gracefully.


**21.23.** _[Optional, feel free to skip]_ Every iterator is also itself _iterable_: you can call `iter` on something that is already an iterator, to obtain _another_ iterator, i.e., an iterator _over the iterator_. This is potentially confusing and not super useful, but to deepen your understanding, consider exploring what happens if you do this. How do the multiple iterators relate? If you call `next` on one, does the other also proceed to the next element? And vice versa?


**21.24.** ⭐ A program can be '(in)efficient' in different respects. An important distinction is between **time efficiency** (i.e., the program runs fast) and **space efficiency** (i.e., the program doesn't use a lot of your computer's memory during execution). Below are two minimally different implementations of the same function, but version A is space-inefficient while version B is space-efficient. How come?

```python
def sum_of_squares_A(upper_bound):
    squares = [n**2 for n in range(upper_bound)]
    sum_of_squares = sum(squares)
    return sum_of_squares 

def sum_of_squares_B(upper_bound):
    squares = (n**2 for n in range(upper_bound))
    sum_of_squares = sum(squares)
    return sum_of_squares

print('Result of version A:', sum_of_squares_A(9999))
print('Result of version B:', sum_of_squares_B(9999))
```

**21.25.** Perhaps you know how to inspect memory usage with a tool in your operating system (e.g., 'system monitor' or 'resource monitor'). But you can also do it within Python itself, e.g., in Section 14 we did `import sys` and used `sys.getsizeof` to obtain the memory size of a particular object. Use this to compare the size of `squares` in versions A and B in the above example.

**21.26.** ⭐ We have seen before that we can read a file in different ways. Which of the following functions, for collecting all words containing the vowel group 'ea', is more space-efficient? (You can verify your understanding using `tracemalloc` if you want, if you happen to have a sufficiently large text file lying around.)
```python
# Version A
def find_ea_words_A(path):
    with open(path) as file:
        text = file.read()
        words_containing_ea = []
        for word in text.split():
            if 'ea' in word:
                words_containing_ea.append(word)
    return words_containing_ea

# Version B
def find_ea_words_B(path):
    with open('some_big_file.txt') as file:
        words_containing_ea = []
        for line in file:
            for word in line.split():
                if 'ea' in word:
                    words_containing_ea.append(word)
    return words_containing_ea

find_ea_words_A('some_big_file.txt')
find_ea_words_B('some_big_file.txt')
```

**21.27.** Is the `file` object in the above code an iterator, or is it only an iterable? Can you verify this by calling `type` on it, or is there a better way (this relates to Python's 'duck typing')?

**21.28.** ⭐ Although in the above code one version is more space-efficient than the other, both functions end up collecting all 'ea'-containing words in a list. And that list, too, can (hypothetically) grow too big to fit in memory. Can you implement a 'version C' of the function which returns a generator of 'ea'-words instead of creating and returning a list?  



