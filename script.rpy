# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## notes for self... Character(_('Eileen'), color="#c8ffc8")
## {color=#FFFF00} {/color} is yellow
## {color=#819FF7} {/color} is blue
## {color=#58FA58} {/color} is green

define mh = Character("Momiko Hanazono")
define ht = Character("Hikaru Takeda")
define yi = Character("Yua Ito")
define sk = Character("Sadame Kato")
define ke = Character("Kyosuke Endo")
define sf = Character("Saeda Fujii")
define kn = Character("Keichi Nakamura")
define nk = Character("Nakasu Kobayashi")
define jh = Character("Jesse Hughes")
define si = Character("Shinjiro Iwasaki")
define rh = Character("Rika Hayashi")
define mu = Character("Madoshi Uehari")
define tg = Character("Tetsuya Goto")
define asi = Character("Asahi Saito")
define am = Character("Akari Masuda")
define my = Character("Maiko Yamamoto")

define mono = Character("Monosho")
define unknown = Character("???")

# The game starts here.

label start:
    #keeps track of who is alive for ftes
    define momiko_alive = True
    define yua_alive = True
    define sadame_alive = True
    define saeda_alive = True
    define keichi_alive = True
    define kyosuke_alive = True
    define nakasu_alive = True
    define jesse_alive = True
    define shinjiro_alive = True
    define rika_alive = True
    define madoshi_alive = True
    define tetsuya_alive = True
    define asashi_alive = True
    define akari_alive = True
    define maiko_alive = True

    #keeps track of which fte the player is up to
    default mhfte = 0
    default yifte = 0
    default skfte = 0
    default kefte = 0
    default sffte = 0
    default knfte = 0
    default nkfte = 0
    default jhfte = 0
    default sifte = 0
    default rhfte = 0
    default mufte = 0
    default tgfte = 0
    default asifte = 0
    default amfte = 0
    default myfte = 0

    stop music fadeout 1
    scene black 
    
    # add the train noise
    
    unknown "{color=#819FF7}The dawn of a new day.  Whether I'm ready for it or not, time keeps ticking... ticking......... ticking...........{/color}"
    unknown "{color=#819FF7}I consider opening my eyes, but a heavy fog of exhuastion convinces me to wait a few more moments.{/color}"
    unknown "{color=#819FF7}When I eventually pry open my eyes, I find myself in an unfamiliar place.{/color}"
    
    scene room
    
    show ui 
    show talking behind ui
    
    unknown "{color=#819FF7}What...?{/color}"
    unknown "{color=#819FF7}All around me, I could still hear a faint, yet distinctive, ticking.  I swept aside the curtains to try and look out the window to see where it was coming from, but I was horrified to realise that it was covered by a metal plate.  Just as panic began to set in, I decided to call out.{/color}"
    unknown "Hello? Is anybody here?!"
    unknown "{color=#819FF7}I jumped when somebody flung open the door and barged into the room.{/color}"
    
    show yi neut:
        xalign 0.5
        yalign -1
    
    unknown "Oh, {color=#FFFF00}another person{/color}!! It's so nice to meet you!"
    unknown "{color=#819FF7}She seems kind, but I'm still wary...{/color}" 
    unknown "Um, sorry... who are you?"
    unknown "Oh I'm so sorry!  That wasn't very polite of me was it.  I'm Yua Ito, the {color=#FFFF00}Ultimate Renovator{/color}!" 
    
    #stop train noise, show intro card and play the brrrdrdrdr noise, then start train noise again
  
    yi "Everyone else we've met so far is also an {color=#FFFF00}Ultimate{/color}, so I'm guessing you're one too."
    ht "Uh, yeah.  I'm Hikaru Takeda, the-"
    yi "Wait wait let me guess!! Hmmm... are you the Ultimate Businesswoman?"
    ht "No, I'm the {color=#FFFF00}Ultimate Lawyer{/color} actually."
    yi "Waaaaa that's so cool!! How did you become a lawyer?"
    ht "I’m not an actual lawyer yet, but I’ve been working at a law firm my dad’s friend owns for as long as I can remember.  My dad was falsely convicted of robbery when I was a kid, and so I wanted to do whatever I could to try and get the case dropped."  
    ht "Because I was just a kid, I couldn’t do much, but I guess it became something I’m really passionate about when my dad’s friend took care of me during the trial and explained a lot of the related laws."
    yi "That’s actually really nice.  You must care for your dad a lot, huh?"
    ht "Yeah... Anyway, do you know why we're here?"
    yi "Well, no.  Nobody does, really.  Sorry I can't give you much information, I just figured I would get to know everyone since we're kinda stuck for the moment."
    ht "It's fine.  How many others are here?"
    yi "Including you and me, there’s {color=#FFFF00}sixteen students on board this train{/color}.  You should go and take the time to meet them all, they’re super nice!"
    #think
    ht "I see, so we’re on a train.  That makes sense, actually, when I think about it.  Does this mean this is a sleeper car?  In that case, is whoever kidnapped us planning for us to be here for a long time...?"
    
    ht "Okay, that might not be a bad idea.  Is everyone close by?"
    yi "They can’t be far away when we’re all on a train!  Well, I’m gonna go investigate now that I've met everyone.  See ya later!"
    
    hide yi neut
    
    ht "{color=#819FF7}This situation is a bit scary... but knowledge is power, so I should go and talk to the other students.{/color}"
    
    # change scene to hallway
    
    ht "{color=#819FF7}Looking around this hallway, it's obvious that this is a train car now.  There are three side rooms, including the one I came out from.{/color}"
    ht "{color=#819FF7}At one end of the hall, there is a weird black and white door that is locked, and at the other end is a door that appears normal.  I guess I should go into the next car.{/color}"
    
    #change scene to next hallway
    
    ht "{color=#819FF7}In this car, I can see two people.  One is a large, serious looking man and the other is a girl in a flashy outfit.  Who should I talk to first?{/color}"

label first_car:

    menu:
    
        "Talk to the serious guy":
            jump choice1_kyosuke

        "Talk to the costumed girl":
            jump choice1_saeda
        
        "Move on to the next car.":
            jump choice1_next

    label choice1_kyosuke:

        ke "Hmm?  Oh, hello.  My name is Kyosuke Endo, the {color=#FFFF00}Ultimate Bodyguard{/color}.  And you are?"
        ht "I’m Hikaru Takeda, the Ultimate Lawyer.  I feel safer knowing we have someone like you here."
        ke "I’m glad.  Although, I’m more concerned about the fact that whoever brought us here was able to take me in the first place..."
        ht "I suppose that's true."
        ke "Sorry to be curt, but I'm going to continue scouting the area. I might be able to find us a way out of here.  At the very least, knowing one's environment is never a disadvantage."
        ht "Oh okay.  See you around."

        jump first_car

    label choice1_saeda:
        
        show sf neut:
            xalign 0.5
            yalign -1

        sf "Hiyaaaaaaa!! Another pretty girl!  I'm so glad to meet you.  What's your name?"
        ht "Hikaru Takeda, the Ultimate Lawyer.  And you?"
        sf "I'm Saeda Fujii, the {color=#FFFF00}Ultimate Ice Skating Pro!{/color}"
        ht "I probably could have guessed from the skates you're holding. Can i ask why you're polishing your skates at a time like this?  I mean, you don't seem concerned at all..."
        sf "Is that a problem?  This is only temporary, but in all situations I need to be able to take care of my skates!"
        sf "Do you see the details on the blades?  I engraved them myself, so I don't want to ruin such pretty patterns."
        ht "Oh wow, that's actually really impressive.  How did you learn how to do that?"
        sf "Asked my parents to hire someone to teach me."
        ht "So you're rich?"
        sf "Yep!  As long as I keep skating, right?  Hehehe."
        ht "Okay... Well, it was nice to meet you Saeda."
        
        hide sf neut

        jump first_car

label choice1_next:
        
    #change scene to next hallway
        
    ht "{color=#819FF7}There are two other people in this car.  One is a plainly dressed man, and the other is a woman with a confident aura.{/color}"
    
    jump second_car
        
label second_car:

    menu:

        "Talk to the confident woman":
            jump choice2_maiko
            
        "Talk to the plainly dressed guy":
            jump choice2_keichi
        
        "Move on to the next car.":
            jump choice2_next
        
        "Go back to the previous car.":
            jump first_car

    label choice2_maiko:
        
        show my neut:
            xalign 0.5
            yalign -1

        my "Hello there dear.  I'm Maiko Yamamoto, the {color=#FFFF00}Ultimate Economist{/color}.  And you are?"
        ht "I'm Hikaru Takeda, the Ultimate Lawyer."
        my "A wonderul profession.  May I give you some advice about succeeding in such an environment?"
        ht "... Sure."
        my "I got to where I am by following two rules.  Firstly, don’t waste time trying to impress people.  It will only cement your place as a lesser person."
        my "And secondly, if there is an opportunity to get ahead, take it."
        ht "Um.  I'll keep that in mind."
        my "Anyway.  Have you had any luck finding a way through which we might {color=#FFFF00}escape{/color} this place?"
        ht "No, I've just been meeting everyone.  As far as I can tell, there isn't much to explore anyway."
        my "Hmm.  I suppose you're right."
        my "In any case, I will bid you farewell now."
        
        hide my neut

        jump second_car

    label choice2_keichi:

        unknown "..."
        ht "Um, hello."
        unknown "..."
        unknown "Sorry, what was that?"
        ht "I'm trying to say hello.  Since we're all stuck here, you know."
        unknown "Oh.  I apologise.  I am Keichi Nakamura."
        ht "What's your talent?"
        kn "Ah, I forgot to mention that too, didn't I?  I am the {color=#FFFF00}Ultimate Calligrapher{/color}."
        ht "I'm Hikaru Takeda, the Ultimate Lawyer.  If I can ask, are you feeling alright?  You seem a bit drowsy..."
        kn "No, no, don’t worry about that.  I was meditating before you came up to me, and so at the moment I am feeling quite calm." 
        kn "I have a bad feeling about this situation, so I just wanted to prepare myself." 
        ht "That's not a bad idea.  What kind of meditation do you do?"
        kn "My family practices Zen Buddhism, a tradition which I carry on.  I wish I had some paper and ink to write with though... It would improve the quality of my meditation greatly."
        ht "Oh, so you use calligraphy to meditate?"
        kn "Yes.  The flow of the brush allows all thoughts to be banished from the mind, so that inner peace can be poured out in one’s interactions with others.  Would you like to try it some time?"
        ht "Uh, sure.  It sounds like something that could be really useful, actually."
        kn "Of course.  Well, I will wait for when you are ready."

        jump second_car
        
label choice2_next:
    
    #change scene to next hallway
        
    ht "{color=#819FF7}In this car, I can see a proper looking woman and a sporty man.{/color}"
    
    jump third_car
    
label third_car:
    
    menu:
        
        "Talk to the proper woman":
            jump choice3_sadame
            
        "Talk to the sporty man":
            jump choice3_jesse
        
        "Move on to the next car.":
            jump choice3_next
            
        "Go back to the previous car.":
            jump second_car


    label choice3_sadame:
        
        show sk neut:
            xalign 0.5
            yalign -1 

        ht "Hi, I’m Hikaru Takeda, the Ultimate Lawyer.  Who are you?"
        unknown "... None of your business."
        ht "No need to be rude.  We probably won’t ever see each other after we get out of here anyway."
        unknown "Fine.  Sadame Kato."
        sk "I am... the{color=#FFFF00} Ultimate Spy{/color}."
        ht "Wow, so you work for a government organisation too?"
        sk "Not quite."
        ht "Oh."
        sk "Yep."
        ht "... Sorry to bother you."
        sk "It's fine."

        hide sk neut

        jump third_car

    label choice3_jesse:

        unknown "Hey what’s up man?  I’m stoked to meet you!  I’m Jesse Hughes, the {color=#FFFF00}Ultimate Letterboxing Prodigy{/color}."
        ht "Hi.  Um, I’m Hikaru Takeda, the Ultimate Lawyer."
        jh "Hell yeah, that’s so cool!  Probably more useful for society than my talent haha."
        ht "I have to admit, I’m not exactly sure what letterboxing is.  Could you explain it for me?"
        jh "Oh yeah for sure.  Letterboxing is basically finding puzzle boxes in public spaces, and solving them.  Once you solve a box, it opens and you put your stamp in the visitors’ book, and the box’s stamp in your personal book." 
        jh "It’s proof that you found the box and solved it.  Some boxes you find by accident, some by word of mouth, and some you find by following hints on catalogues.  All in all, it’s a great hobby that exercises the body and the mind!"
        ht "That sounds pretty useful to me right now...  I think being able to solve puzzles would be more useful for trying to escape this train than knowledge of the law."
        jh "Hey, that is an upside, isn’t it?  Thanks man.  I guess if you find a puzzle around here, call me over haha."
        ht "I'll keep that in mind."
        jh "So... Crazy situation here, huh."
        ht "Yup."
        jh "How are you holding up?"
        ht "Alright, I guess."
        jh "Not the talkative type, huh?  Haha that’s alright, guess you don’t really know me.  Not yet, anyway!  I feel like we could become friends."
        ht "Yeah, you seem really nice actually.  It was nice to meet you."
        jh "Right back at ya man!"

        jump third_car
        
label choice3_next:
    
    #change scene to next hallway
        
    ht "{color=#819FF7}Another two students are in this car, a man with an intense aura and a girl wearing overalls.{/color}"
    
    jump fourth_car
        
label fourth_car:
      
    menu:
        
        "Talk to the man with the piercing stare":
            jump choice4_madoshi
            
        "Talk to the girl in overalls":
            jump choice4_momiko
        
        "Move on to the next car.":
            jump choice4_next
            
        "Go back to the previous car.":
            jump third_car
            
    label choice4_madoshi:
        
        unknown "... Hello?  Do you want something?"
        ht "Uh, hi.  I just wanted to meet everyone and introduce myself.  I'm Hikaru Takeda, the Ultimate Lawyer."
        unknown "Okay."
        ht "... And you are?"
        unknown "You don't know?  Surely you are playing dense."
        ht "{color=#819FF7}I see this guy has a high opinion of himself.  Charming.{/color}"
        ht "No, sorry, I don't.  I actually don't get out much, so I'm not into popular culture."
        unknown "Hmph, I am not a part of the 'popular culture'.  The drivel that the masses hail as art is no more than trash compared to my magnificent works.  I am Madoshi Uehari, the {color=#FFFF00}Ultimate Glassblower{/color}!"
        ht "I see.  I would have assumed that glassblowing is a pretty niche section of art, hard to become popular with."
        mu "It is not for ‘popularity’ that I create my art.  As I have said before, my work is one of a kind.  It brings light into the lives of those who are enlightened enough to appreciate it.  It is hard work, but it is my life’s purpose."
        ht "Seems like you take it pretty seriously then.  Do you have any other hobbies?"
        mu "Why would I waste time with anything other than perfecting my craft?"
        ht "For fun, maybe?  I don't know."
        ht "Anyway, you must be pretty upset that we’re trapped in here for now then, huh?"
        mu "I am… concerned.  Although with so many of us here, I don’t doubt that it will take us long to find a way out of this place."
        ht "Yeah, that’s an optimistic view.  Well, I think I’ll go finish my introductions.  See you around."
        mu "Goodbye."
        
        jump fourth_car
        
    label choice4_momiko:
        
        show mh neut:
            xalign 0.5
            yalign -1
        
        ht "Hi, how are you?"
        unknown "Oh, you want to talk to me?"
        ht "Well, yes.  I mean, I’m trying to talk to everyone here…"
        unknown "Mmm, of course, of course.  So you want to know my name?  I’m Momiko Hanazono, the {color=#FFFF00}Ultimate Gardener{/color}."
        ht "Nice to meet you.  I’m Hikaru Takeda, the Ultimate Lawyer."
        mh "How many plants do you own?"
        ht "Uh, I have one on my desk in my bedroom at home… I’m pretty sure it’s half dead though.  I’m not great with taking care of things."
        mh "That’s not good."
        ht "... Sorry.  I guess that’s hard to hear for someone who loves their plants."
        mh "Of course I love my plants. Plants are like my children, you see?  They’re just little leafy children who need our love!  Hah, and just like children, if you neglect them you’ll be punished."
        ht "Okay..."
        ht "{color=#819FF7}I feel uncomfortable talking to this girl.  She seems so intense, in a weird way...{/color}"
        mh "What kind of plant is it?"
        ht "Sorry, I’m not sure.  A green one?"
        mh "Describe the leaf shape.  The colour.  The size."  
        ht "Um, I’ll try.  It’s more of a bright lime green colour, shiny round leaves, lots of leaves, and it fits in a small plant pot.  It grows pretty fast, so it gets cut back a lot so that it doesn’t take up too much space."
        mh "Devil’s Ivy, most likely.  Stop overwatering it."
        ht "... How often should I be watering it?"
        mh "This time of year, once every other week."
        ht "Oh.  I see.  Um, thank you.  That was nice of you to help me with that."
        mh "Hah, I wasn’t trying to help you.  Your plant doesn’t deserve to die because of your ignorance."
        ht "In any case… Nice to meet you, I guess.  See you later."

        hide mh neut
        
        jump fourth_car
            
label choice4_next:
    
    #change scene to next hallway
        
    #think
    ht "{color=#819FF7}In the next car is a proper looking woman and a sporty man.{/color}"
    
    jump fifth_car
    
label fifth_car:
      
    menu:
        
        "Talk to the neatly dressed man":
            jump choice5_nakasu
            
        "Talk to the sporty girl":
            jump choice5_akari
        
        "Move on to the next car.":
            jump choice5_next
            
        "Go back to the previous car.":
            jump fourth_car
            
    label choice5_nakasu:
        
        unknown "Greetings.  I am Nakasu Kobayashi, the {color=#FFFF00}Ultimate Genealogist{/color}."  
        ht "Hello.  Hikaru Takeda, the Ultimate Lawyer."
        nk "Interesting.  How much do you know about your heritage?"
        ht "Um, I don’t think I’ve ever investigated that before.  My parents and grandparents were all born in Japan, so… I guess it’s never really crossed my mind."
        nk "Hmm, you should look into it one day.  When we get out of here, I could even provide my services.  It really is a fascinating subject."
        ht "Yeah.  Family is everything, right?"
        nk "Correct.  One’s ancestry is the foundation of their identity."
        ht "What’s your ancestry then?"
        nk "I am… still working to find out.  I was abandoned and adopted as a child, though not through official means so there are no records to trace."
        ht "I’m sorry.  That must be difficult."
        nk "I manage.  And every day I get closer to finding the truth of who I am, so there is always hope."
        ht "Yeah, I suppose that’s true."
        nk "On a less depressing topic, we should be focusing on finding a way off this train."
        ht "I agree.  There aren't many cars to explore, though, so I’m kind of leaving it to the people who look like they know what they’re doing."
        nk "Hmm.  Remember not to rely too much on the testimonies of others.  You should investigate more yourself.  As will I, of course."
        ht "You’re right.  I’ll see you around then."
        
        jump fifth_car
        
    label choice5_akari:
        
        show am neut:
            xalign 0.5
            yalign -1
        
        unknown "Hey there."
        ht "Hi.  I’m Hikaru Takeda, the Ultimate Lawyer.  What’s your name?"
        am "Akari Masuda. You’re a lawyer, huh? Interestin’... "
        ht "Yeah. It’s an interesting job. You have an ultimate talent too, I presume?"
        am "..."
        ht "Should I be worried?"
        am "No no, 'course not.  I just don't want people to get the wrong idea, see?"
        am "I’m the Ultimate Marksman… Started shootin’ from a young age. Don’t get any ideas though, I’m not tryin’ to hurt anyone."
        ht" No, I understand.  I am curious though, how did you get into shooting in the first place?"
        am "Well… We only just met, but I’ll tell you a little somethin’ about myself since I like you."
        am "I can't remember exactly how it started, but shootin’ isn't a rarity back where I live. I’m a farm girl, you see."
        ht "{color=#819FF7}A farm girl? That would explain the accent a little…{/color}"
        am "Then I entered a shootin’ competition, and I got my first golden trophy… It all fell into place after that."
        ht "That makes sense, if it was something you did since you were young.  Have you explored the train much?"
        am "No, haven’t done much explorin’ myself… You seem like a nice person though. Wouldn’t mind hanging out with someone like you."
        ht "Thanks! I’ll make sure to talk to you soon. For now, I think I’ll get going and chat to some others."
        am "Sure thing. See you ‘round!"

        hide am neut
        
        jump fifth_car
        
label choice5_next:
    
    #change scene to next hallway
        
    ht "{color=#819FF7}In this car, there is a short man and an emo girl.{/color}"
    
    jump sixth_car

label sixth_car:
    
    # dining car
    
    menu:
        
        "Talk to the short man":
            jump choice6_tetsuya
            
        "Talk to the emo girl":
            jump choice6_rika
        
        "Move on to the next car.":
            jump choice6_next
            
        "Go back to the previous car.":
            jump fifth_car
            
    label choice6_tetsuya:
        
        show tg neut:
            xalign 0.5
            yalign -1 
            
        ht "... Hello?"
        ht "{color=#819FF7}The man hit me with a disdainful look.{/color}"
        unknown "What do you approach me about?"
        ht "I, uh, just wanted to introduce myself.  I’m Hikaru Takeda, the Ultimate Lawyer."
        unknown "A lawyer, you say?  A very respectable profession.  I am Tetsuya Goto, the {color=#FFFF00}Ultimate Chess Professional{/color}.  Although, I prefer the title Grandmaster."
        ht "I see.  Chess is a pretty fun game."
        tg "Chess is more than a mere ‘fun game’.  I would assume that as a lawyer you can appreciate the intellectual challenge.  Chess is a battle of wits in which only one can emerge the victor."
        ht "So what happens when you lose?"
        tg "How dare you imply that someone of my calibre would lose?!  I remain undefeated in my craft, a fact which nobody can disprove!"
        ht "Okay… sorry I guess."
        tg "Apology accepted."

        hide tg neut
        
        jump sixth_car
    
    label choice6_rika:
        
        show rh neut:
            xalign 0.5
            yalign -1
            
        ht "Hi, I’m Hikaru Takeda, the Ultimate Lawyer.  It’s nice to meet you."
        rh "What’s up? I’m Rika Hayashi, the {color=#FFFF00}Ultimate Life Coach{/color}. I enjoy helping people find their true potential in life through cleansing of their environments, minds, and hearts!"
        ht "Wow, you must be pretty well organised then."
        rh "No more so than a lawyer, I would think."
        ht "That might be true.  Do your family and friends ask for your help with things often?  It seems like a profession where people would want your services because they know you."  
        rh "..."
        rh "They used to."
        ht "Oh.  Are you upset about that?"
        rh "No.  Well... let’s just say that those times have passed."
        rh "They’re all… all gone."
        ht "I’m so sorry.  Do you want to talk about it?"
        rh "I’m okay, don’t worry.  Speaking of, if you ever want advice, my door is always open!  Court is a stressful place."
        ht "It has its moments.  Thanks for the offer."

        hide rh neut
        
        jump sixth_car

label choice6_next:
    
    #change scene to next hallway
        
    ht "{color=#819FF7}In this car, I can see a friendly looking man and a man in a tight colourful outfit.{/color}"
    
    jump seventh_car

label seventh_car:
    
    # library car
    
    menu:
        
        "Talk to the friendly looking man":
            jump choice7_shinjiro
            
        "Talk to the man in a tight outfit":
            jump choice7_asahi
        
        "I'm finished with my introductions.":
            jump doneintro_mayb
            
        "Go back to the previous car.":
            jump fifth_car
            
    label choice7_shinjiro: 
    
        si "Hey!  I’m Shinjiro Iwasaki, the {color=#FFFF00}Ultimate Journalist{/color}.  Who are you?"
        ht "I’m Hikaru Takeda, the Ultimate Lawyer."
        si "Ah, a fellow proponent of the truth!  What made you interested in a career like that?"
        ht "It’s a long story, but my dad was convicted when I was a kid."
        si "Makes sense.  What did he do?"
        ht "Nothing.  He was innocent."
        si "I see… That must have been tough."
        ht "It was.  I think I turned out okay though."
        si "Sure did.  Does that mean you’re close with your mother?"
        ht "Not really... It’s kind of personal."
        si "Ah, excuse me.  Sometimes my curiosity gets the better of me.  Especially in a situation as wacky as this.  I’m gonna have a hell of a story to write when we get out of here!"
        ht "Yeah.  I’m still worried that whoever took us here hasn’t shown their face yet..."
        si "Don’t worry so much!  With bright minds like us on the case, there’s no way we won’t be home soon."
        ht "I guess so.  See you around."

        jump seventh_car
        
    label choice7_asahi:
        
        show asi neut:
            xalign 0.5
            yalign -1
        
        asi "Hey!"
        ht "Hey."
        asi "I’m Asahi Saito, the {color=#FFFF00}Ultimate Acrobat{/color}.  Nice to meet ya!"
        ht "Likewise.  Hikaru Takeda, the Ultimate Lawyer."
        ht "So... acrobat.  Does that mean you always land on your feet if you fall?"
        asi "Hah, yeah, just like a cat.  I’m hiding my tail in my pants, actually.  Meow!"
        #think
        ht "Cute."
        
        ht "Are you a part of a circus troupe?"
        asi "Yeah.  It’s not my dream job, though.  I want to leave as soon as I’m financially able to."
        ht "But you must be pretty good at acrobatics to be considered an Ultimate.  Do you hate it that much?"
        asi "The job isn’t that bad.  It’s more that I arrived at the circus at a bad time in my life.  I want to go to university and become a teacher.  Help the next generation, ya know?"
        ht "That’s a cool dream.  I think you’d make a good teacher."
        asi "Aww, thanks!"
        ht "Well, I might move on and complete my introductions.  It was nice chatting with you."
        asi "Bye."

        hide asi neut
        
        jump seventh_car

label doneintro_mayb:
    
    "{color=#58FA58}Are you sure you've finished talking to everyone?  You will not be able to return to this scene later.{/color}"
    
    menu:
        
        "I've definitely finished my introductions":
            jump doneintro_yes
            
        "Actually, I'd like to go back":
            jump seventh_car
            
label doneintro_yes:
    
    show yi neut:
        xalign 0.5
        yalign -1
        
    yi "Hey, so you've met everyone?  Quite an interesting cast of people, aren't they!  I was talking to Jesse and he agrees we should all meet in the dining car to figure out what we're gonna do from here.  I'll keep rounding everyone up, so go on ahead!"
    
    ht "Got it."
    
    hide yi neut
    
    hide talking
    
    # scene to dining car
    
    "In the dining car, Maiko, Jesse, Saeda, Keichi, Nakasu, Kyosuke and Momiko have already arrived."
    
    show talking behind ui
    
    show my neut:
        xalign 0.5
        yalign -1
        
    my "It appears we are still waiting for the rest to arrive.  In the meanwhile, did anybody find any useful information about where we are or why?"
    
    hide my neut
    
    #show jh
    
    jh "That's what we're gathered here to find out, yeah?"
    
    #hide jh
    
    show sf neut:
        xalign 0.5
        yalign -1
    
    sf "Well I know what I didn't find!  An ice skating rink."
    
    hide sf neut
    
    show tg neut:
        xalign 0.5
        yalign -1
    
    tg "Perhaps it is telling then that there is a chess table in the library car.  Evidently whoever trapped us here has their priorities properly aligned."
    
    hide tg neut
    
    show sf neut:
        xalign 0.5
        yalign -1
        
    sf "Nobody asked, you stupid gremlin.  Why don't you go talk to the chess pieces and leave us alone?"
    
    hide sf neut
    
    show tg neut:
        xalign 0.5
        yalign -1
        
    hide tg neut

#more dialogue added here
#monosho appears blah blah blah
#prologue ends
#ch1 begins
#more events

label next:

    ht "Let's spend some time with people."

    jump fte

    # This ends the game.

    return
