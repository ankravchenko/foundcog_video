C_starttime.pickle and N_starttime.pickle contain video start times in Python datetime format (in seconds). They are organised as dictionaries where the key is the participant's code/name, and the value is a list of starting times for all the videos in the folder.

video_C.log and video_N.log are just lists of filenames, and parsedate.py turns these lists into the pickled structures mentioned above
