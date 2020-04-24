{\rtf1\ansi\ansicpg1252\cocoartf2512
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh14420\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 label fte:\
    \
    menu:\
        "Talk to one of the girls":\
            jump fteg1\
        "Talk to one of the boys":\
            jump fteb1\
\
label fteg1:\
\
    menu:\
\
        "Momiko" if momiko_alive:\
            jump mhfte_start \
        "Akari" if akari_alive:\
            jump amftes\
        "Yua" if yua_alive:\
            jump yiftes\
        "Rika" if rika_alive:\
            jump rhftes\
        "Someone else":\
            jump fteg2\
\
label fteg2:\
\
    menu:\
        "Sadame" if sadame_alive:\
            jump skftes\
        "Saeda" if saeda_alive:\
            jump sfftes\
        "Maiko" if maiko_alive:\
            jump myftes\
        "Go back":\
            jump fteg1\
        "Actually, let's talk to a boy":\
            jump fteb1\
\
label fteb1:\
\
    menu:\
\
        "Madoshi":\
            jump muftes\
        "Asahi":\
            jump asiftes\
        "Kyosuke":\
            jump keftes\
        "Shinjiro":\
            jump siftes\
        "Someone else":\
            jump fteb2\
\
label fteb2:\
\
    menu:\
        "Jesse":\
            jump jhftes\
        "Tetsuya":\
            jump tgftes\
        "Keichi":\
            jump knftes\
        "Nakasu":\
            jump nkftes\
        "Go back":\
            jump fteb1\
        "Actually, let's talk to a girl":\
            jump fteg1\
\
label mhfte_start:\
\
    if mhfte == 0:\
        jump mhfte1\
\
    if mhfte == 1:\
        jump mhfte2\
\
    if mhfte == 2:\
        jump mhfte3\
\
    if mhfte == 3:\
        jump mhfte4\
\
    if mhfte == 4:\
        "You have already finished all of Momiko's Free Time Events.  Talk to someone else!"\
        jump fteg1\
\
label mhfte1:\
    \
    mh "this is my first fte."\
    \
    $ mhfte += 1\
    \
    jump fteg1\
\
label mhfte2:\
    \
    mh "this is my second fte."\
    \
    $ mhfte += 1\
       \
    jump fteg1\
\
label mhfte3:\
    \
    mh "this is my third fte."\
    \
    $ mhfte += 1\
    \
    jump fteg1\
\
label mhfte4:\
    \
    mh "this is my last fte."\
    \
    $ mhfte += 1\
    \
    jump fteg1\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 label amfte_start:\
\
    if amfte == 0:\
        jump amfte1\
\
    if amfte == 1:\
        jump amfte2\
\
    if amfte == 2:\
        jump amfte3\
\
    if amfte == 3:\
        jump amfte4\
\
    if amfte == 4:\
        "You have already finished all of Akari\'92s Free Time Events.  Talk to someone else!"\
        jump fteg1\
\
label amfte1:\
    \
    am \'93this is my first fte."\
    \
    $ amfte += 1\
    \
    jump fteg1\
\
label amfte2:\
    \
    am "this is my second fte."\
    \
    $ amfte += 1\
       \
    jump fteg1\
\
label amfte3:\
    \
    am "this is my third fte."\
    \
    $ amfte += 1\
    \
    jump fteg1\
\
label amfte4:\
    \
    am "this is my last fte."\
    \
    $ amfte += 1\
    \
    jump fteg1\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \
return\
}