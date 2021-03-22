# The program: university selection

This command line program in university_finished.py helps the user choose
a university.

It first shows them a count of universities by country 
and asks them to choose a country.

Then it asks them whether they prefer a university with more 
graduate students or more undergraduates or do not care. 

Then it prompts them about which of the three scores to rank by:
teaching, international, or research. 

Finally, it prints out the filtered list, ranked in that way. 

The problem for the candidate
--------------------------------
The version university_finished.py is a finished working version. The one 
given to the candidate is university_incomplete.py. There are a few 
things missing that need to be completed. This includes two functions whose 
purposes are clear and documented but not yet implemented in the incomplete 
file. Tests exist for these two functions 
as well. 

There is also one undesirable feature / bug that the candidate 
should find and fix, time permitting.

The code runs in any Python 3 as well as Python 2.7 and does not use and 
does not need any libraries. The candidate should not use any libraries 
other than those in the builtin python standard lib.

The tests should pass and the program should appear to run correctly.

For interviewers only (Do not send this part to candidate)
------------------------------------------------------------

We are looking for the candidate to solve this problem without any 
input from the interviewer. The problem should be completely self explanatory.

If they get stuck on syntax or something, you
may suggest something just to speed them along but note this down. We are 
also looking for their familiarity with Python and it's syntax. 

The version we give them will have the university_finished.py and test.py files 
removed and should have a Readme file without this subheading. So they have just
university_incomplete.py, test_incomplete.py and university_data.csv.

They should not get this code in advance.

The interview process should be as follows. 

* Run the program on your laptop. Briefly describe what it's doing (2 min)

* Explain that they will be given an unfinished version and must finish it in 
15 minutes without using any libraries outside of the Python standard lib. 

* Send them the link to the appropriate repo. Do not tell them anything else. 
We want to see if they know what to do with git/github. If they do not seem 
to know how to download it and get started, note that down and then 
explain how to do it. If we have to hold their hand at this point, they 
are probably already failing the interview.

* Have them complete the work in the allotted time. If they need a little more time
and (more importantly) you need more time to evaluate them, they can gave an extra 
5 minutes.

Things to look for:

* Did they seem familiar with Github/git? 

* Did they manage to download it and get started quickly?

* Did they use an IDE like Pycharm?

* Are they familiar with the Python syntax or do they have to Google it?

* Did they notice the tests and, better yet, actually try to run them?

* Observe how they mentally process the code. See how long it takes for them to 
notice the two missing functions and realize they need to be implemented.

* How do they go about writing the count_countries function? It's a positive if they
are familiar with the "Counter" object from the collections library but it's not 
required.

* If they finish this function, how do they test it. Have they noticed the test 
program by now? Do they at least test it in the python shell.

* The other function sort_by_chosen_score should basically be a one-liner. 

* After writing these two functions, can they get the program to run?

* Do they notice the duplicate universities? If so, do they know how to go about
fixing it in some reasonable way? Do they actually fix it in the allotted time?




