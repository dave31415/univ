For interviewers only (Do not send this part to candidate)
------------------------------------------------------------

The candidate-visible version of this repo contains only 4 files

* README.md
* university_incomplete.py
* university_data.py
* test.py

These other two files are NOT given to them:
* INTERVIEWERS_ONLY.md (This file)
* university_finished.py

The candidate needs to recognize that two functions
count_countries and sort_by_chosen_score are not implemented.

We are looking for the candidate to solve this problem without any 
input from the interviewer. The problem should be completely self explanatory.
They need to view the code, understand the program structure which should
lead them to the fact that these two functions need to be implemented. They
will be easy functions to implement for anyone familiar with python 
programming especially with regard to data science use cases.

If they get stuck on syntax or something, you
may suggest something just to speed them along but note this down. We are 
also looking for their familiarity with Python and it's syntax.

The version we give them will have the university_finished.py and test.py files 
removed and should have a Readme file without this subheading. So they have just
university_incomplete.py, test.py and university_data.csv and an 
abbreviated (this section removed) version of the Readme.

They should not get this code in advance.

The interview process should be as follows. 

* Run the program on your laptop. Briefly describe what it's doing (2 min)

* Explain that they will be given an unfinished version and must finish it in 
15 minutes without using any libraries outside of the Python standard lib. 

* Send them the link to the appropriate repo and tell them to clone it.
Do not tell them anything else. We want to see if they know what to 
do with git/github. If they do not seem to know how to download it and 
get started, note that down and then explain how to do it. If we have 
to hold their hand at this point, they are probably already failing 
the interview. If they don't know what git is or don't have it installed 
that's basically a failed interview. They can also download the code via a 
tar file.

* Have them complete the work in the allotted time. If they need a little more time
and (more importantly) you need more time to evaluate them, they can gave an extra 
5 minutes. Be sure to note this as well.

Things to look for:

* Did they seem familiar with Github/git? 

* Did they manage to download it and get started quickly?

* Did they use an IDE like Pycharm?

* Are they familiar with the Python syntax or do they have to Google it?

* Did they notice the tests and, better yet, actually try to run them and see 
why that is helpful?

* Observe how they mentally process the code. See how long it takes for them to 
notice the two missing functions and realize they need to be implemented.

* How do they go about writing the count_countries function? It's a positive if they
are familiar with the "Counter" object from the collections library but it's not 
required.

* If they finish this function, how do they test it? Have they noticed the test 
program by now? Did they run it? Do they at least test it in the python shell?

* The other function sort_by_chosen_score should basically be a one-liner. 

* After writing these two functions, can they get the program to run?

* Do they notice the duplicate universities? If so, do they know how to go about
fixing it in some reasonable way? Do they actually fix it in the allotted time?

* We will expect that they complete at least one of the functions and 
therefore pass one of the two tests in 20 min max. That would be enough info
to judge their familiarity with Python programming. Someone who is a little 
better will finish both functions. Neither should take more than 5 min to write.
The count_counties function requires no more than 5 lines of code. The other
sort_by_chosen_score should be a one-liner.
