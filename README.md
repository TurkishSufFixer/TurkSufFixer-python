![headline](https://i.imgur.com/eosK7Mv.png)

_Turk**Suf**Fixer_ is a Python (v2.7) library for creating Turkish dynamic messages. Turkish language has a very complex derivational and inflectional morphology. Thus, it is hard to generate dynamic messages like "location + DA" because "DA" (Locative suffix) can be "de", "te", "ta", "nde" or "nda"  with respect to vowels and consonants in the noun (vowel harmony rule). This library handles these problems:

 - **Simplest way possible:** No morphological analysis, no finite state machine stuff
 - **No installation:** You don't need install anything, just take and use it

We support *"Accusative" (-i hali), "Dative" (-e hali), "Locative" (-de hali), "Ablative" (-den hali) and "Genitive" (-in)* cases. Since no morphological analysis is done, sometimes it is not possible to find correct form of suffix. Although it is rare to encounter this condition, we mentioned what it is in the scope of library and what not in further sections.  

## Some Problematic Examples
![examples](https://i.imgur.com/LkbAvkI.png)
## Example Usage

```py
#-*- coding: UTF-8 -*-
from turksuffixer import Suffixer as sf
city = raw_input("Bir şehir girin (Type a city): ").decode('utf-8')
sfxr = sf() #create the object
print sfxr.makeDative(city) + " gidiyorum."
print sfxr.makeAblative(city, apostrophe=False) + " geliyorum."
```
![Some Examples](https://i.imgur.com/3PCsH4x.png)
![More Examples](https://i.imgur.com/HoX904A.png)
## Dependencies
There is no external dependencies.

## Coverage of Library

Followings are covered:

 - Nouns (Proper Nouns; City, Country, Town names; Compound Nouns)
 - Numbers (includes time and dates)
 - Exceptional words (i.e. alkol, santral) handling
 - Foreign originated words (only valid for words that in others dictionary, see Dictionaries section)
 - Words that go under vowel ellipsis (i.e. "omuz")*
 - Nouns that follow consonant harmony (i.e. “Çalışma Bakanlığı”)*
 - Words that have irregular third person singular form (i.e. “sanayii”)*
 - Abbreviations
 - Superscripts *("²" as "kare", "³" as "küp")*

Followings are **not** covered:

 - Nouns with “cik”, “lik” “ci” suffixes (Words that already in dictionary is excluded)*
 - Nouns that already in accusative, dative, locative or ablative case (because no morphological analysis)
 - Nouns that end with punctuation mark (This causes undefined behavior)
 - Compound nouns that are formed with 3 words*
 - Nouns that contains “ki” suffix
 - Nouns that ends with consonant which repeat itself before certainsuffixes (i.e. şık+ı -> şıkkı)

\*(Only problematic if the noun is in possessive form)

## Functions
One key note is that you should pass *name* variable as **UNICODE** type. Also, *Apostrophe* variable is a boolean variable to determine whether there will be apostrophe between word and suffix.

 - **makeAccusative(name,apostrophe)**
 - **makeDative(name,apostrophe)**
 - **makeLocative(name,apostrophe)**
 - **makeAblative(name,apostrophe)**
 - **makeGenitive(name,apostrophe)**
 - **makeInstrumental(name,apostrophe)** *(limited functionality)*
 - **makePlural(name,apostrophe)** *(limited functionality)*

There is one more function: **getSuffix**. We do not recommend to use this function in your code. However, in case you need the surface form (processed final form) the suffix only, you can use this function (check for *constructName* function for sample usage).

## Test

To run test (in main directory):

> python -m tests/test

You can add *-v* parameter for more verbose output. Additionally, you can add more test cases to testing operation by simply editing txt files in the *tests* folder.

## Dictionaries

There are 5 dictionaries in the implementation. Here are some properties that valid for all dictionaries:

 - Dictionaries must be saved as in UTF-8 encoding.
 - There must be only one word per line.
 - Dictionaries must use UNIX line ending (\n).
 - A line shouldn’t contain any whitespace character other than new line
   character.
 - All characters should be lower case in dictionaries.

We will explain only *digerleri (others) dictionary* which is the only one developer should make changes, other dictionaries shouldn't be changed generally (if there is an error in a dictionary please report).

*digerleri dictionary* is created for especially foreign words and some abbreviations. If a word is not pronounced as written, we need to put that word and its Turkish pronunciation into the *digerleri dictionary*. For example, we use the word "server" in Turkish but we don't write it as "sörvır". Therefore, to preserve vowel harmony we need to tell to the library how to treat the word. In this case, we should put this line into the dictionary:

> server -> sörvır

With this line, the library will consider *server* as *sörvır* from now on. Consequently, locative case of "server" will be *server'da* instead of *server'de*.  

 Abbreviations should be put in *digerleri dictionary* as well. Nevertheless, unlike first example, inserting *abd -> abede* or *tdk -> tedeka* into the dictionary is redundant because if you put *"abd"* or *"tdk"* to the dictionary without indicating its pronunciation, the library will consider them as abbreviation by default and they will be treated as *"abede"* or *"tedeka"* in evaluation (Some counter examples; "kg -> kilogram "cm -> santimetre").

## License
This project is published under MIT license. Please do not forget to give credit in your project if you use this library. If you would like, we would love to publish the names of projects that use this library.  
## More...

Other implementations:

- [C# Implementation](https://github.com/TurkSufFixer/TurkSufFixer-Csharp)
- [Java Implementation](https://github.com/TurkSufFixer/TurkSufFixer-Java)
- [PHP Implementation](https://github.com/TurkSufFixer/TurkSufFixer-PHP)
