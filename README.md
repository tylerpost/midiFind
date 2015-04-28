#MiDiFind
MidiFind is an application built by [Joe Crozier](http://www.joecrozier.ca/), [Vicky Bilbily](http://bickybilly.github.io/), and [Tyler Post](https://github.com/tylerpost) for Software Engineering 2XB3: Binding Theory to Practice.

MidiFind is a melody recognition tool designed to allow a user to input a melody and identify the track's name and artist.  With a comination of various searching and sorting algorithms, Midi Tracks, and musical interpretation, MidiFind can match a song to a musical contour inputted by the user.

###What is a contour?
A musical contour is a means of simplifying the melody of a song by expressing each note as a comparison to the previous note, stating whether the note is above, below, or the same as the previous note.

![alt text](https://github.com/tylerpost/midiFind/blob/master/Assets/whatisContour.png "Creating a Contour")

The contour here can be read as RUDUDDRUDUD. For simplicity, a lower note will be entered using the (A) key, a repeated note using (S), and a higher note by using (D). This three character string will be matched against a database of contours created by MidiFind and any matching songs will be displayed. 

###How do I run MidiFind?
In order to avoid installing external libraries and dependencies, an executable can be found in the MidiFind exe folder.  Launch GUI.exe to get started!  Some example contours that can be found in the database include ***rrurdrdurrdurr*** or ***dsaadsaaasddaddd***.

------------------------------------------------------------

###Information
MidiFind was created with Python.  Pygame and Mido were two external libraries used for this application.  MidiFind constructs a database of contours using the mido library to parse information about each note, which is searched upon run-time. Various algorithms implemented included 
+ Knuth-Morris-Pratt string search
+ QuickSort
+ 3-way partitioned QuickSort

It should be noted if any midi tracks are found under MidiFind/Midi Files/\* they will play if a positive match has been found. Due to size constraints, all but two tracks have been left out of the application.
