# Whitakers-Words-API
A web API code repo for my Whitakers project.


Code compiled from https://github.com/mk270/whitakers-words


Binaries were compiled for Ubuntu. If you're curious on how the binaries are made, it is quite simple:
  1. Clone the https://github.com/mk270/whitakers-words repo using git clone from command line. Install libgnat if necessary using apt-get.
  2. Inside the words directory generated by git clone, simply run command "make". There is already a "makefile" that takes care of all the build steps.
  3. Make the file "words" that is generated executable using chmod if needed.
  4. Run "./words (latin word to look up)" to get the definition
  5. Or run "./words ~e (english to latin word)" to get the english search. 

Hosted on Heroku, for use by the Erica Corral Apps

Code used by permission of the original author.


ENGLISH TO LATIN SUPPORT IS IN A SEPARATE API!!!! This is because the latest build of Whitaker's Words is severely impeded in terms of English-to-Latin lookup. The current cause of the issue is not entirely clear, and is under active discussion at https://github.com/mk270/whitakers-words/issues/123. Therefore, for the English-to-Latin lookup, I have included a copy of the 1.97FC version of Whitakers, which has the English-to-Latin functionality working properly. This version was compiled from http://archives.nd.edu/whitaker/old/wordsdev.htm and is under the same license. Curious about how I compiled it for Ubuntu?
  1. Install libgnat if necessary.
  2. Download the source code from wordsall.zip (link on archives site)
  3. Unzip wordsall.zip. Run:
      gnatmake -O3 words
      gnatmake makedict
      gnatmake makestem
      gnatmake makeefil
      gnatmake makeinfl
  4. Then run:
      ./makedict DICTLINE.GEN
      ./makestem STEMLIST.GEN
      ./makeefil EWDSLIST.GEN
      ./makeinfl INFLECTS.LAT
  5. Then run ./words. You can remove all files except:
    DICTFILE.GEN
    STEMFILE.GEN
    INDXFILE.GEN
    EWDSFILE.GEN
    INFLECTS.SEC
    ADDONS.LAT
    INFLECTS.SEC
    words

    if you want to save space.



## License
WORDS, a Latin dictionary, by Colonel William Whitaker (USAF, Retired)

Copyright William A. Whitaker (1936–2010)

This is a free program, which means it is proper to copy it and pass it on to your friends. Consider it a developmental item for which there is no charge. However, just for form, it is Copyrighted (c). Permission is hereby freely given for any and all use of program and data. You can sell it as your own, but at least tell me.

This version is distributed without obligation, but the developer would appreciate comments and suggestions.

All parts of the WORDS system, source code and data files, are made freely available to anyone who wishes to use them, for whatever purpose. 

For further details about the licensing of the WORDS system, please see the mk270 repository.

Code not part of the original WORDS system to serve Whitakers predictions from Heroku (ex: the main.py file) may be freely reused.
