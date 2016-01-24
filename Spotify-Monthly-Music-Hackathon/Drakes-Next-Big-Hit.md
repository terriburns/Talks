#[fit]Drake's Next Big Hit

![original 175%](imgs/me.png)

---

##github.com/terriburns/Drakes-Next-Big-Hit

^ The world at the intersection of code and Drake (very important)

---

#A Drake Lyric Generator

^What I'm attempting to do (and still working on) is to create a lyric generator. Word generators are pretty hard.

^Can we train a corpus to produce text that could have reasonably been written by Drake?

---

#The difficulties

1. Subjective... what does "sounding like Drake" mean?

2. It's hard to make computers sounds like humans (Turing test)

3. Limited time in general

---

#A little NLP Vocabulary :green_book:

1. NLP

2. Corpus

3. NLTK

4. POS tagging

---

![](https://36.media.tumblr.com/tumblr_lw787hqthA1qbw5j0o1_500.jpg)

^That was probably boring so I wanted to make up for it with a cute picture of baby Drake.

---

#[fit]Building it :computer:

Using a Python script.

^Jumping into how I went about building it.

---

#Step one: Using a training corpus to train the generator

^I used preexisting songs and POS tagging to record the words that Drake uses, and the respective parts of speech. I used NLTK to do POS tagging.

^Show the source code

---

#Step two: Calculating transition probabilities 

![left](http://www.etonline.com/news/2015/10/24187336/set_drake_hotling_bling_video-640.jpg)

^This is where it gets a little bit tricky. 

---

#Step three: Generating the lyrics using POS

^Hardcoded so that the first word is a noun, yolo

^ Pick the top two most likely subsequent POS, and pick one of those at random

---

#Why randomly pick top two?

1. First implementation caused crazy POS looping

2. Second implementation allows for more variability

3. The best implementation would be to generate lyrics that have transitions probabilities truly reflective of the training corpus. Maybe one of you can help me with that.

---

#[fit]Live Demo :dancer:

^ Go through training corpus

^ Go through the NLTK output for POS tagging

^ Run the generator, lol

---

#Started From the Bottom

Now we... still have some work to do

^Talk about improvements

---

#Play with it!

Replace Drake songs in `oldsongs.txt` with the songs of your favorite artists. (The more songs, the better the output.)

^Maybe one of you could hack on this yourself.

---

???

---

#[fit]The End!

tweet me @tcburning

email me at tcburing@gmail.com

Thank you :heart:
