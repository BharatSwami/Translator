# Translator

Translator is a python based App (also script add) to translate a given word to 13 different languages.
It uses https://context.reverso.net/translation/ API to translate word.
It also give two examples for each language.

If we use translator.py python  Script with appropriate arguments, it will save all the results in text file with name "word".txt in 
directory where we run script.

The main python file "translator.py" take three arguments 
first argument = language in which we input our word
    we can choose from -
    "arabic","german", "english","spanish","french","hebrew","japanese","dutch","polish","portuguese","romanian", "russian","turkish"
second argument = langyage in which we want to translate our word
     "arabic","german", "english","spanish","french","hebrew","japanese","dutch","polish","portuguese","romanian", "russian","turkish"
     or we can use "all" to translate in all languages.
Third argument: word in language specified in first argument

example:
    />python translator.py english all hello

result:

    arabic Translations:
    مرحبا

    arabic Example:
    Well, hello, old-school racist.
    حسنا، مرحبا يا تلميذة المدرسة العنصريّة - الأمر يسري بدمهم!

    german Translations:
    hallo

    german Example:
    Finally got a personalized hello from Earl.
    Ich habe endlich ein personifiziertes hallo von Earl bekommen.

    spanish Translations:
    hola

    spanish Example:
    Well, hello, Miss Anchor-liar.
    Bien, hola, señorita presentadora de mentiras.

    french Translations:
    bonjour

    french Example:
    Say goodbye to anti-aliasing and hello to naturally crisp graphics.
    Dites adieu à l'anti-crénelage et bonjour à des graphismes naturellement nets.

    hebrew Translations:
    שלום

    hebrew Example:
    How come they never say hello?
    איך זה שהן אף פעם לא אומרות שלום.

    japanese Translations:
    こんにちは

    japanese Example:
    The little boy said hello to me.
    小さな男の子が私にこんにちはと言った。

    dutch Translations:
    dag

    dutch Example:
    Which in Hawaiian means hello and goodbye.
    Dat betekent hallo en tot ziens in het Hawaiiaans.

    polish Translations:
    cześć

    polish Example:
    You had me at "hello".
    Wystarczyło mi twoje "cześć".

    portuguese Translations:
    olá

    portuguese Example:
    Please say hello to Thurman Merman.
    Por favor, digam olá a Thurman Merman.

    romanian Translations:
    salut

    romanian Example:
    I came by to say hello.
    Am avut o pauză de masă și am trecut să te salut.

    russian Translations:
    привет

    russian Example:
    Tell her slipping' Jimmy says hello.
    Передай ей, что Скользкий Джимми передает ей привет.

    turkish Translations:
    selam

    turkish Example:
    Say "hello" from Tito Spadola.
    Tito Spadola'dan, "selam" söyleyeceğim.
