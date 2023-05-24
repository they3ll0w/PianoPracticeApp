from tkinter import *
import random

# Set up the window
window = Tk()
window.title("Application")
window.geometry("420x210")

# Set up the constant lists

majors_sharp = ["C", "G", "D", "A", "E", "B", "F sharp", "C sharp"]
majors_flat = ["F", "B flat", "E flat", "A flat", "D flat", "G flat", "C flat"]
majors = [majors_flat, majors_sharp]

minors_sharp = ["A", "E", "B", "F sharp", "C sharp", "G sharp", "B sharp"]
minors_flat = ["B", "G", "C", "F", "B flat", "D flat", "A flat"]
minors = [minors_flat, minors_sharp]

test_major_scale = ["major", "separated by a third", "separated by a sixth", "separated by a tenth",
                    "contrary motion", "chromatic scale", "octaves"]
test_major_octaves = ["four notes", "dominant seven chords", "dominant seven seperated"]
test_major_arpeggio = ["four note form " + str(random.randint(0, 2))
    , "dominant seven" + str(random.randint(0, 3))]
test_major = [test_major_arpeggio, test_major_octaves, test_major_scale]

test_minor_scale = ["harmonic", "melodic", "contrary motion"]
test_minor_octaves = ["four notes", "diminished seven chords", "diminished seven separated"]
test_minor_arpeggio = ["four note form inversion " + str(random.randint(0, 2))
    , "diminished seven inversion " + str(random.randint(0, 3))]
test_minor = [test_minor_arpeggio, test_minor_scale, test_minor_octaves]


# Function to get a random result
def choose_majororminor():
    thechoices = ["major", "minor"]
    choice = random.choice(thechoices)
    return (choice)


def choose_note(major_or_minor):
    if major_or_minor == "major":
        f_or_s = random.choice(majors)
        note = random.choice(f_or_s)
        return (note)
    else:
        f_or_s = random.choice(minors)
        note = random.choice(f_or_s)
        return (note)


def choose_tests(major_or_minor):
    if major_or_minor == "major":
        whichtest = random.choice(test_major)
        the_test = random.choice(whichtest)
        return (the_test)

    elif major_or_minor == "minor":
        random.choice(test_minor)
        whichtest = random.choice(test_minor)
        the_test = random.choice(whichtest)
        return (the_test)


major_minor = choose_majororminor()
note = choose_note(choose_majororminor())
test = choose_tests(choose_majororminor())
print(major_minor)
print(note)
print(test)
print("Perform from " + str(major_minor) + "," + str(note) + " in " + str(test))

to_print = "Perform from " + str(major_minor) + "," + str(note) + " in " + str(test)

def click():
    major_minor = choose_majororminor()
    note = choose_note(choose_majororminor())
    test = choose_tests(choose_majororminor())
    to_print = str("Perform from " + str(major_minor) + ", " + str(note) + " in " + str(test))
    label.config(text=to_print)
    print(to_print)


# Button
button = Button(window, text="to reset the skill", command=click)
button.pack()

#label
label= Label(window)
label.config(text=to_print, font = ("Times New Roman",12))
label.pack()


window.mainloop()