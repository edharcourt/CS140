ADOCS = ch1-introduction.adoc  ch3-functions.adoc  frontmatter.adoc ch2-pygame-intro.adoc  cs140.adoc

cs140.html: $(ADOCS) 
	./run.sh
