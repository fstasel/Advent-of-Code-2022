I did not add a period calculator code. By the observation of dellist variable and after some trials, I realized that we have a flat ground in a period. So, I just wrote the codes to work on that case.

In order to make it work on every dataset, we need to change "diff == 0" to "diff > SOME LARGE NUMBER" and try to observe the repetition in dellist. Then "if len(dellist) == 2:" and subsequent part must be changed to calculate the number of rocks fallen and the increase in the rock height in a period.
