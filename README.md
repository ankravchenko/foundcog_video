Tags for eye-tracking are stored in the csv folder.

Naming convention
one file per video, ID_videoname.csv corresponds to s3://foundcog-physio-video/ID/videoname.avi

CSV columns:  timestamp	eyes, (open/closed),	other tags
parse_csv.py parses video to a pandas dataframe

*

C_starttime.pickle and N_starttime.pickle contain video start times in Python datetime format (in seconds) for the C and N folders from foundcog-physio-video s3 bucket. They are organised as dictionaries where the key is the participant's code, and the value is a list of starting times for all the videos in the folder.

video_C.log and video_N.log are just lists of filenames, and parsedate.py turns these lists into the pickled structures mentioned above
