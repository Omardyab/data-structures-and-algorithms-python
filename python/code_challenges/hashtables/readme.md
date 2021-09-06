# Hashtables
<!-- Short summary or background information -->
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

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
