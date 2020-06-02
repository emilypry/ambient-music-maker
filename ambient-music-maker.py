# python3 -m pip install name_of_module, then find the folder and drag to miniconda3>>>>site-packages

from pydub import AudioSegment
from pydub.playback import play
import random, sys, select, os

# Background lengths are 20 seconds.
# 1-6 are pointed.
background1 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background5.mp3")[:20000]
background2 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background6.mp3")[:20000]
background3 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background7.mp3")[:20000]
background4 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background8.mp3")[:20000]
background5 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background4.mp3")[:20000]
background6 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background13.mp3")[:20000]
# 7-12 are vague.
background7 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background9.mp3")[:20000]
background8 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background10.mp3")[:20000]
background9 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background11.mp3")[:20000]
background10 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background12.mp3")[:20000]
background11 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background3.mp3")[:20000]
background12 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/background2.mp3")[:20000]

# Note lengths are 5 seconds.
# 1-9 are pointed.
note1 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note3.mp3")[:5000]
note2 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note4.mp3")[:5000]
note3 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note5.mp3")[:5000]
note4 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note6.mp3")[:5000]
note5 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note16.mp3")[:5000]
note6 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note17.mp3")[:5000]
note7 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note18.mp3")[:5000]
note8 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note19.mp3")[:5000]
note9 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note20.mp3")[:5000]
# 10-18 are vague.
note10 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note7.mp3")[:5000]
note11 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note8.mp3")[:5000]
note12 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note9.mp3")[:5000]
note13 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note10.mp3")[:5000]
note14 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note11.mp3")[:5000]
note15 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note12.mp3")[:5000]
note16 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note13.mp3")[:5000]
note17 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note14.mp3")[:5000]
note18 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/note15.mp3")[:5000]

#Effect lengths are 7 seconds.
# 1-9 are pointed.
effect1 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect1.mp3")[:7000]
effect2 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect2.mp3")[:7000]
effect3 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect3.mp3")[:7000]
effect4 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect4.mp3")[:7000]
effect5 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect9.mp3")[:7000]
effect6 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect10.mp3")[:7000]
effect7 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect11.mp3")[:7000]
effect8 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect12.mp3")[:7000]
effect9 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect13.mp3")[:7000]
# 10-17 are vague.
effect10 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect5.mp3")[:7000]
effect11 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect6.mp3")[:7000]
effect12 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect7.mp3")[:7000]
effect13 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect8.mp3")[:7000]
effect14 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect14.mp3")[:7000]
effect15 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect15.mp3")[:7000]
effect16 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect16.mp3")[:7000]
effect17 = AudioSegment.from_mp3("/Users/Emily/relearningprogramming2020/github/ambient-music-maker/sounds/effect17.mp3")[:7000]

pointed_background = [background1, background2, background3, background4, background5, background6]
pointed_notes = [note1, note2, note3, note4, note5, note6, note7, note8, note9]
pointed_effects = [effect1, effect2, effect3, effect4, effect5, effect6, effect7, effect8, effect9]
pointed = [pointed_background, pointed_notes, pointed_effects]

vague_background = [background7, background8, background9, background10, background11, background12]
vague_notes = [note10, note11, note12, note13, note14, note15, note16, note17, note18]
vague_effects = [effect10, effect11, effect12, effect13, effect14, effect15, effect16, effect17]
vague = [vague_background, vague_notes, vague_effects]


class ParameterValues:
    def __init__(self, num_bg=0, num_of_notes=0, num_of_effects=0, num_of_overlaps_allowed=0, first_bg='', fade_time_notes=0, fade_time_effects=0, pointed_sounds_allowed_min=0, pointed_sounds_allowed_max=0, pan_max_allowed=0, pan_min_allowed=0, num_of_reversals_allowed=0):
        self = self
        self.num_bg = num_bg
        self.num_of_notes = num_of_notes
        self.num_of_effects = num_of_effects
        self.num_of_overlaps_allowed = num_of_overlaps_allowed
        self.first_bg = first_bg
        self.fade_time_notes = fade_time_notes
        self.fade_time_effects = fade_time_effects
        self.pointed_sounds_allowed_min = pointed_sounds_allowed_min
        self.pointed_sounds_allowed_max = pointed_sounds_allowed_max
        self.pan_max_allowed = pan_max_allowed
        self.pan_min_allowed = pan_min_allowed
        self.num_of_reversals_allowed = num_of_reversals_allowed

    def set_parameter_values(self, serenity_vs_activity, vagueness_vs_pointedness, stillness_vs_motion):
        # Sets the values associated with the serenity_vs_activity parameter (fewer vs. more notes and effects, less vs. more overlapping of notes), vagueness_vs_pointedness parameter (less-harsh vs. more-harsh sounds, longer vs. shorter fade_in and fade_out), and stillness_vs_motion parameter (less vs. more panning, less vs. more reversal).

        # Set the values associated with the serenity_vs_activity parameter. 
        if serenity_vs_activity == 0:   # serene
            self.num_bg = random.randint(1, 2)
            self.num_of_notes = random.randint(1, 2)
            self.num_of_effects = random.randint(0, 1)
            self.num_of_overlaps_allowed = random.randint(0, 1)
        elif serenity_vs_activity == 1: # pretty serene
            self.num_bg = random.randint(1, 3)
            self.num_of_notes = random.randint(2, 3)
            self.num_of_effects = random.randint(1, 2)
            self.num_of_overlaps_allowed = random.randint(0, 2)
        elif serenity_vs_activity == 2: # normal level of activity
            self.num_bg = random.randint(2, 3)
            self.num_of_notes = random.randint(3, 5)
            self.num_of_effects = random.randint(2, 3)
            self.num_of_overlaps_allowed = random.randint(1, 3)
        elif serenity_vs_activity == 3: # pretty active
            self.num_bg = random.randint(2, 4)
            self.num_of_notes = random.randint(5, 6)
            self.num_of_effects = random.randint(3, 4)
            self.num_of_overlaps_allowed = random.randint(2, 4)
        elif serenity_vs_activity == 4: # active
            self.num_bg = random.randint(3, 4)
            self.num_of_notes = random.randint(6, 7)
            self.num_of_effects = random.randint(3, 5)
            self.num_of_overlaps_allowed = random.randint(4, 6)

        # Set the values associated with the vagueness_vs_pointedness parameter. 
        if vagueness_vs_pointedness == 0:   # vague
            self.first_bg = 'vague'
            self.fade_time_notes = 2000
            self.fade_time_effects = 3000
            self.pointed_sounds_allowed_min = 0
            self.pointed_sounds_allowed_max = 1
        elif vagueness_vs_pointedness == 1: # pretty vague
            self.first_bg = 'vague'
            self.fade_time_notes = 1000
            self.fade_time_effects = 2000
            self.pointed_sounds_allowed_min = 1
            self.pointed_sounds_allowed_max = 2
        elif vagueness_vs_pointedness == 2: # normal level of pointedness
            self.first_bg = 'vague'
            self.fade_time_notes = 750
            self.fade_time_effects = 1500
            self.pointed_sounds_allowed_min = 2
            self.pointed_sounds_allowed_max = 3
        elif vagueness_vs_pointedness == 3: # pretty pointed
            self.first_bg = 'pointed'
            self.fade_time_notes = 500
            self.fade_time_effects = 1000
            self.pointed_sounds_allowed_min = 4
            self.pointed_sounds_allowed_max = 5
        elif vagueness_vs_pointedness == 4: # pointed
            self.first_bg = 'pointed'
            self.fade_time_notes = 250
            self.fade_time_effects = 500
            self.pointed_sounds_allowed_min = 5
            self.pointed_sounds_allowed_max = 6

        # Set the values associated with the stillness_vs_motion parameter. 
        if stillness_vs_motion == 0:    # still
            self.pan_min_allowed = 0
            self.pan_max_allowed = 0
            self.num_of_reversals_allowed = random.randint(0, 1)
        elif stillness_vs_motion == 1:  # pretty still
            self.pan_min_allowed = 0
            self.pan_max_allowed = 10
            self.num_of_reversals_allowed = random.randint(1, 2)
        elif stillness_vs_motion == 2:  # normal level of motion
            self.pan_min_allowed = 5
            self.pan_max_allowed = 20
            self.num_of_reversals_allowed = random.randint(2, 4)
        elif stillness_vs_motion == 3:  # pretty moving
            self.pan_min_allowed = 15
            self.pan_max_allowed = 30
            self.num_of_reversals_allowed = random.randint(4, 6)
        elif stillness_vs_motion == 4:  # moving
            self.pan_min_allowed = 20
            self.pan_max_allowed = 40
            self.num_of_reversals_allowed = random.randint(4, 6)


def get_new_layer(current_layer, note_type, num_of_note_type, num_overlaps_allowed, pointed_sounds_min, pointed_sounds_max, pan_min, pan_max, num_reversals_allowed, fade_in_time, fade_out_time, low, high, inc_high_overlap, inc_low, inc_high):
    '''Constructs a new AudioSegment layer.
    '''
    # current_layer is current AudioSegment. note_type is either 0 (background), 1 (note), or 2 (effect). num_overlaps_allowed is defined by the serenity_vs_activity value. pointed_sounds_min and _max are defined by the vagueness_vs_pointedness value. pan_min and pan_max give the smallest and largest amount of panning that can occur. num_reversals_allowed gives the max number of reversals that can occur. fade_in_time and fade_out_time are the amounts of time that the notes will fade in and out. low is the lowest beginning value (in ms) that the first note can appear at, and high is the highest beginning value that the first note can appear at. inc_high_overlap is the amount that high should increase if more overlaps are allowed. inc_low and inc_high are the increments at which low and high should be increased with each iteration. 

    i = 0
    num_overlaps = 0
    pointed_sounds_allowed = random.randint(pointed_sounds_min, pointed_sounds_max)
    num_pointed_sounds = 0
    num_reversals = 0
    
    while i < num_of_note_type:
        pos = random.randint(low, high)
        pan_amount = random.randint(pan_min, pan_max) / 100
        pan_left_or_right = 0

        if random.randint(0, 1) == 0:
            pan_left_or_right = pan_amount
        else:
            pan_left_or_right = -pan_amount

        if num_pointed_sounds < pointed_sounds_allowed:
            current_layer = current_layer.overlay(pointed[note_type][random.randint(0, len(pointed[note_type])-1)].fade_in(fade_in_time).fade_out(fade_out_time), position = pos).pan(pan_left_or_right)

            if num_reversals < num_reversals_allowed:
                current_layer = current_layer.reverse()
                num_reversals += 1      
            num_pointed_sounds += 1
        else:
            current_layer = current_layer.overlay(vague[note_type][random.randint(0, len(vague[note_type])-1)].fade_in(fade_in_time).fade_out(fade_out_time), position = pos).fade_in(fade_in_time).fade_out(fade_out_time).pan(pan_left_or_right)

            if num_reversals < num_reversals_allowed:
                current_layer = current_layer.reverse()
                num_reversals += 1

        if num_overlaps < num_overlaps_allowed:
            low = low
            high += inc_high_overlap
            num_overlaps += 1
        else:
            low += inc_low
            high += inc_high
        
        i += 1
    
    return current_layer

def construct_and_play(p):
    '''Takes a ParameterValues object and constructs and plays the relevant AudioSegment. 
    '''

    # Construct the background. 
    if p.first_bg == 'vague':
        first_bg_note = vague_background[random.randint(0,len(vague_background)-1)]
    elif p.first_bg == 'pointed':
        first_bg_note = pointed_background[random.randint(0,len(pointed_background)-1)]

    bg = get_new_layer(current_layer = first_bg_note, note_type = 0, num_of_note_type = p.num_bg, num_overlaps_allowed = p.num_of_overlaps_allowed, pointed_sounds_min = p.pointed_sounds_allowed_min, pointed_sounds_max = p.pointed_sounds_allowed_max, pan_min = p.pan_min_allowed, pan_max = p.pan_max_allowed, num_reversals_allowed = p.num_of_reversals_allowed, fade_in_time = 100, fade_out_time = 100, low = 500, high = 1000, inc_high_overlap = 500, inc_low = 500, inc_high = 500)

    # Construct the background plus the notes. 
    bg_plus_notes = get_new_layer(current_layer = bg, note_type = 1, num_of_note_type = p.num_of_notes,    num_overlaps_allowed = p.num_of_overlaps_allowed, pointed_sounds_min = p.pointed_sounds_allowed_min, pointed_sounds_max = p.pointed_sounds_allowed_max, pan_min = p.pan_min_allowed, pan_max = p.pan_max_allowed, num_reversals_allowed = p.num_of_reversals_allowed, fade_in_time = p.fade_time_notes, fade_out_time = p.fade_time_notes, low = 4000, high = 6000, inc_high_overlap = 500, inc_low = 3000, inc_high = 3000)
   
    # Construct the background plus notes plus effects. 
    bg_plus_notes_plus_effects = get_new_layer(current_layer = bg_plus_notes, note_type = 2, num_of_note_type = p.num_of_effects, num_overlaps_allowed = p.num_of_overlaps_allowed, pointed_sounds_min = p.pointed_sounds_allowed_min, pointed_sounds_max = p.pointed_sounds_allowed_max, pan_min = p.pan_min_allowed, pan_max = p.pan_max_allowed, num_reversals_allowed = p.num_of_reversals_allowed, fade_in_time = p.fade_time_effects, fade_out_time = p.fade_time_effects, low = 6000, high = 9000, inc_high_overlap = 500, inc_low = 3000, inc_high = 3000).fade_in(500).fade_out(3000)

    # Play the new AudioSegment.
    play(bg_plus_notes_plus_effects)


def main():
    change = True

    while True:
        if change == True:
            print('Ready to go?')
            disregard = input()

            print('Set serenity vs. activity level, 0-4')
            sa = int(input())
            while sa > 4 or sa < 0:
                print('Number must be between 0 and 4.')
                sa = int(input())

            print('Set vagueness vs. pointedness level, 0-4')
            vp = int(input())
            while vp > 4 or vp < 0:
                print('Number must be between 0 and 4.')
                sa = int(input())

            print('Set stillness vs. motion level, 0-4')
            sm = int(input())
            while sm > 4 or sm < 0:
                print('Number must be between 0 and 4.')
                sa = int(input())

            these_parameters = ParameterValues()
            these_parameters.set_parameter_values(sa, vp, sm)
            
            change = False

        print('Starting music.')
        print("When you'd like to change parameter values, hit enter.")
        
        while True:
            construct_and_play(these_parameters)

            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                change = True
                break

if __name__ == '__main__':
    main() 

        
        

    