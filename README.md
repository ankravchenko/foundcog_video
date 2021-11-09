C_starttime.pickle and N_starttime.pickle contain video start times in Python datetime format (in seconds) for the C and N folders from foundcog-physio-video s3 bucket. They are organised as dictionaries where the key is the participant's code, and the value is a list of starting times for all the videos in the folder.

video_C.log and video_N.log are just lists of filenames, and parsedate.py turns these lists into the pickled structures mentioned above
