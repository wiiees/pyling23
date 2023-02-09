# Python for Linguists 2023

## Coding Quest D: Trees

**_Finish [Section 12](../exercises/12_more_lists_and_loops.md) before attempting this quest._**


**D.1.** Conceptually (no programming required), can you think of a way to represent a syntactic constituency tree with the help of lists? Try to unambiguously represent, for instance, the constituency tree for "the student walks", with the help of (nested) lists. (Try not to peek at the next exercise.)

**D.2.** A tree is a so-called directed, acyclic graph (DAG): a collection of nodes that are connected by an asymmetric (= directed) relation (like 'is child of'), such that following this relation from node to node will never bring you back to where you started (= acyclic). We can represent each node as a list with two elements: the first a string representing the 'label' of the node (e.g., DP, VP), the second a (potentially empty) list containing its children. Such a tree can be defined all at once, or step-by-step as shown below, assigning subtrees to auxiliary variables first. Do you think that printing the variable `s` will print the entire tree? Try to predict what it might look like, before trying it out.

<details><summary>Only reveal this once you have answered exercise D.1!</summary>

```python
the = ['the', []]       # leave nodes have an empty list of children
det = ['Det', [the]]
student = ['student', []]
n = ['N', [student]]
walks = ['walks', []]
v = ['V', [walks]]
dp = ['DP', [det, n]]
vp = ['VP', [v]]
s = ['S', [dp, vp]]
```
</details  >

**D.3.** ⭐⭐ To familiarize yourself with this representation, define a couple of syntactic trees for other sentences. For some variation, at least try one with a transitive verb and a direct object, as well as a sentence with an adverb and/or adjective. (Feel free to choose a specific theory of syntax of course, or improvise a bit.)

**D.4.** ⭐ A computational linguist tried to define a function to print syntactic trees, with each node on a new line, but there is a bug; it doesn't quite work. Can you fix this code? Note that it is a _recursive_ function.

```python
def pretty_print_tree(node):
    print(node[0])
    for child in node:
        pretty_print_tree(child)
```

**D.5.** ⭐⭐ Improve the function `pretty_print_tree` to print each node's label with indentation (i.e., prefixed by spaces) corresponding to its depth in the tree. For this, the function will need a second argument to keep track of the 'current depth'. The output should look something like:

```python
S
  DP
    Det
      the
    N
      student
  VP
    V
      walks
```

**D.6.** ⭐⭐ Define a function that takes a node as input, and prints all _leaf_ nodes concatenated (with spaces in between) on a single line, i.e., the plain sentence.