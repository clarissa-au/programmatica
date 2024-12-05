# Day 4 - Ceres Search

(This writeup will be posted to my blog later on when I have time, after I transition my blog's structure.)

![Oh, frick me.](/blob/adventOfCode/2024/day4_iamfucked.jpg)
> Oh, frick me. I haven't coded in Kotlin before. I definitely haven't played Russian Roulette with language choice with some of my friends also playing Advent Of Code 2024.

## Problem Statement

We have a grid of characters, and we want to find occurences of specific patterns within the grid.

## Analysis

This is awfully similar to a [previous AoC question](/advent_of_code/2023/code/day3.py) last year, where we have to find... something? I cannot decipher what I had to find without looking back at the question. (The question is linked [here](https://adventofcode.com/2023/day/3))

I am pretty sure I didn't use padding last year, being the first time I have to deal with these sorts of questions, but having did last year's Day 3, I feel like not using padding here would make my life hell by coding various kinds of exits. There may be a use for the non-padded version of solution in a real environment, but here in AoC as the input data is relatively small (140x140 square) padding it is the most easy way to deal with the issue.

## Part 1

The structure we have to find looks something like this.

    X
    M
    A
    S

It could be rotated in 45 angles increment, (i.e. SAMX is a legal target to be searched for.)

To begin this part, the important clue is that all XMAS structure start with a X. (You can start with a S, that also works, but starting with a X is more intuitive). Therefore, any non-X characters need not to be considered as a beginning to a XMAS structure.

The issue with this, tho; is this (and is why padding is necessary) -

    XAMA...
    AMAS...
    XMAS...
    MASX...
    ....
    ....
    ....

When we consider the X at grid position (0,0); when we fit the star-shaped check on it in Kotlin it will cause a error of out of bounds (in Python, it will wrap itself around and cause false positives). There are two solutions to this, one is adding a padding and one is using a custom gridQuery as shown in the following:

    def gridQuery(ary, x, y):
        if x < 0 or y < 0:
            return "_"
        try:
            return ary[x][y]
        except:
            return "_"

Depending on grid size, adding padding may be infeasible or is code-time-expensive, as I am coding this solution in Kotlin.

    val ary = data.split("\n").toTypedArray()

    // part 1
    // part 1a preparing the data
    val size = ary.size + 6
    val charAryIntermediate = Array<String>(size) {"_"}
    for (i in 0..2){
        charAryIntermediate[i] = ".".repeat(ary[0].length + 6)
    }
    for (i in 0..<ary.size){
        charAryIntermediate[i+3] = "..." + ary[i] + "..."
    }
    for (i in ary.size+3..ary.size+5){
        charAryIntermediate[i] = ".".repeat(ary[0].length + 6)
    }
    val charAry = Array(size) { Array<String>(size) {"_"} }
    for (i in 0..<charAryIntermediate.size){
        var chunked = charAryIntermediate[i].chunked(1)
        for (j in 0..<chunked.size){
            charAry[i][j] = chunked[j]
        }
    }

This section inserts the padding, and splits them into an array of an array of a character.

    // part 1b iterate thru the data and check for possibilities
    var answerP1 = 0
    for (i in 0..<charAry.size){
        for (j in 0..<charAry.size){
            if (charAry[i][j] == "X"){
                if(charAry[i-1][j] == "M" && charAry[i-2][j] == "A" && charAry[i-3][j] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i-1][j-1] == "M" && charAry[i-2][j-2] == "A" && charAry[i-3][j-3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i][j-1] == "M" && charAry[i][j-2] == "A" && charAry[i][j-3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i+1][j-1] == "M" && charAry[i+2][j-2] == "A" && charAry[i+3][j-3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i+1][j] == "M" && charAry[i+2][j] == "A" && charAry[i+3][j] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i+1][j+1] == "M" && charAry[i+2][j+2] == "A" && charAry[i+3][j+3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i][j+1] == "M" && charAry[i][j+2] == "A" && charAry[i][j+3] == "S"){answerP1 = answerP1 + 1}
                if(charAry[i-1][j+1] == "M" && charAry[i-2][j+2] == "A" && charAry[i-3][j+3] == "S"){answerP1 = answerP1 + 1}
            }
        }
    }
    println("Part 1 answer: $answerP1")

This implements the star-shaped search pattern.

There could be a way where we don't use 8 if statements and multiply a direction against a vector in the following and could be more readable:

    for vertical in [-1, 0, 1]:
        for horizontal in [-1, 0, 1]:
            if charAry[i+vertical*1][j+horizontal*1] == "M" && charAry[i+vertical*2][j+horizontal*2] == "A" ...

Thus, the first star in the progress in finding the Historian!

## Part 2

> Uh-huh, turns out that we are here to find X-MAS, not XMAS!

![is this a X?](/blob/adventOfCode/2024/day4_isthisaX.png)
> me: is this a X?

The structure we are going to find looks something like this.

    M S
     A
    M S

S and M can be in opposite order as long as the whole structure looks like a X (not a +) and both slashes contains MAS (i.e. the same letter is not in opposite corners).

Additional padding is not needed, since the beginning point of the structure (being the A) is within 1 character distance of all the other letters, and we gave 3 letters of padding for the structure in Part 1.

With some discussions with my friends, it is also possible to note that we do not actually need to pad this at all, since even if A is at the corner of the array it couldn't have been a valid A to begin a X-MAS structure with because there is no character outside the array at all!

    // part 2 note that every cross mas has to begin with a A
    // iterate and possibilities
    var answerP2 = 0
    for (i in 0..<charAry.size){
        for (j in 0..<charAry.size){
            if (charAry[i][j] == "A"){
                var forwardSlash = charAry[i-1][j-1] + charAry[i+1][j+1]
                var backwardSlash = charAry[i-1][j+1] + charAry[i+1][j-1]
                if (
                    (forwardSlash == "SM" || forwardSlash == "MS") &&
                    (backwardSlash == "SM" || backwardSlash == "MS")
                ){answerP2 = answerP2 + 1}
            }
        }
    }
    println("Part 2 answer: $answerP2")

This implements the search for both the forward slash and the backwards slash of the X structure, and as there is only 2 character the only possible method to put it is either MS or SM.

Thus, the second star in the progress in finding the Historian!
