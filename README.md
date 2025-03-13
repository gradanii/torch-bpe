# Byte-Pair Encoding (BPE)
__Byte-Pair Encoding__ is an algorithm for encoding strings of text into smaller strings by creating and using a translation table.

The original version of the algorithm focused on compression. It replaces the highest-frequency pair of bytes with a new byte that was not contained in the initial dataset. A lookup table of the replacements is required to rebuild the initial dataset.

The modified version builds "tokens" (units of recognition) that match varying amounts of source text, from single characters (including single digits or single punctuation marks) to whole words (even long compound words).

## Original Algorithm
The original algorithm was based on how frequently certain word pairs occur.

Let's say we have this string of letters:

```
aaabcaaabac
```
The byte-pair 'aa' occurs most often, so we replace every occurence of that pair with another byte 'X' that is not already in the data.
```
XabcXabac
X = aa
``` 
The next pair of bytes which occurs more than once is 'ab', we replace it with another byte 'Y' which isn't in the data.
```
XYcXYac
X = aa
Y = ab
```
Since now, we see that the pair 'XY' also occurs more than once, we replace it with anotehr byte 'Z'. This is called recursive encoding.
```
ZcZac
X = aa
Y = ab
Z = XY
```