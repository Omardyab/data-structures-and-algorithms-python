# Hashtables
<!-- Short summary or background information -->
hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.
## Challenge
<!-- Description of the challenge -->
Create a hashtable with the following methods:

    add
    get
    contains
    hash
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time: O(1) space:O(n)
## API
<!-- Description of each method publicly available in each of your hashtable -->
add: which takes: key and value. Hash the key, and add the key and value pair to the table.
get: takes in the key and returns the value from the table.
contains: that takes in the key and check if the key exists  or not.
hash: takes an arbitrary key and returns an index.
