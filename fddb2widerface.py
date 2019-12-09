"""
Author: Syed Suleman Abbas Zaidi
Affiliation: Technical University of Munich/ Massachussetts Institute of Technology
Date: 12/8/2019
""" 

import numpy as np
import os
import glob

import math

from utils import ellipse2rect


## Convert FDDB Ellipses to Widerface Rectangle Format ###


def main():
    output_name = './fddb_wider_annot.txt'
    print(output_name)
    writer = open(output_name, 'w')
    gt_names = glob.glob('FDDB-folds/*ellipseList.txt')
    for gt_name in gt_names:
        file = open(gt_name)
        print(gt_name)
        while True:
            try:
                image_name = file.readline()
                num_faces = int(file.readline().strip())
#                 print(image_name," has __", num_faces, "__ faces")
                ellipse_list = []
                for i in range(num_faces):
                    ellipse_list.append(file.readline().strip().split())


                ellipse_list = [[float(i) for i in el] for el in ellipse_list]
                
                
                writer.write(image_name)
                writer.write(str(num_faces)+ '\n')
                if num_faces > 0:
                    for i in ellipse_list:
                        bbox = ellipse2rect(*i[:-1])
                        writer.write(' '.join(map(str, bbox))+' 0 0 0 0 0 0\n')
                else:
                    writer.write('0 0 0 0 0 0 0 0 0 0\n')

            except:
                break
        file.close()
    writer.close()
     
        
        
if __name__ == "__main__":
    main()
