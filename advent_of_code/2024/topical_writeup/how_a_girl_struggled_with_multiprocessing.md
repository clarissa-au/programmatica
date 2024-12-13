# How a Girl struggled with Multiprocessing

> aka A Confessional of a Girl who cheated in AoC
> or How I inadvertently fell into a X/Y problem

> def("XY Problem")
> the act of asking a question with a solution in mind, not presupposing that the solution may itself be wrong. ([source](http://www.catb.org/~esr/faqs/smart-questions.html#goal))

## TLDR

When I was working for a solution to Day 6 of Advent of Code, my code took 8 minutes to run, and returns a wrong answer. Thinking that making the solution faster would make it easier to debug, I tried to use multiprocessing and in the process of trying to use multiprocessing to speed up my code I found out that using nonoptimized code for multiprocessing itself won't make anything better, only giving a marginal improvement on runtime despite on a med-high end computer. At the end, I copied a solution from the Solutions Megathread and used it to compare stepwise to what I have done, and after 20 minutes of computation (due to being on battery probably) I computed the answer for my solution.

## Visualization

![map](/advent_of_code/2024/visualization/day_6.png)

![pikachu_shocked_face](/blob/adventOfCode/2024/shocked_pikachu.png)

> pikachu_shocked_face.png

> X represents the path taken,
> M represents misidentified loop locations,
> U represents unidentified loop locations.

## 9th December

0100 Local: I have just solved and did the writeup for Day 5, and after a night of sleep I am intending to get the solutions for Day 6 - 8.

0300 Local: I have solved Day 6a, but I am having troublem with 6b - whatever I do, I cannot get 6b to work! I asked on reddit how to solve 6b, and got back some testcases to work with.

0500 Local: While waiting for replies to my question, I solved D7 and D8 - and tried to use multiprocessing on Day 7. As I found out that my multiprocessing solution does not actually run faster than my nonmultiprocessing solution, I again turned to reddit for help - to identify where is the pain points of multiprocessing in a futile attempt to try quicken my Day 6 solution. Being absurdly tired does not help with my quest to solve D6b, and I set a alarm for 0845 for work.

Here is a few assumptions I used for day 6b:

1) loop locations can only happen on the path
2) if a position key has been encountered before on a trial run, it is considered to be a loop.

## 9th December, post shift

1400 Local: I was extremely tired, and with a nearly stopped brain I decided that I could only debug it by comparing to a solved solution and using it to see where I did wrong. I'm not sure if it is cheating, but hey, even if I cheated I would learn what I did wrong? 

1410 Local while on shift: Color me pikachu shocked when I see unidentified loop locations on positions that isn't even on the path, as shown in the visualization grid.

1430 Local while on shift: Color me double pikachu shocked when I correct for the grid positioning by using `mapping[(j, i)] = data[i][j]` instead of `mapping[(i, j)] = data[i][j]` and saw this when comparing my grid to a correct solution. Using this, I resolved the unidentified loop positions, but there is still a lot of missing loop positions with no apparant cause.

![why](/blob/adventOfCode/2024/day6_whyistheretwofootstops.jpg)
> There are two fricking footstops? Why does Python think the left footstop isn't the right footstop?

1730 Local: After throwing out using a dict to represent the mapping and only using a list that stores the wall location and the simulation position and direction I cut the runtime from 8mn to 2mn - my earlier multiprocessing attempt is not even a correct solution to make my attempt go quicker!

## 11th December

After taking a day of rest due to examination, I essentially followed the steps of the correct solution in 2nd rewriting of the solution and got a correct solution.

## Further Thinking

1) How can multiprocessing be used in AoC effectively? While researching on multiprocessing, they have big performance overheads that limits their own usefulness. I would like to investigate further on how multiprocessing can be employed effectively.
2) In the correct solution, they scans for every point in the grid space compared to only on the path. Logically, searching more points would not decrease the amount of points determined for a set. However, a interesting finding I saw later on is that misidentified points are all points that are crossed in both directions. There might be a off-by-one error somewhere in the original solution that looping for all points would fix somehow.
3) Does being exhausted actually affect how a person codes? If I wasn't coding at 3 am for the solution and in a better headspace, would the underlying bug not be coded in at the first place?
4) How does the solution gets part A right but not part B? I didn't encounter such a heavy resistance on D6a, only on D6b.