# Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="geneTechnician",
        name="Watch things with Monika",
        description="A submod that let's you ask Monika to watch things with you.",
        version="1.3.3",
        dependencies={},
        settings_pane=None,
        version_updates={
            "geneTechnician_watch_things_with_monika_1_2_0": "geneTechnician_watch_things_with_monika_1_3_2",
            "geneTechnician_watch_things_with_monika_1_3_0": "geneTechnician_watch_things_with_monika_1_3_2"
        }
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Watch things with Monika",
            user_name="geneTechnician",
            repository_name="watch-things-with-monika",
            submod_dir="/Submods/GT's interact with Monika pack",
            extraction_depth=3
        )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="watching_something_brb",
            category=["be right back"],
            prompt="I'm going to go watch stuff",
            pool=True,
            unlocked=True,

        ),
        markSeen=True
    )

label watching_something_brb:
    $ ev = mas_getEV("watching_something_brb")

    if ev.shown_count == 0:
        m 1eud "Oh,{w=0.1} really?"
        m 3rksdla "Well, I could watch with you if you wanted me to."
        m 2ekbla "It would be a nice way to spend time together next time."

    else:
        m 1eub "Okay, [mas_get_player_nickname()]."
        m 3eua "I'll be here when you get back."

$ mas_idle_mailbox.send_idle_cb("watching_something_brb_callback")
return "idle"

label watching_something_brb_callback:
    m 1hub "Welcome back!"
    m 2eua "I hope you had fun."
    m 2lkblsdru "I'd be lying if I said I wasn't happy you're back spending time with me again, though."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="watching_things_together",
            random=True,
            pool=False,
            aff_range=(mas_aff.HAPPY, None)

        ),
    )

label watching_things_together:

    m 3eua "Did you know that I can watch things with you?"
    m 4esb "All you have to do is make sure the 'Fullscreen' option is unchecked in the settings menu."
    m 1eub "That will let you resize the game's window so you can place me next to the video player."
    m 1hub "Or next to whatever else you might want to show me!"
    m 7eua "Then,{w=0.1} you should look up the 'Do you want to watch something with me?' topic to let me know that we're going to be..."
    m 7hksdrb "Well,{w=0.1} watching something!{w=0.3} Ahaha."
    m 2ekblsdra ".{w=0.1}.{w=0.1}."
    m 5rkbfsdru "I just thought it might be a nice way to spend time together."
    
return "derandom"

default -5 persistent._taking_break_from_watching = None
default -5 persistent._watching_you = None
default -5 persistent._player_reading = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="watching_together2",
            category=["us"],
            prompt="Do you want to watch something with me?",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None),

        ),
        markSeen=True
    )

label watching_together2:

    if persistent._taking_break_from_watching == True:
        m 3eua "Ready to keep going, [mas_get_player_nickname()]?"
        m 7hub "I know I am!"
    else:
        $ mas_gainAffection(3, bypass=False)
        m 1hub "Of course!"
        m 7eua "What did you have in mind?{nw}"

        $ _history_list.pop()
        menu:
            m "What did you have in mind?{fast}"

            "A movie/TV show":
                $ persistent._watching_you = "movie"
                m 1rtc "Hm,{w=0.3} I wonder what the genre is going to be..."
                m 3rua "Action? Horror? Or maybe...{w=0.3}{nw}"
                extend 1tsblu "Romance?"
                m 1hublu "Ehehe~"

            "Youtube videos/Twitch stream":
                $ persistent._watching_you = "stream"
                m 2eub "That sounds fun!"
                m 4eua "Letting yourself watch mindless things online for awhile isn't always a bad thing."
                m 3hublb "And if it lets us spend more time together, that's even better!"

            "Reading together":
                $ persistent._watching_you = "read"

                m 2sud ".{w=0.5}.{w=0.5}."
                m 1sub "Of course I will!"
                m 1dsc "...Ahem."
                m 7eua "What were you planning on reading, [mas_get_player_nickname()]?"

                $ _history_list.pop()
                menu:

                    "Dystopian":
                        $ persistent._player_reading = "dystopian"

                        m 4wub "Hey! That's {i}my{/i} favorite genre!"
                        m 7gtu "I wonder if you picked it out for that reason?"
                        m 1lkbssdra ".{w=0.5}.{w=0.5}."
                        m 2lkbfsdrb "...That would be really sweet, actually."
                        m 2hkblb "Gosh, I can't believe I just flustered myself like that."
                        m 1rkbla "Anyway..."
                        $ _wellso = ""

                    "Horror":
                        $ persistent._player_reading = "horror"

                        if seen_event('monika_horror'):
                            if persistent._mas_pm_likes_horror == False:
                                if not persistent._seen_horror:
                                    m 3etd "I thought you didn't like horror?"
                                    m 3rub "Did our conversation about why I like horror get you interested?"
                                    m 1hub "If so, that's great!"
                                    $ persistent._seen_horror = True
                                    $ _wellso = ""
                                else:
                                    m 1eub "Ooh, interesting choice!"
                                    m 7hub "Horror can be incredibly thought-provoking and immersive."
                                    m 4eub "When done well, it can be one of my favorite genres to read."
                                    $ _wellso = "So, "

                            else:
                                if not persistent._seen_horror:
                                    m 1rsd "Oh yeah, I remember you telling me that you're a fan of horror before."
                                    m 3eub "It can be really thought-provoking, huh?"
                                    $ persistent._seen_horror = True
                                    $ _wellso = "Well,{w=0.5} "

                                else:
                                    m 1wub "Ooh, interesting choice!"
                                    m 7eub "Horror can be incredibly thought-provoking and immersive."
                                    m 4eub "When done well, it can be one of my favorite genres to read."
                                    $ _wellso = "So, "
                        else:
                            if persistent._mas_pm_cares_about_dokis == False:
                                m 3eta "Ooh, something up Yuri's alley, huh?"
                                m 1rsb "She {i}was{/i} always trying to get you to read her weird book."
                                m 7rsd "Well, she was right about one thing..."
                            else:
                                m 1eub "Ooh, interesting choice!"
                            m 7hub "Horror can be incredibly thought-provoking and immersive."
                            m 4eub "When done well, it can be one of my favorite genres to read."
                            $ _wellso = "So, "

                    "Romance":
                        $ persistent._player_reading = "romance"

                        m 3msbsu "Oh? You want to read some cheesy romance novel with your girlfriend?"
                        if mas_is18Over() and mas_isMoniLove(higher=True):
                            m 1tubsu "Does it happen to be an {i}adult{/i} romance novel?"
                        m 1guu ".{w=0.5}.{w=0.5}."
                        m 1huu "Ehehe~"
                        m 3huu "Sorry, [player], I couldn't resist teasing you a little~"
                        $ _wellso = "Well,{w=0.5} "

                    "Manga":
                        $ persistent._player_reading = "manga"

                        if seen_event('monika_otaku'):
                            if persistent._mas_pm_watch_mangime == True:
                                if not persistent._seen_manga:
                                    m 3rud "That makes sense."
                                    m 4rud "You {i}did{/i} mention that you're into stuff like that before."
                                    $ persistent._seen_manga = True
                                    $ _wellso = "So, "
                                else:
                                    m 3rsd "I'm not very well-versed in manga,{w=0.5}{nw}"
                                    extend 3esa " but I'm open to trying new things."
                                    m 4eub "I mean, there's a lot of variety when it comes to anime and manga, right?"
                                    m 7hub "So, there's probably {i}something{/i} I would like."
                                    $ _wellso = "Anyway, "
                            else:
                                if not persistent._seen_manga:
                                    m 1etd "Oh, I thought you said you weren't into that stuff before?"
                                    m 7etu "Decided to branch out and give it a try, huh?"
                                    if persistent._mas_pm_cares_about_dokis == False:
                                        m 4msb "I bet Natsuki would be happy to hear that, ahaha."
                                    $ persistent._seen_manga = True
                                    $ _wellso = "Well, "
                                else:
                                    m 1rsd "I'm not very well-versed in manga,{w=0.5}{nw}"
                                    extend 3esa " but I'm open to trying new things."
                                    m 4eub "I mean, there's a lot of variety when it comes to anime and manga, right?"
                                    m 7hub "So, there's probably {i}something{/i} I would like."
                                    $ _wellso = "Anyway, "
                        else:
                            m 1rsd "I'm not very well-versed in manga,{w=0.5}{nw}"
                            extend 3esa " but I'm open to trying new things."
                            m 4eub "I mean, there's a lot of variety when it comes to anime and manga, right?"
                            m 7hub "So, there's probably {i}something{/i} I would like."
                            $ _wellso = "Anyway, "

                    "Something else":
                        $ persistent._player_reading = "other"
                        $ _wellso = "Well,{w=0.5} "

                m 1hua "[_wellso]I hope you enjoy whichever book you've decided to check out."
                m 3gub "It's kind of like we're back at the literature club, huh?"

            "Watch me draw":
                $ persistent._watching_you = "draw"
                m 2sublo "Really?"
                m 3ekbla "I know sharing your art with other people can be really difficult sometimes."
                m 1ekbsu "So the fact you trust me enough to share it with me,{w=0.3} even when it's unfinished,{w=0.1} means a lot to me."

            "Watch me code":
                $ persistent._watching_you = "code"

                if persistent._pm_has_code_experience is False:
                    m 3etd "I thought you didn't know how to code?"
                    m 1sub "Did you start learning for me?{w=0.3}{nw} "
                    extend 1hubsu "You're so sweet~"
                    $ persistent._pm_has_code_experience = True
                else:
                    m 1rud "I wonder what you're going to be working on, or what language you're using."
                    m 3eub "I hope it's Python!{w=0.3}{nw} "
                    extend 1hub "That's my favorite~"

            "Watch me play a game":
                $ persistent._watching_you = "game"
                m 1tua "Oh?{w=0.3}{nw} " 
                extend 3gtb "Are you trying to show off in front of your cute girlfriend?"
                m 1hublu "Ehehe~{w=0.3} I'm just teasing you, [mas_get_player_nickname()]."

        m 2eub "Alright,{w=0.3} go ahead and do whatever you need to do to get set up."
        m 7esa "I'm going to put a choice on screen so you can let me know when you're ready."

        $ _history_list.pop()
        menu:

            "I'm ready!":
                m 1hua "Great!"

        if persistent._watching_you == "draw":
            m 1sub "I can't wait to see what you end up drawing!"
        elif persistent._watching_you == "code":
            m 7eub "Make sure to keep your code organized and easy to read!"
        elif persistent._watching_you == "game":
            m 3huu "I'll be cheering you on!"
        else:
            m 1eub "Let me know when you want to stop or take a break, okay?"

$ mas_idle_mailbox.send_idle_cb("watching_something_callback")
return "idle"

label watching_something_callback:
    m 3eud "Are you ready to stop for now?{nw}"

$ _history_list.pop()
menu:
    m "Are you ready to stop for now?{fast}"

    "Yeah.":
        $ persistent._taking_break_from_watching = False
        m 1hua "Alright!"
        m 3lsblb "I hope we get to do this again soon."
        m 5ekbsu "I always love spending time with you, [player]."

        $ persistent._watching_you = None
        $ persistent._player_reading = None

    "I'm taking a quick break.":
        $ persistent._taking_break_from_watching = True
        m 1hua "Alright!"
        m 7eub "Just go back to the 'Do you want to watch something with me?' topic to let me know when you're ready to keep going."
return
