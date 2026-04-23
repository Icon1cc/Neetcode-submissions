# NeetCode 250 — Solutions & Notes

> My worked solutions to the [NeetCode 250](https://neetcode.io/practice) problem set, synced from [NeetCode.io](https://neetcode.io). Each entry below walks through **what the problem is asking**, **the idea behind the solution**, and **why it's correct / efficient**. Click any problem title to jump to the code.

Currently working through: **Arrays & Hashing**.

---

## Table of Contents

- [Arrays & Hashing](#arrays--hashing)
  - [1. Concatenation of Array](#1-concatenation-of-array)
  - [2. Contains Duplicate](#2-contains-duplicate)
  - [3. Valid Anagram](#3-valid-anagram)
  - [4. Two Sum](#4-two-sum)
  - [5. Longest Common Prefix](#5-longest-common-prefix)
  - [6. Group Anagrams](#6-group-anagrams)
  - [7. Remove Element](#7-remove-element)
  - [8. Majority Element](#8-majority-element)
  - [9. Design HashSet](#9-design-hashset)
  - [10. Design HashMap](#10-design-hashmap)

---

## Arrays & Hashing

Arrays store elements contiguously in memory — indexing is O(1) but searching for a value is O(n). Hash-based structures (sets, maps) trade that linear scan for O(1) average-case lookup by mapping a key to a bucket via a hash function. The recurring trick in this topic is **"turn a search into a lookup"**: replace a nested loop with a single pass that consults a hash table built during the same pass.

---

### 1. Concatenation of Array

> **Code:** [`concatenation-of-array/submission-0.py`](./Data%20Structures%20%26%20Algorithms/concatenation-of-array/submission-0.py)

**Problem.** Given an array `nums`, return `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]`.

**Idea.** The output is literally `nums` followed by `nums`. Python's `+` on lists produces a new list that is the concatenation, matching the required shape in a single expression.

**Complexity.** Time **O(n)** for the copy, space **O(n)** for the returned list.

**Takeaway.** This is the warm-up problem of the topic — it exists to make sure you're comfortable with building a new array rather than mutating input.

---

### 2. Contains Duplicate

> **Code:** [`duplicate-integer/submission-0.py`](./Data%20Structures%20%26%20Algorithms/duplicate-integer/submission-0.py)

**Problem.** Return `True` if any value appears at least twice in `nums`.

**Idea.** Walk the array once, keeping a `set` of values seen so far. On each element, check membership in O(1); if it's already there you've found a duplicate and can return immediately, otherwise add it. The set is the classic "turn search into lookup" tool.

**Complexity.** Time **O(n)**, space **O(n)** for the set.

**Why not sort?** Sorting and scanning for adjacent equals also works and uses O(1) extra space, but it's O(n log n) — strictly worse on time unless memory is tight.

---

### 3. Valid Anagram

> **Code:** [`is-anagram/submission-0.py`](./Data%20Structures%20%26%20Algorithms/is-anagram/submission-0.py)

**Problem.** Given two strings `s` and `t`, return whether `t` is an anagram of `s` (same multiset of characters).

**Idea.** Two strings are anagrams iff every character appears the same number of times in each. Instead of maintaining two separate count tables and comparing them, this solution uses a single dictionary: **increment** for each char in `s`, **decrement** for each char in `t`. If they're anagrams every count cancels to zero. A length check up front rejects the obvious mismatches in O(1).

**Complexity.** Time **O(n)**, space **O(k)** where `k` is the alphabet size (at most 26 for lowercase English).

**Alternate forms.** `sorted(s) == sorted(t)` is a one-liner but runs in O(n log n). `Counter(s) == Counter(t)` is idiomatic Python with the same big-O as the hand-rolled version.

---

### 4. Two Sum

> **Code:** [`two-integer-sum/submission-0.py`](./Data%20Structures%20%26%20Algorithms/two-integer-sum/submission-0.py)

**Problem.** Given `nums` and a `target`, return indices of the two numbers that add to `target`.

**Idea.** The brute-force pair check is O(n²). The trick: as you scan, for each number `n` the question "is there a partner?" becomes "have I already seen `target - n`?" — a hash lookup. Maintain `seen: value → index`, and for each element check whether `target - n` is in the map **before** inserting the current element (so the same index can't be used twice).

**Complexity.** Time **O(n)**, space **O(n)**.

**Why one pass works.** The partner must come earlier in the array by the time we find the match, so any valid pair is discovered exactly once — when the *second* of the two elements is visited.

---

### 5. Longest Common Prefix

> **Code:** [`longest-common-prefix/submission-0.py`](./Data%20Structures%20%26%20Algorithms/longest-common-prefix/submission-0.py)

**Problem.** Return the longest string that is a prefix of every string in `strs`.

**Idea.** Seed `prefix` with the first string — the answer can't be longer than this. For every other string, shrink `prefix` from the right (`prefix[:-1]`) until it is a prefix of the current string. If it ever becomes empty, no common prefix exists. This is **horizontal scanning**: reduce against one string at a time.

**Complexity.** Time **O(S)** where `S` is the total number of characters across all strings (each character is examined at most once during shrinking), space **O(1)** beyond the output.

**Alternate approach.** Vertical scanning — compare the i-th character across all strings at once, stopping at the first mismatch. Same big-O, different constants.

---

### 6. Group Anagrams

> **Code:** [`anagram-groups/submission-0.py`](./Data%20Structures%20%26%20Algorithms/anagram-groups/submission-0.py)

**Problem.** Group the input strings so that anagrams live together.

**Idea.** Every anagram set shares a **canonical signature**. Any function that maps all anagrams of a word to the same key and different words to different keys will work. This solution uses a **26-length character-count tuple** as the key — tuples are hashable, and building one is O(length of the word). Strings then bucket into a `defaultdict(list)` keyed by that signature.

**Complexity.** Time **O(n · k)** where `n` is the number of strings and `k` their max length, space **O(n · k)** for the buckets.

**Why not `sorted(word)`?** `"".join(sorted(word))` also works and is O(k log k) per word — fine for short strings but asymptotically slower. The count-tuple keeps it linear in the word length.

---

### 7. Remove Element

> **Code:** [`remove-element/submission-0.py`](./Data%20Structures%20%26%20Algorithms/remove-element/submission-0.py)

**Problem.** In-place, remove every occurrence of `val` from `nums` and return the new length `k`. The first `k` entries must be the surviving values (any order).

**Idea.** Classic **two-pointer / slow-fast pattern**. A single write pointer `first` tracks where the next kept value should go; the read pointer walks the array. When we hit a value that should survive, we copy it to `nums[first]` and advance `first`. Values equal to `val` are simply skipped — they get overwritten later (or are past the returned length, so they don't matter).

**Complexity.** Time **O(n)**, space **O(1)** — the whole point is no extra buffer.

**Key invariant.** After processing index `i`, `nums[0..first)` contains exactly the surviving values seen so far, in original order.

---

### 8. Majority Element

> **Code (hash map):** [`majority-element/submission-1.py`](./Data%20Structures%20%26%20Algorithms/majority-element/submission-1.py)
> **Code (Boyer–Moore):** [`majority-element/submission-2.py`](./Data%20Structures%20%26%20Algorithms/majority-element/submission-2.py)

**Problem.** An element appears more than `⌊n/2⌋` times — return it. It's guaranteed to exist.

**Approach 1 — Counting (`submission-1`).** Build a frequency dictionary, then return the key with the maximum count via `max(count, key=count.get)`. Straightforward, but uses O(n) extra memory.

**Approach 2 — Boyer–Moore Voting (`submission-2`).** Keep a `candidate` and a `count`. Scan left-to-right: when `count == 0`, adopt the current element as the new candidate. Then increment `count` if the current element matches, decrement otherwise.

The intuition: pair off each majority occurrence with a non-majority one — they cancel. Because the true majority has strictly more than `n/2` occurrences, at least one of it is left standing, and that's whoever `candidate` is at the end.

**Complexity.** Boyer–Moore runs in **O(n)** time and **O(1)** space — optimal on both axes. The hash-map version is O(n)/O(n).

---

### 9. Design HashSet

> **Code:** [`design-hashset/submission-0.py`](./Data%20Structures%20%26%20Algorithms/design-hashset/submission-0.py)

**Problem.** Implement `add`, `remove`, `contains` for a set of integers without using the language's built-in hash set.

**Idea.** A hash set is an **array of buckets** plus a **hash function** that maps a key to a bucket index. Collisions — different keys hashing to the same bucket — are resolved with **separate chaining**: each bucket is itself a list, and we do a linear scan within the bucket for add/remove/contains.

This implementation uses `size = 1000` buckets and `key % size` as the hash. That's fine for correctness; real-world hash tables choose a prime size and resize (rehash) once the load factor gets high, to keep bucket lists short.

**Complexity.** Average **O(1)** for all three ops assuming a good hash and bounded load factor; worst case **O(n)** if every key lands in the same bucket.

---

### 10. Design HashMap

> **Code:** [`design-hashmap/submission-0.py`](./Data%20Structures%20%26%20Algorithms/design-hashmap/submission-0.py)

**Problem.** Same exercise as Design HashSet, but each key stores an associated value. Implement `put`, `get`, `remove`.

**Idea.** Identical bucket-array + separate-chaining skeleton, but each bucket stores `[key, value]` pairs instead of raw keys. `put` must handle the **update case**: if the key is already present in its bucket, overwrite the value instead of appending a duplicate pair. `get` returns `-1` on miss by contract.

**Complexity.** Average **O(1)** per op, worst case **O(n)** — same reasoning as the hash set.

**What's missing vs. a production map.** No dynamic resizing (load factor grows unbounded as entries accumulate), a trivially weak hash (`% 1000` is vulnerable to adversarial keys that all land in one bucket), and no iteration order guarantees. Plenty of room for follow-up submissions.

---

## Repository layout

Solutions are auto-synced from NeetCode.io. File paths follow:

```
Data Structures & Algorithms/<problem-id>/submission-<N>.py
```

`submission-0` is the first accepted attempt; higher indices are later iterations (often a better approach, like the Boyer–Moore variant of Majority Element above).
