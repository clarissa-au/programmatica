# Day 5 - Print Queue

(This writeup will be posted to my blog later on when I have time, after I transition my blog's structure.)

## Today's Visualization

![The Ouroboros](/advent_of_code/2024/visualization/day5_ouroboros.png)
> What actually does the dependency graph looks like? A Ouroboros.

## Problem Statement

We got a dependency table, and we have to check if the papers are following the dependency table, and sort using the dependency table.

## Analysis

There is a nice article about some discrete math and graph theories used in this question linked [here from Reddit by FCBStar-of-the-South](https://www.reddit.com/r/adventofcode/comments/1h7mm3w/2024_day_05_part_2_how_nice_is_the_input_a_binary/). That goes into much more deeper graph theory territories than my small writeup of how I have done the solution.

[This video by TED](https://www.youtube.com/watch?v=5y0pcLkD7-I&list=PLJicmE8fK0EiFngx7wBddZDzxogj-shyW&index=9) also goes into a similar question, but the question it presents is a directed acyclic graph and not a directed cyclic dependency as we know it.

## Idea behind Visualization

I know that the input is a cyclic one from what can be gleaned from the AoC subreddit, and I want to showcase the circularity of the dependencies. The dependencies are clockwise. (i.e. 19 depends on 66 before it, 66 depends on 57 before it)

## Part 1

We are asked to verify a set of book if they fit the dependencies as introduced in the top.

    66|19

This can be seen as a dependency on 19, where it has to have 66 before it if 66 exists at all.

Therefore, we can group the dependencies, and if a dependent page comes *after* the page that depends on it, we flag it as a error. (and in fact, we don't need to check if the depended page is itself present, we just need to check if it does not come afterwards)

Checking the dependencies gives us a Star in the search for the Historian!

## Part 2

We are asked to reorder the pages so that they match the dependency table. I was exhausted at that time, so I just sorta bodged it until I had the realization when I was playing with a previous iteration that just swaps errors once at a time in a Jupyter notebook that what I am doing essentially is writing a custom Bubble Sort!

Writing the Bubble Sort, sorting the pages out and finding the median gives us another Star in the search for the Historian.
