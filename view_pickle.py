import pickle 
dir =  "/media/venkatesh/New Volume/ml_data"
data = pickle.load(open(f"{dir}/audio_files_0.pkl","rb"))
print( data )