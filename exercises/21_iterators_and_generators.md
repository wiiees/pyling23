# Python for Linguists 2023

## 21. Iterators and generators

Effort profile: `(▁▁▁)` 

**TODO:** Make this section.



----

🦉 **_This entire section is OPTIONAL!_**

----

**21.1.** Generator expressions and yield:  https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do   including this fun example -- ACTUALLY that example fits way sooner, e.g., in loop control flow, but do add a reminder here that processing files is a prime example where yield can be helpful. Maybe also `next`. Maybe also `yield` with no argument? `print`, `yield`, `print`, `yield`, etc.

```python
def f123():
    yield 1
    yield 2
    yield 3
    
for item in f123():
    print(item)
```



**21.2.** Thus far we learned how `break` lets you escape from a loop early, which can benefit time-efficiency. In this Coding Quest you learn how to change your loops for greater space-efficiency.

**21.3.** A program can be more or less 'efficient' in different respects. An important distinction is between time-efficiency (i.e., the program runs fast) and memory-efficiency (i.e., the program doesn't use a lot of working memory during execution). 


