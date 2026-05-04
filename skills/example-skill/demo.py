# demo.py — Identify Outputs Skill Demo

from logic import run

ASSIGNMENT = """\
The dictionary abstract data type is possibly the most generally useful ADT. It
allows one to store values associated with keys, and to look up these values given
the corresponding keys. As with any ADT, multiple concrete data structures
can be used to represent a dictionary. In this assignment, you will implement
two of them: an association list, and a hash table.
An association list is a data structure which uses a linked list to store key-value
pairs. Most of its operations rely on linear search, which gives them a worst-case
time complexity of O(n). Still, association lists can be a good choice when we
expect n to be small.
A hash table is a data structure that can achieve average O(1) time for lookup
and insert operations, so long as certain conditions are met. We saw two main
strategies for organizing a hash table in class: open addressing and separate
chaining. In this assignment, you will implement a separate chaining hash table.
In dictionaries.rkt I've supplied stubs for the two classes you'll need to write,
along with some frankly embarrassing excuses for tests. Your job is to fill in the
methods and write a bunch more tests, as well as to write a small piece of code
that uses your dictionaries.
Dictionaries
The starter code defines an interface, DICT, which both your association list and
your hash table will implement:
interface DICT[K, V]:
def len(self) -> nat?
def mem?(self, key: K) -> bool?
def get(self, key: K) -> V
def put(self, key: K, value: V) -> NoneC
def del(self, key: K) -> NoneC
That is, a DICT, for some key contract K, and some value contract V, provides
five methods, which should behave as follows:
- len returns the number of mappings in the dictionary.
- mem? returns whether a particular key is present in the dictionary.
- get returns the value associated with a key if the key is present, or calls
  error with a message that includes "key not found" otherwise.
- put associates a key with a value in the dictionary, replacing the key's
  previous value if already present.
- del removes a key and its associated value if the key present and has no
  effect if the key is absent.

Association list
The first kind of dictionary you must implement is an association list.
Association lists use linked lists of key-value pairs as their representation; you
will need to figure out how to represent that in your code.
You will also need to implement the five methods from the DICT interface as
well as a constructor, which does not take any arguments (aside from self) and
initializes an empty association list.
There are a few possible strategies for insertion in an association list, some of
which we discussed in class:
1. assume there won't be any duplicate keys and always insert a new key-value
   pair at the front;
2. look for the key, then only insert the new key-value pair if the key
   doesn't exist, otherwise throw an error with a message that includes
   "key not found"; or
3. look for the key, then either update the existing key-value pair with a new
   value or insert a new key-value pair.
For this assignment, you must write a general-purpose association list which does
not assume that no one will ever use duplicate keys and which allows updating
the values of existing keys. Therefore, you must use the third insertion strategy.
Hash table
The second dictionary you must implement is a separate chaining hash table.
To help you get started, the starter code provides you with definitions for the
fields you will need, as well as a partial definition for the constructor:
class HashTable[K, V] (DICT):
let _hash
let _size
let _data
def __init__(self, nbuckets: nat?, hash: FunC[AnyC, nat?]):
self._hash = hash
...
In this code, the _hash field stores the hash function, which you will use to
hash keys into natural numbers. The _size field is for storing the number of
key-value mappings in the dictionary. The _data field is intended to store your
vector of buckets. In a separate chaining hash table, each bucket is a linked list
of key-value pairs, but the exact representation is up to you. You are welcome
to add more fields and change the body constructor as you see fit, but you must
leave the constructor's signature (i.e., its parameters) as is, so that we can test
your code.

Using dictionaries
The final part of your task is to write a short piece of code that uses the
dictionaries you just wrote.
You are planning a trip abroad to a country where English is not the primary
language. Thinking ahead, you are building a short phrasebook to map various
words in the language spoken at your destination to both their English translation
and their pronounciation.
You must write the compose_phrasebook function, which accepts as its argument
a (possibly empty) dictionary representing a phrasebook. The function should
add key-value pairs to that dictionary mapping at least five words in a non-
English language of your choice to their translation and pronounciation.
This function should use only operations from the DICT interface (enforced by
the DICT! contract on its argument), which means you will be able to test it
with both kinds of dictionaries that you have implemented.
After you've written your compose_phrasebook function, write a test case that
retrieves the pronounciation (only the pronounciation!) of one of your words.
"""

WELCOME = """
============================================================
       CS 214 — Identify Outputs Skill Demo
============================================================

Assignment loaded: Dictionaries (association list + hash table)

Ask questions about what your code should output, return,
or print. I'll guide you without giving away the answer.
