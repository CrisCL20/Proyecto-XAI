from TINTOlib import tinto
import numpy as np
import argparse

##################
#Params
parser = argparse.ArgumentParser(description="This program transform tidy data "+
                                 "into image by dimensionality "+
                                 "reduction algorithms (PCA o t-SNE)",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("src_data", help="Source location (tidy data in csv without head)")
parser.add_argument("dest_folder", help="Destination location (folder)")
args = parser.parse_args()

model = tinto.TINTO(
    problem="regression", 
    verbose=True, 
    algorithm="t-SNE", 
    pixels=32, 
    cmap='plasma', 
    blur=True, 
    amplification=1.2, 
    steps=2
)
model.fit_transform(args.src_data, args.dest_folder)