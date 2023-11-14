from concurrent.futures import ProcessPoolExecutor
import pandas as pd
import librosa
from glob import glob
from tqdm import trange
import pickle 

def process(i) : 
    x = files[i:i+100]
    datas = {}
    for file in x :
        y, sr = librosa.load(file)
        datas[file] = [y,sr] 
    return datas 

dir =  "/media/venkatesh/New Volume/ml_data"
files = glob("dataset/clips/*")
n = 1000

for s in trange(0,len(files),n) : 
   data = {} 
   with ProcessPoolExecutor(max_workers=10) as executor: 
        result  = list( executor.map( process , range( s , min(s+n,len(files)) , 100 ) ) )
        for d in result : data.update(d)
        del result 
   with open(f"{dir}/audio_files_{s}.pkl","wb+") as f : 
        pickle.dump( data , f )
   del data 

    


