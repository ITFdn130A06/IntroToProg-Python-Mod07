# IntroToProg-Python-Mod07
Name: Vikram Tirumalai
Date: 11/30/2022
Course: IT Fdn 110


Assignment 7 - Pickling and Errors

URLs that I feel are good for explaining pickling:
https://www.geeksforgeeks.org/understanding-python-pickling-example/
I really liked this example because it contained coding terminology that has already been covered in our course and also presented a logical example that one might enjoy doing for an assignment like this one through entering student data in a dictionary.
https://www.youtube.com/watch?v=2Tw39kZIbhs
I struggled with understanding the benefits of serialization until I watched this video. The creator explained the purpose of pickling as a more time-efficient way of storing an object to avoid delays in processing.
URLs that I feel are good for explaining exception handling:
https://www.youtube.com/watch?v=nlCKrKGHSSk
Exception handling isn’t one of the more glamorous or fun topics that we’ve covered so far, but the creator of this video put lots of effort and it made my knowledge of exception handling far greater. For example, I learned what key errors are finally in simple terms (looking up values in a dictionary that are out of range). I get this error all the time at work and I never fully understood it. 
https://runestone.academy/ns/books/published/thinkcspy/Exceptions/01_intro_exceptions.html
I thought this page was very informative and it explained the difference between using “catch-all” types of error handling and why you might opt to not do that instead. I was confused from Professor Root’s module notes on that matter but this site cleared up my confusion. This site also taught me the term “flow-of-control” which I’m intrigued to learn more about now because in SQL (which I primarily use at work) we have a similar type of code logic that determines how we write our queries. 
Introduction:

	This assignment overall was very enjoyable for me. I struggled a lot with the two most recent assignments that we had in class so I used this free-flowing assignment to review and mesh all the previous concepts we had learned (functions, classes, parameters, etc.) together into one mini-project. My project is about the world cup, the user has the opportunity to enter who they think will be the top scorers in the world cup and predict how many goals they will score. The intention is for the user to check back on 12/18 after the world cup has ended and see if their predictions came true. 
	I utilized pickling to read data from a binary file (old predictions) and to also store new predictions in that file. My error handling was also found throughout each output-menu option provided to the user. I made use of Professor Root’s module document sections on try/except and error handling. Initially, try and except didn’t make much sense to me but now I understand that by using try and except, you can figure out exactly where code stopped working. Today at work because I used debugging and my try/except statements, I was able to solve an issue and figure out exactly where one of our reporting processes stopped. 
Body:
Documentation of steps:
	I found great joy in coming up with custom errors. I thought this was a really innovative way to learn how to think like a programmer. Making your code user-friendly and also user-proof is a valuable saying I took from a reading I did on this topic. One error handling concept I implemented is shown below in Figure 1.1: 

				Figure 1.1: Custom Error
	This error was related to the input_menu_choice function, where a user is expected to enter the number on the menu that corresponds to the action they want to perform. I made this part of the function so that users had to enter a number. I also made sure throughout my code to provide detailed error handling by using the code shown in Figure 1.2:

				Figure 1.2: common appendage to my try/except statements
	Another example of error handling that I implemented was found in the input of player information. I made my data so that goals could be entered in float form (half a goal counting as an assist, so decimals were necessary). I also made sure that all goals scored values were positive and player’s names could only have alphabet characters. Figure 1.3 illustrates these specific error handling concepts.

				Figure 1.3: Specific error handling in my code

This was my final output: 


Conclusion and Summary:
	This assignment was extremely enjoyable for me and served as a nice catch-up to material I didn’t previously understand. I look forward to pursuing the next assignment and also learning more about error handling in Python. 


Citations:
https://www.tutorialspoint.com/python-pickling - links to an external site
https://www.w3schools.com/python/gloss_python_error_handling.asp - links to an external site
