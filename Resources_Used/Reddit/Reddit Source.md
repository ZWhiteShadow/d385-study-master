(UPDATED) 11/2023 Software Security and Testing D385
Disclaimer: I have never posted before, ever in my life, this is my first ever reddit post, but I felt that people need to hear the truth about this class!!


I passed my OA and felt overly prepared because I spent way too much time studying materials I found outside of WGU online. I took a lot of time in this class before I took the test because this course was intimidating! Amid dealing with work/family life balance it took me about 3 months. I crammed the last 3 weeks but I was still dreading OA. The lack of relative course material/ proper support for a coding exam that throws you in headfirst.

If I took it any sooner I would have failed the first time and I did not want that. I scheduled an appointment with my CI, they said that they had no advice and I will fail the first time. I don't think students need to fail the OA the first time to be able to pass the second time. That's not a model for success. If I only studied what WGU had and used the quizzes from chapters 2,3, and 4(Which were mostly irrelevant to anything I was tested on); I would have failed miserably.

I understand that the course instructors are responsible for multiple courses sometimes, and that there's a group of instructors. But who is the responsible party and held accountable for the lackluster experience of D385? I mean calling it lackluster is being generous.

PLEASE PLEASE PLEASE use this stuff I found that helped me!!! I hope you don't struggle like I did. This test is hard and you must be prepared!
Use this to know the http headers and status codes: https://realpython.com/python-api/

200 OK
Your request was successful!

201 Created
Your request was accepted, and the resource was created.

400 Bad Request
Your request is either wrong or missing some information.

401 Unauthorized
Your request requires some additional permissions.

404 Not Found
The requested resource doesn’t exist.

405 Method Not Allowed
The endpoint doesn’t allow for that specific HTTP method.

500 Internal Server Error
Your request wasn’t expected and probably broke something on the server side.

You need to know types of cyberattacks and how they happen! Just by looking at some scripts of code. There were 2-3 of these questions.

Credit to Cydo_Entis! Use this for mutiple choice questions: https://quizlet.com/813493586/d385-pre-assessment-all-correct-flash-cards/?new

You must know forwards and backwards all the coding, and yes I said ALLLL OOFF ITT! Its all mostly the same on the PA to the OA. Here is a link that has the right answers for the PA: https://glass-diadem-acc.notion.site/D385-Assessments-3261412dc25f4bce829d34341f33e8b3

Here is my own list because its slightly different, even some of the glass-diadem solutions reported wrong on the PA's before I took the OA. Pay attention to the variables and declarations because you will have to use different ones they give you in the code on the test. Example: instead of x, its z; Example: instead of encrypted_text its encrypted_plain_text. Watch for these things.

Logging error

logging.error('The exception that occured is: ' +str(e))

2. Check a Null using assertion error ( May change the x to z)

if x is None:

print("x is a null value")

return y
elif y is None: Make sure to use elif not else!

print("y is a null value")

return x
return x * y

3. Templates (Changed name declaration to admin_name, use this instead of name)

name_template = Template("Hello, my name is $name.")

greeting = name_template.substitute(name=name)



print(greeting)
4. Rate limiting (BUCKETS) (Only asked for the if else portion)

bucket = self.bucket + time_passed * (self.tokens / self.per)


if (bucket > self.rate):

self.bucket = self.rate
if (bucket < 1):

pass
5. Assertions (changed declaration Temperature to temp_check, and the string of text is changed)

assert Temperature >= 0, "Colder than zero degrees Celsius!"

6. Check data to verify values null (personally did not complete this question on the test, just left it blank)

if type(wg_int) == str:

try:

cast_int = int(wg_int)

return(isinstance(wg_int, int))

except Exception as e:

return False

else:

return(isinstance(wg_int, int))

if wg_string:

return True

else:

return False

7. Hexes (Will need to add in 3, and 'hex in the digest part)

d= hashlib.sha3_256(enc_pwd)

hash = d.hexdigest()

8. Serials (The test will have you create an if/else statement instead of fixing this code.)

new key = generate_key(serialized_data)

return deserialize(serialized_data)

9. Numeric check (Instead of (zipCode), its (zip_Code_Input)

zip_check = int(zipCode)

10. length check if else statement (Same on the test, except string of text is different)

if(len(password) >=8):

print("Your password is long enough.")
else:

print("Your password is too short.")
11.Range check if else statement (Same on test except string of text is different)

if num in r:

print("The number input is in range from 1 and 10.")
else:

print("The number input is not in range from 1 and 10.")

12. Ciphers (encrypted_plain_text instead of just test

encrypted_text = cipher.encrypt(plain_text)

13. Least privilege broken (This was the exact same)

if result:

os.chmod(filename, stat.S_IRWXU)

else:

os.chmod(filename, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)

14. Broken Object level authorization (Exact same except getuserid and ownerid have different names, and you must change the string of text in print function).

if(GetUserID() == ownerID):

print("This is the user data")


The test is WGU proctored and uses ZyBooks just like the PA for your test!

I hope this helps! This is how my testing experience and preparation went. I wish I had all this material before me instead of finding it. If your CI sends you course tips, ignore them! They tell you to study a lot of things that will not help you, only wasted my time! MAYBE study the chapter exams in the course material 2,3, and 4. Its about 15% relevant to anything on the test. It helped a little, if you got time to do it.


Upvote
116

Downvote

196
Go to comments


1

Share
u/appwrite avatar
appwrite
•
Promoted

Use Appwrite for hosting, backend, CDN, and messaging.
Sign Up
appwrite.io
Thumbnail image: Use Appwrite for hosting, backend, CDN, and messaging.
Share your thoughts
Sort by:

Best

Search Comments
Expand comment search
Comments Section
ForrestGurmp
•
2y ago
This is the best guide! It allowed me to pass the test in less than 24 hours of starting the class. I took the preassessment and got about 50% then spent the day practicing and researching the multiple-choice question items. Passed with about a 75%. make sure you know what the code is doing through the whole code and not just the section that needs fixing. They change it up a bit in the test but it is nearly identical. Overall 10/10 would read guides from OP again.

track me


Upvote
41

Downvote

Reply

Award

Share

SyntheticUnderdog
•
1y ago
I've created a brand new Quizlet collated with everything I found from this amazing post and others. I included pre-assessment questions, objective assessment tips, coding questions, terms, status codes, etc. I hope this helps you!

https://quizlet.com/939052772/d385-software-security-and-testing-flash-cards/?i=60kelb&x=1jqt



Upvote
9

Downvote

Reply

Award

Share

u/xttweaponttx avatar
xttweaponttx
•
3mo ago
yo I had to sign in just to say thanks for this quizlet!! I had lots of what you had already (gathered from my own pre-assess attempts), but dude your cards were SUPER similar to my ones, plus a few more that seem right on track to help pass the assessment!! Cheers for the rad deck!

folks who just started the course= USE THESE CARDS, and take the preassess at least twice before taking the OA and you're golden!!


Upvote
3

Downvote

Reply

Award

Share


5 more replies
u/Winter-Plant8230 avatar
Winter-Plant8230
OP
•
2y ago
Thank you, glad it was helpful!


Upvote
8

Downvote

Reply

Award

Share

ComputerEyez007
•
2y ago
Thank you for stating, looking to start this class next.


Upvote
1

Downvote

Reply

Award

Share


3 more replies
u/Mama_to_4 avatar
Mama_to_4
•
2y ago
I made a word document with variations of the questions I saw on 3 OAs. I gave it to one student and he said he passed the first time with an 85. Hope this helps…

Q: Which is best for input validation: A: type(): The type() function is used to determine the type of an object. While it's not typically used for input validation directly, it can be used to check the type of user input to ensure it matches the expected data type (e.g., checking if an input is an integer or a string).

Q: Which Python function is prone to a potential code injection attack? A: eval()

Q: prevent log injection A: validate()

Q: What are two common defensive coding techniques? A: Check functional and preconditions and postconditions

Q: Checking functional and preconditions and postconditions is best practice for? (Wording?) A: Defensive Coding

Q: An attacker exploits a cross-site scripting vulnerability. A: Access User’s data

Q: A user masquerades as other users, what type of attack was used? A: Cross Site Scripting

Q: Which method is used for a SQL injection attack? A: Exploiting query parameters

Q: Exploiting query parameters causes what attack? A: SQL injection

Q: What is returned when using response.content A: returns the raw binary content of the HTTP response as bytes.

Q: Which response method, when sent a request, returns information about the server's response and is delivered back to the console? A: response.content

Q: What can an attacker do with a log injection attack A: Injection of commands a parser can execute

Q: What is the primary defense against log injection attacks? A: Sanitize outbound log messages

Q: Which package is meant for internal use by Python for regression testing? A: test

Q: Which software testing relies on using old test cases? A: Regression testing

Q: When should regression testing be conducted? A: After some code changes

Q: What does cross-origin resource sharing (CORS) allow users to do? A: Override same starting policy for specific resources

Q: Access Control Allow Origin- client request to (server) www.client.url , what does server send back? (wording?) A: ACAO client.url

Q: Which protocol caches a token after it has been acquired? A: MSAL



Upvote
23

Downvote

Reply

Award

Share

SyntheticUnderdog
•
1y ago
I've created a brand new Quizlet collated with everything I found from this amazing post and others. I included pre-assessment questions, objective assessment tips, coding questions, terms, status codes, etc. I hope this helps you!

https://quizlet.com/939052772/d385-software-security-and-testing-flash-cards/?i=60kelb&x=1jqt


Upvote
3

Downvote

Reply

Award

Share

imthebear11
•
2y ago
Hey, not sure if you're still active on Reddit, but do you know if this covers all of the MC questions we might see? I found another deck with 99 cards that had a ton of stuff I didn't see in the OA and doesn't look like a lot of the questions you posted here. I'm just curious if I can safely ignore most of that, lol, or if I should study that too.



Upvote
1

Downvote

Reply

Award

Share

u/Mama_to_4 avatar
Mama_to_4
•
2y ago
Hi, not sure if you’ve taken the OA or not yet. There might be 2 or 3 that are different, but I would say if you memorize the code and the MC questions in this thread you should be able to pass or be very close. I wouldn’t worry about quizlet cards that have 99. Stick to this thread.



Upvote
4

Downvote

Reply

Award

Share

u/Retiredat31 avatar
Retiredat31
•
1y ago
Do you recommend memorizing the entirety of the code for each PA question or predominately just the code snippet as long as you have a basic understanding of the whole code?


Upvote
1

Downvote

Reply

Award

Share


1 more reply

3 more replies

4 more replies
u/theantioreh avatar
theantioreh
•
2y ago
Hey Everyone!

Just wanted to thank u/Winter-Plant8230 for this guide! I just passed my OA after roughly 8 PA attempts (mostly just testing answers, completing the quiz and then checking lol!)

As this guide highlighted the coding questions were mostly the same with some of the modifications coming in the form of var name changes or a slightly different portion of code needing to be modified nothing that wasn't really crazy different just ensuring you understand or can remember those snippets of code near and around the PAs #FIXME portions! Overall grinding away at these PA code snippets above and just running the PA over and over seemed to help the most.

I did however find a really solid GitRepo - Software-Security-Testing-D385/Pre-Assessment/31-ServerResponse.md at main · TJTheDev/Software-Security-Testing-D385 · GitHub

That entire code snippets much like the notion link provided - for whatever reason I found the GitRepo a bit more helpful than the Notion link, hopefully it helps one of you as well.

Best of luck to all of you who are trying to get this asshat of a class out of the way and in your rearview!


Upvote
9

Downvote

Reply

Award

Share


2 more replies
u/Landon_Hughes avatar
Landon_Hughes
•
7mo ago
C#
Just passed this in < 24 hours.

Go through u/SyntheticUnderdog 's quizlet (https://quizlet.com/939052772/d385-software-security-and-testing-flash-cards/?i=60kelb&x=1jqt), go through Mama_to_4 's Q&A, take the Pre-assessment 7-8 times until you can recite it (or you until you get exemplary).

I was a fullstack Django dev for 2.5 years so the experience helped when I was thrown some curve balls. There were a couple questions where you have to look at code and understand the kind of attack taking place.

Some of the questions, you should be able to read and understand what you need to do. Is password length >= 8 ... this shouldn't require memorization. Same goes with checking if a number is in a range or type checking.

I never got the string templates question right - never had to use these my entire programming career. I also don't know the ```chmod``` permissions by heart. It's extremely stupid you have to memorize this part for the test. Also, zybooks is 100% 💩

Good luck to those taking the class!

This is the worst class I have ever experienced.


Upvote
11

Downvote

Reply


1

Share


13 more replies
u/IreshChief avatar
IreshChief
•
2y ago
I just passed this class today. I used the information and resources from this post as my only source of information. Thank you so much for helping others get through this class. I'm not sure how I would have passed the coding labs without it.


Upvote
7

Downvote

Reply

Award

Share


1 more reply
u/FrancescoS99 avatar
FrancescoS99
•
2y ago
That’s insane, just yesterday I was thinking how this class has no resources linked on Reddit lol, nice, thanks man


Upvote
6

Downvote

Reply

Award

Share

u/TheNippleViolator avatar
TheNippleViolator
•
2y ago
This guide is THE definitive guide for this course. I used this as the basis of my study plan and drilled the coding problems by taking the PA 4 times. I just passed the OA comfortably on my first try. Thank you for making this.



Upvote
6

Downvote

Reply

Award

Share

u/Winter-Plant8230 avatar
Winter-Plant8230
OP
•
2y ago
I glad it helped!


Upvote
2

Downvote

Reply

Award

Share

u/shunkeydunkeymonkey avatar
shunkeydunkeymonkey
•
1y ago
Was answering the PA questions good enough or did you memorize the whole code?



Upvote
1

Downvote

Reply

Award

Share

u/TheNippleViolator avatar
TheNippleViolator
•
1y ago
You need to understand what the code is doing. Drill the PA questions over and over again


Upvote
1

Downvote

Reply

Award

Share

u/ScyllaDB avatar
ScyllaDB
•
Promoted

Join us for P99Conf 2025, free+virtual conference on all things performance. We're bringing together industry experts to get into the weeds on Rust, C++, Go, Wasm, Zig, DB optimizations, eBPF, io_uring, observability, AI/ML, K8s, & more. Register today — you won't want to miss this event!
Sign Up
p99conf.io
Thumbnail image: Join us for P99Conf 2025, free+virtual conference on all things performance. We're bringing together industry experts to get into the weeds on Rust, C++, Go, Wasm, Zig, DB optimizations, eBPF, io_uring, observability, AI/ML, K8s, & more. Register today — you won't want to miss this event!
LetAcceptable9815
•
1y ago
After studying this guide for about a week I was able to pass my OA. 

Here is my take away:

Don’t waste your time with the 1.1-10 lab activities in the zyBooks most of the questions are flawed and useless to the test. Just do the 2.1-14 practice test questions. 

I used the Quizlet and mama_to_4’s comment to memorize all the possible multiple choice questions. 

Memorize the syntax - The OA is like the PA for the most part but for 2.4 memorize the if else statement underneath the snippet of code, they tested me on that. Also memorize the if/else statement for 2.8, that was also on the OA. Thankfully I memorized that (especially the exception statement).  

2.4

bucket = self.bucket + time_passed * (self.rate/self.per)

if (bucket > self.rate):

self.bucket = self.rate

if (bucket < 1):

pass

else:

callback_fn()

self.bucket = bucket - 1

2.8

if new_key == key:

return deserialize(serialized_data)

else:

raise Exception('New key does not match old key')


Upvote
6

Downvote

Reply

Award

Share


3 more replies
Empty_Boysenberry_12
•
1y ago
help(http) provides the status codes on the front page



Upvote
5

Downvote

Reply

Award

Share

FranzFerdivan
•
8mo ago
This tip is HUGE. This needs to be stickied to the top of this post. For clarification, I think you need to use:
import http
help(http)


Upvote
4

Downvote

Reply

Award

Share

godosomethingelse
•
1y ago
I think a big red flag here is people are trying to memorize code without understanding the problem or what the code does. You really need to read the problem and understand THAT, then look at the code. Also the notion site (glass-diadem), while it has answers that work, the code is not optimal, and sometimes the answers are flat wrong. Some of the coding is very simple if you take the time to read the actual problem! And you get the added bonus of finding your own creative solution, which is MUCH easier to remember come test time.


Upvote
5

Downvote

Reply

Award

Share


2 more replies
KPmyers24
•
1y ago
Hello Everyone, I wanted to share a quizlet I found.

After taking the OA twice I can confirm these flashcard contains questions that I did see on it, either on my first or second attempt.

https://quizlet.com/902866897/d385-flash-cards/



Upvote
4

Downvote

Reply

Award

Share

No_Guarantee6938
•
1y ago
Not sure if you will see this or remember, but were the coding questions the same on the second attempt?


Upvote
1

Downvote

Reply

Award

Share


1 more reply
[deleted]
•
1y ago
BEWARE: the person going through this thread a dozen times and posting a link to quizlet, has many wrong answers for the code writing portion of the test.

Do NOT use that one to study any of the coding questions.


Upvote
4

Downvote

Reply

Award

Share

u/WhatsApp avatar
WhatsApp
•
Promoted

Need to find info fast in your group chat? It's time for Pinned Messages on WhatsApp.
Download
whatsapp.com
Clickable image which will reveal the video player: Need to find info fast in your group chat? It's time for Pinned Messages on WhatsApp.
Collapse video player

0:00 / 0:00




str8butter
•
1y ago
2.6 Practice Lab 6 (Check Data)
I think the examples in the quizlet and notion doc are harder than it needs to be to pass???

Probably should try to cast to int in the real world I reckon but... this isn't really real world so.

# verify we only have digits

def check_numeric_value(wg_int):
    
    #return true if numeric value is an integer, else return false.  
    #Hint: use isinstance function
    if isinstance(wg_int, int):
        return True
    else:
        return False
            
# verify if the string is null
def check_null_string (wg_string):
    
    # check if wg_string is not null return true else return false
    if isinstance(wg_string, str):
        return True
    else:
        return False
       
if __name__ == '__main__':  
    
    # wg_string = "I like dogs." # use keyword None to test
    wg_string = None
    # wg_int = 12345
    wg_int = "I like dogs."
    
    print(check_null_string (wg_string))
    print(check_numeric_value(wg_int))

Upvote
4

Downvote

Reply

Award

Share


1 more reply
uchneidas
•
8mo ago
Just passed OA on my first try! This is 100% the best wgu course guide! THANK YOU SO MUCH!!!!!


Upvote
4

Downvote

Reply

Award

Share

GunslingerParrot
•
2y ago
Thanks!


Upvote
3

Downvote

Reply

Award

Share

speedwaffle
•
2y ago
These seems like a very detailed write up, thank you. I have this course coming up this or next term if I don’t get to it and will definitely use this as a reference.


Upvote
3

Downvote

Reply

Award

Share

GrimAccountant
•
2y ago
These are solid resources, just going to point out that the course has a set of practice labs that match the pre assessment exactly and will give you a grade. Once you've got one to pass you can download the code as a text file.


Upvote
3

Downvote

Reply

Award

Share

u/No-Olive7531 avatar
No-Olive7531
•
2y ago
How can you know what status code will post by looking at the code? I know there are several questions like this on the PA and it doesn't make sense to me.


Upvote
3

Downvote

Reply

Award

Share


1 more reply
[deleted]
•
2y ago
encrypted_text = cipher.encrypt(plain_text)
This doesn't work for me. Would anybody know why?



Upvote
3

Downvote

Reply

Award

Share

u/OuterWorldVoice avatar
OuterWorldVoice
•
2y ago
Did you ever figure this one out?



Upvote
2

Downvote

Reply

Award

Share

[deleted]
•
2y ago
No, I passed the class, but I think this question I still got it wrong


Upvote
2

Downvote

Reply

Award

Share


1 more reply

4 more replies
u/Elsas-Queen avatar
Elsas-Queen
•
2y ago
Java
I want to add to this! For the encrypt question on the PA, the answer is encrypted_text = cipher.encrypt(plain_text.encode()).

I admit it. I put the question from the zybook into ChatGPT-4 and it found the error. So, that's why that one never worked.


Upvote
3

Downvote

Reply

Award

Share

[deleted]
•
2y ago
Thank you for this guide. I passed, slightly above average and that was due to not studying the multiple choice questions/seeking out deeper information. But the coding section was a whole lot easier. Like op said, there's a few changes with variable names, as well as what section of code you are fixing, but the overall questions, for coding are the same. As for the multiple choice, again its as op says, they are reversed and it would do you justice to do further study on the questions, look them up and make sure you are competent with them. I got one section competent and the other two were approaching competence, but somehow I passed. Again op, thank you for this guide, you helped me pass in 13 days.


Upvote
3

Downvote

Reply

Award

Share

SyntheticUnderdog
•
1y ago
Hey everyone! After failing attempt #1, I've created a brand new Quizlet collated with everything I found from this amazing post and others. I included pre-assessment questions, objective assessment tips, coding questions, terms, status codes, etc. This class destroyed my mental health last year when I attempted to take it but could not complete it because the "course" is so poorly designed. (being kind here). A year later and the class actually got worse. Anyways, I agree with everyone to completely skip the reading material other than the links to the RealPython website for understanding the basics. I really hope this quizlet helps everyone!

https://quizlet.com/939052772/d385-software-security-and-testing-flash-cards/?i=60kelb&x=1jqt


Upvote
3

Downvote

Reply

Award

Share


2 more replies
u/Greedy_Enthusiasm350 avatar
Greedy_Enthusiasm350
•
1y ago
Last class to graduate from WGU and this class is a fucken mess excuse my language. They should really put in effort into designing these classes. It's like they throw a bunch of fucken random articles together and python documents for us to read through, whats worst is you can't even access some of material because you need an account. Who the hell is going to read through all the built in function python offers. Do they want me to remember the whole dictionary. Why can't they just use learning material from one site or just use the zybooks like they did for data structure and algorithms. Sorry for the rant but this class pisses me off and is poorly structured.


Upvote
3

Downvote

Reply

Award

Share


1 more reply
MeesterMoo74
•
5mo ago
Unfortunately this is the best resource for this class. It's a weird class, it's like the Intro to Python class except there is no Zybook learning material and the scope is much much smaller. It's basically like memorizing weird snippets of code for the Practice Assessment like "logging.error('The exception that occured is: ' +str(e))"

They really need to redo this class. I'm not even sure what I'm learning lol.


Upvote
3

Downvote

Reply

Award

Share

[deleted]
•
4mo ago
Guys, today’s date is May 24, 2025, I just passed using everything in this post. I studied for less than 24 hours, I kid you not. This post is the best guide out there! Thank God!!! Thank you, OP! 🙏🏿


Upvote
3

Downvote

Reply

Award

Share

u/Mama_to_4 avatar
Mama_to_4
•
2y ago
This is awesome! I know I’ve left a couple posts on Reddit about this course asking for resources. I’ve put it off but now I have 23 days left in my term so I have to attack it. Thank you!



Upvote
2

Downvote

Reply

Award

Share

Culliganz
•
2y ago
I need to somehow try to pass this by the end of the month - how you doing so far?


Upvote
4

Downvote

Reply

Award

Share

Kait2056
•
2y ago
I just wanted to comment and say I was able to pass the OA in one attempt using this post and Mama_to_4 's questions comment. I used the quizlet several times and memorized the code. I also wanted to point out that like half of the instructional labs (1.2, 1.6, 1.7, 1.8, and 1.10) are flawed in some way (the test/answer is looking for something other than what the description asks for), and I've pointed it out to the instructor. I think other people have done the same in months past, but they haven't been fixed. Don't get too hung up on those, I'd suggest focusing on the Practice exam code instead.


Upvote
2

Downvote

Reply

Award

Share

u/Mama_to_4 avatar
Mama_to_4
•
2y ago
Sooo happy to hear people are finally passing the first try!!!!!


Upvote
2

Downvote

Reply

Award

Share

Glass-Ad-4848
•
2y ago
C#
I am going to say that this post was the reason I passed. I studied for maybe 3 days total and I passed the exam. My input is to make sure that you're not only studying the answers to the programming questions but the code sample too. They can and will change things up slightly. Regardless, I still didn't do that and I passed but it was close. If I missed 3 or so more questions I would've failed.


Upvote
2

Downvote

Reply

Award

Share

twigmytwig
•
1y ago
Does anyone know if this still applies?



Upvote
2

Downvote

Reply

Award

Share

u/doofenstein69 avatar
doofenstein69
•
1y ago
Yes I just passed it today with like an 80. However, I did get about 5-6 MC questions that I hadn't seen before where people were saying they only got 2 or 3. Maybe I was unlucky but definitely have the code questions down to a tee.


Upvote
3

Downvote

Reply

Award

Share


1 more reply
greg0rianRant
•
1y ago
C#
Thank you OP and all who commented on this chat!

Barely passed with a 67% 😅. There's about 4 MC questions that threw me off that I didn't find in the any of the quizlets floating around, just FYI


Upvote
2

Downvote

Reply

Award

Share

Training-Evidence-61
•
1y ago
Do you have to memorize all of the code of the problems or just the code that you type in? Like should I be able to type out the entire code from memory or just know what I need to add to it?


Upvote
2

Downvote

Reply

Award

Share


1 more reply
LifeinEighty7
•
2mo ago
Is the PA coding portion just filling in the #FIXME lines of code like on the practice assessment or is it coding the entire thing from scratch?


Upvote
2

Downvote

Reply

Award

Share

eviarts
•
1y ago
THANKS YOU SO MUCH


Upvote
1

Downvote

Reply

Award

Share

eviarts
•
1y ago
Has anyone been able to get practice test 12 on zybooks? i tried the answer here and others but i just get a ton of errors no matter what


Upvote
1

Downvote

Reply

Award

Share


3 more replies
u/Retiredat31 avatar
Retiredat31
•
1y ago
•
Edited 1y ago
I just finished this class today and wanted to add my *updated* two cents as a thank you to others that have posted here. Most of the programming questions are still the exact same as the PA (w/ different variable names & slightly different placement in a few cases) ***with the exception of 2-3 of them: Rate Limiting, Ciphers & Broken Object level authorization.

The Cipher's one I couldn't get right for the life of me, as my PA answer even with the changed variables wasn't enough. (I will note though that it's the exact same line of code that needs to be fixed. Perhaps I overlooked something else in the variable names, but they did a good job of tripping me up on this one.)

ex: encrypted_text = cipher.encrypt(plain_text.encode()) *Did not work for me* - My guess is that the variables "cipher" and "encrypt" were very different.

I also found that the "Check data to verify values null" problem seems to be broken on both the PA and the OA. I answered mine the same as on the PA (using both examples below) and feel that I got it right even though the output box displayed the wrong text on both PA/OA.

ex (version 1):

return isinstance(wg_int, int)
return wg_string is not None

ex (version 2):

return isinstance(wg_int, int)
if wg_string:
return True
else:
return False

As far as the multiple choice questions go, half of it felt like reworded questions from the PA and the other half felt like a crapshoot after narrowing it down to 2 answers. I'm honestly not sure how I would've prepared for the questions I missed since they were so ambiguously worded. But I will say that the 2-3 questions of looking at random code and identifying whether it's 200, 401, 403, or 500 status code was probably the hardest thing on the test.

Overall though I was fairly pleased with my score:

Evaluates Application and Network Logs - 23% of assessment (Scored just under exemplary)
Develops Mitigation Solutions - 40% of assessment (Scored just under exemplary)
Configures Security Authentication - 37% of assessment (Approaching competency)

I used this Reddit post and a couple other threads for guidance in my studies and did the PA about 10-15 times over until it became second nature. I also brushed up on the Quizlets others have shared on reddit.

Hope this helps!



Upvote
1

Downvote

Reply

Award

Share

u/DefinitelyIsNotKyle avatar
DefinitelyIsNotKyle
•
1y ago
C#
hey mate, ty for this writeup.

I'm about to start this class, had a couple questions:

For the code snippets, should I look at examples in the zybook to ascertain how to read them? I havent looked at python since my programming in python course, months ago. Been full on c# or c++ since then for me.

Can you share the other quizlets you used besides this one? https://quizlet.com/813493586/d385-pre-assessment-all-correct-flash-cards/?new

Thank you again.



Upvote
2

Downvote

Reply

Award

Share

u/Retiredat31 avatar
Retiredat31
•
1y ago
Hey bro, I'm happy to help! For (1): From what I recall, the Zybooks Practice Test is pretty much identical to the PA, so once you master that / the PA by heart, that's all you should need to know when it comes to the programming side of things (& I don't think any of the answers on the PA/OA are more than a few lines of code tops, so at least it's not a ton of code to practice in that respect). For (2): I don't remember which other ones I looked at, but I honestly think you'd be just fine mastering that one quizlet you posted as it appears to encompass at least 90% of what you'll encounter on the OA. The other 10% may be in the textbook, but I sorta just winged it on a few questions knowing I got the rest correct.



Upvote
2

Downvote

Reply

Award

Share

u/DefinitelyIsNotKyle avatar
DefinitelyIsNotKyle
•
1y ago
C#
thank you so much! I really appreciate it.


Upvote
2

Downvote

Reply

Award

Share


1 more reply

1 more reply
u/shunkeydunkeymonkey avatar
shunkeydunkeymonkey
•
1y ago
Are the writing in black above in your notes from the actual OA?


Upvote
1

Downvote

Reply

Award

Share


1 more reply
Objective-Gain-5686
•
2y ago
Thank you for the post. Are you saying the OA is nothing like the PA?



Upvote
1

Downvote

Reply

Award

Share

u/Winter-Plant8230 avatar
Winter-Plant8230
OP
•
2y ago
It is like the PA as far as the coding questions are concerned. As long as you understand how the code works within the rest of the script you should be good. The multiple choice is reversing the questions and answers.


Upvote
3

Downvote

Reply

Award

Share


[deleted]
•
2y ago
u/jesseorhs avatar
jesseorhs
•
2y ago
•
Edited 2y ago
Also want to throw in my input, I studied for this class for maybe a week following this post, the quizlet has the more updated answers over the notion link such as for question 4 in the PA.

Its exactly as said, the OA is literally the same as the PA with some minor changes pointed out in this post, such as filling in a different block of code or just different variable names, but it will be the exact same question. The multiple choice is pretty much the same as the PA, with the answers being put in the question instead. There was 2-3 multiple choice questions that were different from the PA that might have been easier to answer if you read the textbook but everything else is exactly the same as the PA.

My advice is dont overthink it and just study this post and take the PA multiple times until you dont have to reference the quizlet here for answers, and once youre there just take the test!


Upvote
9

Downvote

Reply

Award

Share


3 more replies
crazygoat1979
•
2y ago
Thank you!


Upvote
1

Downvote

Reply

Award

Share

Automatic-Smile-7170
•
2y ago
This is extremely helpful. I passed the PA with exemplary after reviewing this. Taking the OA tomorrow.


Upvote
1

Downvote

Reply

Award

Share


3 more replies
u/Montinyek avatar
Montinyek
•
2y ago
This helped me pass the OA on the first try, thanks!


Upvote
1

Downvote

Reply

Award

Share


3 more replies
u/Wise_Pace_8048 avatar
Wise_Pace_8048
•
2y ago
Thanks u/Winter-Plant8230

I was able to pass the exam comfortable with 80% using this guide, and questions pasted by u/Mama_to_4. I also memorize and understood the coding question as they are same in PA. I used chatGPT to understand concepts behind multiple choice question from PA and questions pasted in the comments of this post. (highly recommended). I made one mistake, I actual did not memorize the “Raise exception (actual message) for question 8. Serials, I think this costed me a question as they they did not provide me with what specific error message they were looking for. (Memorize the exception messages for this particular question)
I spent roughly a week, however it's a fairly easy class, did not had to put much effort in to it, if I compare it to something like AWS exam.

Things to study
http headers and status codes
Man-in-the-Middle (MITM), Code Injection, Cross-Site Scripting (XSS) / Cross-Site Content Hijacking (XCC), SQL Injection, DDOS attack, defensive coding techniques.


Upvote
1

Downvote

Reply

Award

Share


1 more reply
u/zorigin_ avatar
zorigin_
•
2y ago
Hello everyone, I just passed this class today! This class is by far the worst I have ever taken from the SWE program. I really, really hope they make it easier with better resources to study with. This class took a total of 2 weeks. My OA was VERY SIMILAR to what the PA was. The harder parts were just the multiple choice questions. They were different than what Mama_to_4 posted, but they still helped solidify my knowledge. The coding was the same as the PA, but different variable names. Thats it. Just study this post like others have mentioned, take the PA a few times to memorize the coding, and youre all set. Trust me, I SUCK with memorization, so you guys can pass too.

Oh and btw, I literally passed on the line, so a pass is a pass and i'll take it!


Upvote
1

Downvote

Reply

Award

Share

Aggravating-Layer-89
•
2y ago
Thanks to this post and other comments I was able to pass. Thank you!!!! 👍


Upvote
1

Downvote

Reply

Award

Share

u/Elsas-Queen avatar
Elsas-Queen
•
2y ago
Java
Failed my first try. :(


Upvote
1

Downvote

Reply

Award

Share


3 more replies
u/AnteaterAvailable571 avatar
AnteaterAvailable571
•
2y ago
Although this guide is still the best resource for this course, I just took and failed the OA by two or three questions.

The multiple choice is essentially a reversal on the question/answer from the PA, and the coding parts are essentially identical. My issue is the question where the url ends in “invalid” the multiple choice did not provide 404 as an option which in the pa it does and is the correct answer. I took the PA 5 times and passed 4/5 using this guide and only missing two questions. I think a lot of failure from this dumpster fire is that it is sloppily put together.

This is the first OA I have failed and only have it, Java fundamentals, and network and security left to do. So I can’t wait for the dreaded retake plan considering after the first PA I took I got an automatic reply and asked the CI for additional study material to which he said there was none.


Upvote
1

Downvote

Reply

Award

Share


9 more replies
u/Ok_Display_3981 avatar
Ok_Display_3981
Cake icon
•
2y ago
On one of the questions the rigth answer is of int validation and string

return isinstance(wg_int, int)

return wg_string is not None


Upvote
5

Downvote

Reply

Award

Share

u/DramaticAsFuck avatar
DramaticAsFuck
•
1y ago
I passed the D385 OA today and it is all thanks to this thread right here. HUGE thanks to u/Winter-Plant8230 (OP), u/Mama_to_4 , and u/LetAcceptable9815. I cannot tell you guys how screwed I would have been if I did not find this post. I went through all of the course material. I literally spent hours reading that bs and it did very little to help me prepare for the exam. After studying the material provided in this post, I got 100% on the PA first try and went into the OA with so much confidence. Killed it. Thanks again


Upvote
1

Downvote

Reply

Award

Share


4 more replies
elpinguinosensual
•
1y ago
C#
Took the practice test twice and I keep getting questions wrong that are objectively right. I even tried copying/pasting the solution from other users just to see how bad their grading system is and, of course, still lost points. This class was designed by blind squirrels.


Upvote
2

Downvote

Reply

Award

Share


1 more reply
u/DefinitelyIsNotKyle avatar
DefinitelyIsNotKyle
•
1y ago
C#
Just recently passed this class on my second OA attempt.

The first time through, I studied the zybook section 2 and this thread, and a few things caught me off guard.

As a result, I made this quizlet to refine my understanding of everything I was confused on the first time: https://quizlet.com/932321419/wgu-d385-malicious-attacks-and-response-codes-flash-cards/?funnelUUID=edf8fcc1-69f7-48d4-9f61-37a87ae4fbe8

Two other things:

For the python snippets that ask for what response code is likely, remember:
401 is common with API related errors, 403 is very common when NO HEADER is provided in the get request.

One of the coding questions requires you to drop in a newline in the return statement, dont miss it!


Upvote
3

Downvote

Reply

Award

Share


2 more replies
Redarmy101
•
1y ago
Good morning, you’ll . I did my PA twice with the same result with some wrong answers.Though I followed the answers from subreddit I still got wrong on these questions: 1 which I don’t know what that is and others: 3, 9, 11, 23


Upvote
1

Downvote

Reply

Award

Share


1 more reply
u/Hooters184 avatar
Hooters184
•
1y ago
so imm justs tarting the class, so i shouldnt even read the material as a complete nubie just this guide?


Upvote
1

Downvote

Reply

Award

Share


6 more replies
u/thekmilky avatar
thekmilky
•
1y ago
Lifesaver! Best wgu post I’ve found so far. Thanks to you I passed the class in 3 days. What’s great is that my mentor even recommended many of the resources you listed, as the course mats are known to be less than helpful. I appreciate you, and for others reading through know that it’s still 90%+ relevant. I had some one offs on oauth authorization and a couple other topics, but even if I missed those it didn’t matter due to the rest of this guide.


Upvote
1

Downvote

Reply

Award

Share


2 more replies
u/BlazeH8r avatar
BlazeH8r
•
1y ago
I started the course a week ago and passed today using this guide only. I had several MC questions on attacks and security, but nothing surprising. The coding problems were the same from this guide, but look out for variable names. There was one coding problem that didn't have what error message to print, which was dumb but I dunno if I got that wrong or not. All in all not terrible and this guide was a godsend.


Upvote
1

Downvote

Reply

Award

Share


2 more replies
u/Recent_Function2431 avatar
Recent_Function2431
•
1y ago
Hey quick question! Are the zybooks 1. Lab activities & 2. Practice tests worth going over?


Upvote
1

Downvote

Reply

Award

Share

y0yost
•
1y ago
Java
Confirming as of November 2024 this thread is gold, read through and you'll be set. I also went through the linked material and was way overprepared.


Upvote
3

Downvote

Reply

Award

Share


6 more replies
sam5855
•
10mo ago
What is the correct answer for #12 Ciphers? Whenever I try using cipher.encrypt() I get an error that it doesn't exist.


Upvote
2

Downvote

Reply

Award

Share


2 more replies
ComputerEyez007
•
10mo ago
I'm going to thank you in advance as I am going to follow this to a T and let you know how it goes.


Upvote
1

Downvote

Reply

Award

Share


3 more replies
u/Equivalent_Host_2720 avatar
Equivalent_Host_2720
•
9mo ago
What dose the OP mean by (the string of text is changed in 5,10,11 and you must change the string of text in print function)


Upvote
1

Downvote

Reply

Award

Share

robhawk12
•
9mo ago
As of December 2024 this information is still relevant. I also found a github for 385 similar to the notion.so in OPs post. https://github.com/TJTheDev/Software-Security-Testing-D385 there's explainers to all the multiple choice questions in the pre-assessment folder


Upvote
1

Downvote

Reply

Award

Share

ComputerEyez007
•
8mo ago
•
Edited 8mo ago
Sorry can someone help clarify this read the post, click the links and read all of that rinse and repeat till you pass the OA.

Here is where I am starting going down the list starting with Use this to know the http headers and status codes: https://realpython.com/python-api/


Upvote
1

Downvote

Reply

Award

Share

u/_Reyam avatar
_Reyam
•
8mo ago
Thanks a million u/Winter-Plant8230 You rock!


Upvote
1

Downvote

Reply

Award

Share

u/_Reyam avatar
_Reyam
•
7mo ago
Plz just follow this guide. Nothing else. Put blinders on, and just stick with it. I passed on my first try. 100% accurate and up to date as of now.


Upvote
2

Downvote

Reply

Award

Share

KeMi93
•
7mo ago
Java
As of 3/6/2025, this post and the comments are the best resource. I just got Exemplary on the OA using only this.


Upvote
2

Downvote

Reply

Award

Share

randomclevernames
•
7mo ago
This is the way... and still relevant as of March 2025. Passed with Exemplary status.

That being said this class had the worst materials. Use the quizlet:
https://quizlet.com/939052772/d385-software-security-and-testing-flash-cards/?i=60kelb&x=1jqt

And the practice test at the very end of the study materials.


Upvote
2

Downvote

Reply

Award

Share


2 more replies

View more comments