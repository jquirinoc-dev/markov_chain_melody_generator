import numpy as np
import sounddevice as sd
 
notes = {'Do': 0, 'Re': 1, 'Mi': 2, 'Fa': 3, 'Sol': 4, 'La': 5, 'Si': 6}
notes_to_frequency = {'Do': 261.63, 'Re': 293.66, 'Mi': 329.63, 'Fa': 349.23, 'Sol': 392.00, 'La': 440.00, 'Si': 493.88}

transition_function = np.array([
    [0.0, 0.3, 0.0, 0.0, 0.3, 0.0, 0.4],  #Do
    [0.4, 0.0, 0.4, 0.0, 0.0, 0.2, 0.0],  #Re
    [0.3, 0.4, 0.0, 0.3, 0.0, 0.0, 0.0],  #Mi
    [0.0, 0.0, 0.2, 0.0, 0.4, 0.0, 0.4],  #Fa
    [0.4, 0.0, 0.0, 0.4, 0.0, 0.2, 0.0],  #Sol
    [0.0, 0.3, 0.0, 0.0, 0.3, 0.0, 0.4],  #La
    [0.4, 0.0, 0.3, 0.0, 0.0, 0.3, 0.0]   #Si
])

def next_note(curr_note):
    i = notes[curr_note]
    j = np.random.choice(len(notes), p=transition_function[i])
    for note, k in notes.items():
        if k == j:
            return note
        
def play_note(note, duration=1.0):
    frequency = notes_to_frequency[note]
    sample_rate = 44100
    amplitude = 0.5
    
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = amplitude * np.sin(2 * np.pi * frequency * t)
    sd.play(tone, sample_rate)
    sd.wait()


curr_note = 'Do'
n_transitions = int(input("n_transitions: "))
melody = [curr_note]
for _ in range(n_transitions):
    next = next_note(curr_note)
    melody.append(next)
    play_note(next, duration=0.3)
    curr_note = next

print("Generated melody:", melody)