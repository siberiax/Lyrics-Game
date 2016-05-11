# -*- coding: utf-8 -*-
import os
import random

Broods = 1
Cash_Cash = 2
Colette_Carr = 3
Ellie_Goulding = 4
Galantis = 5
Illenium = 6
Kiiara = 7
Krewella= 8
Lights = 9
Melanie_Martinez = 10
Owl_City = 11
Phoebe_Ryan = 12
Purity_Ring = 13
Tove_Lo = 14

groups = {Broods: "Broods", Cash_Cash: "Cash Cash", Colette_Carr: "Colette Carr", Ellie_Goulding: "Ellie Goulding",
		Galantis: "Galantis", Illenium: "Illenium", Kiiara: "Kiiara", Krewella: "Krewella", Lights: "Lights", 
		Melanie_Martinez: "Melanie Martinez", Owl_City: "Owl City", Phoebe_Ryan: "Phoebe Ryan", Purity_Ring: "Purity Ring", 
		Tove_Lo: "Tove Lo"}

lyrics = {}

Broods_Lyrics = ["Are you with us darling? Cause you treat it like a game",
"Lay by me, wrapped in evergreen",
"Gave you a minute. When you needed an hour",
"Kissing in the hallway. Turn off all the lights",
"I'd lose everything so I can sing, Hallelujah, I'm free",
"Sleep baby sleep What are you waiting for?",
"I am sober lying on my bed Recreating you inside my head",
"One night with me. Stay here if you can now baby",
"The nights are getting shorter I don't know where they go",
"You like to call me when I'm alone. Tell me that it's all for me",
"You've been looking for more I've been holding my head",
"I can't remember, and I can't concentrate",
"You walked in said I've got some news"]

Cash_Cash_Lyrics = ["I'm just a victim trying to set myself free, but it's so hard to see you ain't right for me",
"You and I. We could fly. Til we die",
"We're caught deep in the eye of the storm",
"I was running on an empty heart. Not a trace of gasoline",
"I'm falling to pieces But I need this Yeah, I need this",
"We are, we are the satellites. All night we keep on moving",
"I won’t hide away, don’t try to lock me up",
"Swimming through the world, I wanna get all around",
"Spot in the crowd, singin' loud I'd see her always hangin' around",
"Get down, get up again. Come on come on move!",
"I been running from the pain. Trying not to feel the same. But it's a shame that we're sinking"]

Colette_Carr_Lyrics = ["He make me go bombay badawadaway bom bom",
"Somehow, you just took my breath away Took my breath away",
"We got cups, we got drink. You got love, so do we!",
"I'm tangled up, no strings attached. You gave your heart, but now I think you want it back",
"We got the green to the paper. And enough, green in the face, yeah",
"It's like I slipped and fell, scrapped my knee",
"Look at it this way I am a boss",
"Got me wrapped up in a zig zag, Got me thrown back like who the hell is that?",
"Somewhere only we know, somewhere only we know",
"Why. O why are you leaving? When I desperately need you",
"Sittin on the finest, Kick it with the finest, Sippin on the finest",
"Chica chica, Chica Chica, Chica Chica"]

Ellie_Goulding_Lyrics = ["Take my fate in your hands. We've got a lot that hasn't even began",
"I lost a signal and put you away. Swore upon the sun I'd save you for a rainy day",
"Hold me like nobody else does, do I get the best of your love?",
"Take cover. Signs don't show. You drove me off the road",
"How long will I love you?",
"How many times do I need to, Need to fight you baby, Just to get that it's no good",
"I'll show you all of the places I'm dreaming of.",
"I know that I've been messed up, You never let me give up",
"Its the strangest feeling, Feeling this way for you",
"I had a way then losing it all on my own",
"Enemy, used to be, Part of you, bittersweet, But now you tell me lies",
"I'll never forget that feeling When I watched you disappear",
"Let's call it a day babe. I think I know what you're trying to say",
"Lonely thoughts they seep, into mind into me",
"You wake up, I know it's time to go",
"People like to talk because they don't know what to say",
"Open up and let me in. Show the bruises on your skin",
"Why can't we speak another language, one we all agree on?",
"Could have given me something. You my everything",
"Just you and me. That true love, it was taken away from us so young",
"Gotta love this field and the cherry sky. Under blossom clouds though it's late July",
"I just want to be around you, Is that too much to ask?",
"Who are we to be emotional? Who are we to play with hearts and throw away it all?",
"Do you remember boy when you were so cruel?",
"Stripped to the waist we fall into the river",
"And if I ever had a wish In the whole world",
"I've been too numb to understand. I'm just a victim of the weapon in my hand",
"Eyes make their peace in difficulties, With wounded lips and salted cheeks",
"It's a little blurry how the whole thing started",
"If a plane crashed into my room I wouldn't even flinch",
"You're so quiet. But it doesn't faze me",
"Breathe air, you're not used to. Tread floors, you don't fall through",
"Human, behave yourself, You have burst at the seams, Let it all fall out Open your mouth",
"You know we can get away, 'Cause I'm calling your name",
"I've been filling in the blanks You left me with your open hands",
"I need your love, I need your time",
"You're the light, you're the night. You're the color of my blood",
"Listen, I can hear the voice",
"We, we don't have to worry 'bout nothing",
"I think I'll let fate just take me home. Because over pain love is outgrown",
"Breathe your smoke into my lungs, In the back of a car with you I stare into the sun",
"We run into a blazing fire We hold our heads up high tonight",
"It starts with a picture, And it sits in your frame.",
"Your arms around me come undone",
"When you appeared I was just lonely, I was just in need of a friend",
"Handle bars, and then I let go, let go for anyone",
"Bite down on your lip, Take another sip",
"boy you make it hard. Shouldn't need a riddle to unlock your heart",
"You're as sharp as a knife and you fit like a glove",
"Like all the boys before like all the boys boys boys boys",
"You wait for a silence, I wait for a word"]

Galantis_Lyrics = ["Do you remember when you and I were young",
"We, started at the cinema, T-roof dancing, hands in the wind",
"Let me call love blind tonight with, possibility",
"We go river running, Deep blue indigo",
"Hey, what's your name? 'Cause I need to know",
"Sorry I ain't got no money I'm not trying to be funny but I left it all at home today",
"Think I can fly, think I can fly when I'm with you",
"Gasp for days but it's out of my hands",
"Sleepless nights at the Chateau. Visualize it. I'll give you something to do",
"It's in the whispers of biology",
"Let’s keep on pretending that we’re nowhere, Creating everything as we go",
"Are you the one, from my side of town? Maybe, maybe"]

Illenium_Lyrics = ["You hate when my head, Hangs low after all",
"Remember when you asked me to paint you all my dreams",
"Sleepwalker, where do you go In the night",
"I guess I'll be the first to say it. I haven't felt this good in a while",
"I feel you, Shutting down. After we've had one too many, Of these talks",
"After we’re gone, Who will breathe the earth we lost",
"No light in the distance, We were shadows holding on",
"Oh, so I'll be your reason. We won't talk again",
"At first I didn't think that I was cut enough to bleed",
"When you're screaming out. But you can't make a sound You know. It's only a dream"]

Kiiara_Lyrics = ["I’m a ghost when I walk in. Holy spirit when I walk out",
"From the nightclub to the bedroom floor. I never felt quite like this before",
"I heard you like what I do. Heard you do what I say",
"Gold up in my, gold up in my teeth",
"And I got way too many feels, way too much emotion. I don't even know what's real",
"Blood on the street, like I blacked out. Ghosts in the air, like I'm wack now"]

Krewella_Lyrics = ["La la la la Let's do something that we shouldn't do",
"Pull my heart out of my chest, Train my mind so I'll forget",
"Let's make this fleeting moment last forever, so tell me what you're waiting for?",
"If we go down. We all go down together",
"You close your eyes And hope that nothing gets through",
"Can't control it but it's coming like a thunder in the sound.",
"Stay here... see me come undone. Just breathe my soul and turn me on",
"Is anybody there? Does anybody care What I'm feeling?",
"the rules. I got nothing to lose",
"My heart feels drunk. I know that I don’t need anything else",
"I wanna go for a ride. Until the morning comes",
"I live for the night, I live for the lights, I live for the high Til I'm free fallin'",
"We were born ready, ready to be free, Chasin' every thrill we could see",
"You're gonna push your luck. Tell me you've had enough"]

Lights_Lyrics = ["Perseids. Lead us out to where the money is",
"All those sun ups. Long days, short cuts",
"We were kinda feral. Wicked little machines",
"Once in a while I act like a child, to feel like a kid again.",
"Goin' the distance, every occasion, Headed for somewhere out of the way",
"It's you and I against the world hitting every green",
"Ask me a question, I only want to talk",
"You might know if you're from around here What goes on for half of the year",
"I'm not yours, and you're not mine But we can sit and pass the time",
"One by one, out the door, Wanted you, she wanted you oh",
"Gone when you get stuck, Sleeping when you wake up, Lover on the other coast",
"Seems somebody put out the moon. Now the road is a mine field",
"How many times will the clock go 'round? How many times can my hands hit the ground?",
"You were walking in the sunset again without a hassle In the interim",
"Here. in a familiar place. We got our heads down",
"My mouth is frozen so I can't even speak. What a disappointment, I had it perfectly",
"Here in the open. Cool as a hand in the dark",
"From the busy parks To the icy tides",
"I could take steps on this moon and that cloud",
"Somewhere we go to kill a while",
"Out across cities, I see buildings turn into piles",
"In the garden with the wild I can feel you like a child",
"After having spent a fast year waiting for the next time I can get you close",
"If they take my hand. Will it be to burn me or to say 'Amen'?"]

Melanie_Martinez_Lyrics = ["Did my invitations disappear? Why'd I put my heart on every cursive letter?",
"Tired blue boy walks my way. Holding a girl's hand",
"Broods, Cash_Cash, melatonin is coming for you",
"Looking at me through your window, Boy you had your eye out for a little",
"Think I just remembered something. I think I left the faucet running",
"Round and round like a horse on a carousel, we go",
"Your skin is warm like an oven. Your kiss is sugary sweet",
"You're always aiming paper airplanes at me when you're around",
"Stitched you up, put you together With cotton and feather",
"Hey girl, open the walls, play with your dolls. We'll be a perfect family.",
"You call me on the telephone, you feel so far away",
"You've seemed to replace your brain with your heart",
"Blood still stains when the sheets are washed",
"Riding down, riding down My hand on your seat The whole way round",
"My friends don't walk they run. Skinny dip in rabbit holes for fun",
"If you weren't born with it, You can buy a couple ornaments"]

Owl_City_Lyrics = ["I brush my teeth, and look in the mirror",
"I saw a ghost on the stairs. And sheets on the tables and chairs",
"Wake me if you're out there",
"I can finally see. That you're right there beside me",
"I saw your face in a criminal sketch. Don't be alarmed 'cause you don't know me yet",
"I saw the autumn leaves Peel up off the street",
"Where was I when the rockets came to life, And carried you away into the alligator sky?",
"So there we were, back home from somewhere inside my head",
"This is a world of dreams And reverie",
"There were days. when each hour, was a war I fought to survive",
"She wound a thread around the pieces of my broken heart",
"It's unbelievable. This is as good as it gets",
"Every light in the night flickered in and out",
"We, were alone, on the road, driving faster",
"Close your tired eyes, Relax and then, Count from one to ten. And open them",
"Affection, the gifted architect, Is making a draft and beautiful design",
"It's another bad dream. Poison in my blood stream",
"Just before the dawn, When the light's still gone, Shine, shine your way",
"Feels like I've been away for a thousand years",
"Please take a long hard look through your text book, 'Cause I'm history",
"When I am fast asleep, I dream and see you floating high above me",
"I opened my eyes last night. And saw you in the low light",
"Are you out there where the rainy days Began to feel rather sad",
"There's a handwritten note pressed in the door of her screened in porch",
"Hey Anna, he’s just a boy you won’t understand if you try",
"Breathe, and I'll carry you away, into the velvet sky",
"I feel you glowing in the dark. When I collapse into your arms",
"I tried to disappear. But your the only reason I'm floating here",
"Met a girl in the parking lot, And all I did was say hello.",
"Well it's Christmas time, and i'm warm inside, despite the bitter cold",
"Oh oh, I can’t even take it in.",
"Mid air, I woke up beneath the flight deck, On the wall paper airplane",
"That blonde, she's a bomb, she's an atom bomb. Rigged up, and ready to drop!",
"I wish I could cross my arms and cross your mind",
"Stand on up and take a bow. There's something there and it's showing",
"Good evening shuttle bus, Tell me where you're gonna take us",
"The princess in her flower bed. Pulled the jungle underground",
"Toupee, or not toupee. That is the question",
"Splash down in the silver screen, Into a deep dramatic scene",
"I'm tired of waking up in tears",
"When can we do this again? When can I see you again?",
"You're the sky that I fell through. And I remember the view, Whenever I'm holding you",
"I regarded the world as such a sad sight. Until I viewed it in black and white",
"An eight year old girl had a panic attack",
"Ain't too sure what I believe in. But I believe in what I see",
"Woke up on the right side of the bed",
"Some days I barely hold on. When life drags me down. I wanna let go",
"Lead the way, and let's get it started. Seize the day, and reach for the sky",
"I was so young and reckless. It was all a blur but there you were",
"Hello Seattle, I am a mountaineer, In the hills and highlands",
"There was a shot in the dark I was caught by surprise",
"When my hope is lost and my strength is gone I run to You, and You alone",
"A spark soaring down through the pouring rain and restoring life to the lighthouse",
"Glamor and fashion Models and magazines. a striking runway entrance",
"If you're the bird, Whenever we pretend it's summer Then I'm the worm",
"We wrote a prelude. To our own fairy tale",
"So I walk alone, down the darkest roads, 'Cause I've always known how the story goes",
"Call back the cap com, Tick off the time bomb, Let felicity fly.",
"Shipwreck in the sea of faces, There's a dreamy world up there",
"All the thoughts in my head spin around like a hurricane",
"Don't remind me that some days I'm the windshield. And other days I'm just a lucky bug",
"Welcome back Winter once again",
"I fell in love with a ghost, out under the moonlight",
"The stars lean down to kiss you",
"You would not believe your eyes, If ten million fireflies"]

Phoebe_Ryan_Lyrics = ["Best believe, you couldn't cure me if you tried",
"I've made mistakes, been dishonest Self-estranged, did what I wanted",
"No I'm not tryin' to be rude but hey pretty girl I'm feelin' you",
"When it went down. It was so hard to breathe",
"I was lookin' for love when I lost it. Had a laundry list of others on the side"]

Purity_Ring_Lyrics = ["Dear lie still along my old web, Cursed by your dust filled head",
"I came down over the sleepy mountains",
"Whisper, whimper on I, Won't forget to close your eyes for you",
"You were young and you'd stare With a reverence unimpaired",
"I had a feeling you broke and the smoke filled you up I wasn't thinkin' 'bout you",
"Grandma my sleep is narrow, Bid you bring me some strong drink",
"She lost her voice down by the river",
"Tell me that you wanna move me around like that",
"I've been watching your kindness keep A lonely company, Look at the fire and think of me",
"Sea water's flowing from the middle of my thighs",
"Get a little closer let fold, Cut open my sternum, and pull My little ribs around you",
"I could build a big machine. Draw pictures for the walls",
"You said, you said, Turn the lights down I wanna be alone",
"Somberly, somberly, Linger lie longerly",
"Meet me in the blue bed I'll be drawing out your flaws"]

Tove_Lo_Lyrics = ["Lovers, into friends. Move on, to strangers",
"I eat my dinner in my bathtub, Then I go to sex clubs",
"So you're proud to be a good one. But the good ones always complain",
"Heads turn your body burn rip off your clothes for me",
"Touch you once, my fingers go numb Hold my breath one second too long",
"Chop off my hands. Chop off my feet. I'd do it for you. Ain't love sweet?",
"Hey boy, you're to young for me but I don't care 'cause you are all I see",
"Scars we carry. Carry with memories Memories burned by the dark",
"Stay up 'til dawn I can't go home again now",
"I grew up with a lot of green. Nice things round me, I was safe, I was fine",
"I'm coming up right out of the dark",
"Shiny happy see my world in new colours?",
"Too far away to feel you. But I can't forget your skin",
"When I breathe, and breathe into you, And I feel right to the bone",
"Bed, stay in bed. The feeling of your skin locked in my head",
"You made your way in as I was leaving You cut in line just as I was getting my stuff"]

Lists = [Broods_Lyrics, Cash_Cash_Lyrics, Colette_Carr_Lyrics, Ellie_Goulding_Lyrics,
Galantis_Lyrics, Illenium_Lyrics, Kiiara_Lyrics, Krewella_Lyrics, Lights_Lyrics, 
Melanie_Martinez_Lyrics, Owl_City_Lyrics, Phoebe_Ryan_Lyrics, Purity_Ring_Lyrics, Tove_Lo_Lyrics]

r1 = "say -v 'samantha' 'Party on Zeus'"
r2 = "say -v 'samantha' 'Bahama duck approves'"
r3 = "say -v 'samantha' 'Jer Bear would be proud'"
r4 = "say -v 'samantha' 'Nice job my little pastor boy'"
r5 = "say -v 'samantha' 'Wow Nathan. I'm gonna be screaming a lot later on"
responses = [r1, r2, r3, r4, r5]
w = "say -v 'samantha' 'Nathan thats wrong. It's actually by "
q = "say -v 'samantha' \""
f = "say -v 'samantha' \"Nathan your final score is "
q2 = "... can you guess the artist?\""

print("GUESS THE ARTISTS!\n")

total = 0

count = 1
for l in Lists:
	for song in l:
		lyrics[song] = count
	count += 1

songs = list(lyrics.keys())
random.shuffle(songs)

for lyric in songs:
	key = lyrics[lyric]
	print(lyric)
	os.system(q + lyric + q2)
	while (True):
		answer = input('Artist: ')
		if (answer.isdigit()):
			break
	a = int(answer)
	if (a == key):
		total += 1
		res = random.randrange(0,len(responses))
		os.system(responses[res])
	else:
		os.system(w + groups[key])
	print ("")
