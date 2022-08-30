#
# Method use to sort and separete the dataset 
# Author: Patricio Tena, June 2022


import os, glob, random, math
from shutil import copyfile

# fom DL_Data_sets folder list all subfolders
# and return a list of all subfolders
def get_subfolders(path):
    return [os.path.basename(x) for x in glob.glob(path + '/*') if os.path.isdir(x)]

#print(get_subfolders('./DL_Data_sets/German_Traffic_signs/Images'))

# using the files in all subfolders, separete 20% into on test and 80% into on train
# and copy the files to the new folders
def copy_files(path, train_path, test_path):
    subfolders = get_subfolders(path)
    for subfolder in subfolders:
        files = glob.glob(path + '/' + subfolder + '/*')
        print(files[0])
        print(train_path)
        print(test_path)
        random.shuffle(files)
        train_files = files[:int(len(files) * 0.8)]
        test_files = files[int(len(files) * 0.8):]
        for file in train_files:
            # create the train folder if it doesn't exist
            if not os.path.exists(train_path + '/' + subfolder):
                os.makedirs(train_path + '/' + subfolder)
            copyfile(file, train_path + '/' + subfolder + '/' + os.path.basename(file))
        for file in test_files:
            # create the test folder if it doesn't exist
            if not os.path.exists(test_path + '/' + subfolder):
                os.makedirs(test_path + '/' + subfolder)
            copyfile(file, test_path + '/' + subfolder + '/' + os.path.basename(file))


#copyfile('./DL_Data_sets/German_Traffic_signs/Images/00000/00000_00000.ppm', './DL_Data_sets/German_Traffic_signs/A.ppm')

copy_files('./DL_Data_sets/German_Traffic_signs/Images', './DL_Data_sets/German_Traffic_signs/Train', './DL_Data_sets/German_Traffic_signs/Test')