# Word Search Generator and Solver

Two Python console apps: one for generating word searches
from user parameters, one for solving user entered word search puzzles

## Generator
gen_word_search.py takes a grid width, grid height, and list
of words to include from the user. A simple insertion algorithm
is followed for each word:

1) generate a random row, column, and orientation
2) attempt to insert the current word into the word grid
starting at the generated row and column, extending in the
generated direction
3) Repeat 100 times or until word can be inserted with no
letter conflicts

This algorithm does not guarantee that a word grid
involving all words will be generated, even if it is
possible to.

### Sample Generator Usage
```
---------- Word Search Generator ----------

Enter width of grid>> 10

Enter height of grid>> 10

Enter the words to include in this word search, one at a time. Press enter when done. Example:
cat
dog
pig
horse
<enter>

>> shall
>> i
>> compare
>> thee
>> to
>> a
>> summers
>> day

You entered the words: 
shall
i
compare
thee
to
a
summers
day
Are these the words you would like to include? (y/n)>> y

Generating word grid...

Grid:
__________
lcomparevr
udokuutohw
ganqjquzlr
jtsxmtoaal
yhnuisupda
zeyimphpad
reswcmraye
smiabbeqlu
ncjiuxmrpl
kndhgjoosn
‾‾‾‾‾‾‾‾‾‾
Words included: shall, i, compare, thee, to, a, summers, day

Would you like to generate another word search? (y/n)>> n

Goodbye...
---------- Word Search Solver ----------
```


## Solver
solve_word_search.py takes a word grid and list of words
to find from the user, and returns all words that are in
the word search. The solving algorithm is simple - for
each word, every grid position and direction is visited
until the word is found or until every orientation has been
visited.

### Sample Solver Usage
```
---------- Word Search Solver ----------

Enter the grid, row by row, and press enter when done. Example:
a b c
d e f
g h i
<enter>

>> lcomparevr
>> udokuutohw
>> ganqjquzlr
>> jtsxmtoaal
>> yhnuisupda
>> zeyimphpad
>> reswcmraye
>> smiabbeqlu
>> ncjiuxmrpl
>> kndhgjoosn

User entered grid:
__________
lcomparevr
udokuutohw
ganqjquzlr
jtsxmtoaal
yhnuisupda
zeyimphpad
reswcmraye
smiabbeqlu
ncjiuxmrpl
kndhgjoosn
‾‾‾‾‾‾‾‾‾‾
Is this the grid you would like to use? (y/n): y

Enter the words to find in this word search, one at a time. Press enter when done. Example:
cat
dog
pig
horse
<enter>

>> shall
>> i
>> compare
>> thee
>> to
>> a
>> summers
>> day

You entered the words: 
shall
i
compare
thee
to
a
summers
day
Are these the words you would like to find? (y/n)>> y

Finding words...

Words found:
shall
i
compare
thee
to
a
summers
day

Solution: 
__________
lCOMPAREvr
udokuuTOhw
ganqjquzlr
jTSxmtoaal
yHnUISupDa
zEyiMpHpAd
rEswcMrAYe
smiabbEqLu
ncjiuxmRpL
kndhgjooSn
‾‾‾‾‾‾‾‾‾‾

Would you like to solve another word search? (y/n)>> n

Goodbye...
---------- Word Search Solver ----------
```