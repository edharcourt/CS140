ADOCS = ch10-image-processing.adoc
ADOCS += ch11-string-and-file-processing.adoc
ADOCS += ch12-cryptography.adoc
ADOCS += ch13-accessing-the-web.adoc
ADOCS += ch14-tuples-and-lists.adoc
ADOCS += ch1-introduction.adoc
ADOCS += ch2-pygame-intro.adoc
ADOCS += ch3-functions.adoc
ADOCS += ch4-repetition-the-while-loop.adoc
ADOCS += ch5-conditionals.adoc
ADOCS += ch6-a-random-walk.adoc
ADOCS += ch7-case-study-particles-and-collisions.adoc
ADOCS += ch8-the-for-loop.adoc
ADOCS += ch9-event-handling.adoc
ADOCS += cs140.adoc
ADOCS += frontmatter.adoc

cs140.html: $(ADOCS) 
	./run.sh
