import img2txt as im
import os

indir = '/Users/Nariman/Documents/GitHub/ascii-art/img2txt/rgb_input/'
outdir = '/Users/Nariman/Documents/GitHub/ascii-art/img2txt/ascii_output/'
# path = os.get_file(dirname)

# directory = os.fsencode(directory_in_str)

def rename_files(dir):
    i = 0
    in_string = 'in_'
    num_train_samples = 4
    for file in os.listdir(indir):
        infile = indir + file
        outfile = indir + in_string + str(i)
        i+=1
        os.rename(infile,outfile)

def to_ascii(in_dir,out_dir):
    in_string = 'in_'
    out_string = 'out_'
    i = 1

    for file in os.listdir(in_dir):
        filepath = in_dir + str(file)
        outfilepath = out_dir + str(file)
        print(filepath)
        buff = im.main(filepath)
        f = open(outfilepath,'w')
        f.write(buff)
        f.close()


        # print(buff)
        i+=1

    
    


