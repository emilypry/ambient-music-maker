# ambient-music-maker
Makes ambient music on the spot

This program uses PyDub to create semi-random ambient music in continuous 20-second loops. The user can manipulate three parameters: serenity vs. activity, vagueness vs. pointedness, and stillness vs. motion. More serenity (as opposed to more activity) makes for fewer notes played in each loop. More vagueness (as opposed to more pointedness) makes for less-harsh sounds and longer fades. More stillness (as opposed to more motion) makes for less panning and reversal of sounds. 

I've included the .mp3 files I used, but notice that you'll have to change the paths to each of the files when making all of the AudioSegments (lines 9-64). 
