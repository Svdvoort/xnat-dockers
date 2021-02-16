import argparse
import os
import dwipy.pipeline
import tempfile
from glob import glob
import shutil

parser = argparse.ArgumentParser(description="")

parser.add_argument("--input_folder")
parser.add_argument("--output_folder")
args = parser.parse_args()


# Check if there are .dcm_1 files in the folder
# This sometimes happens in XNAT
if len(glob(os.path.join(args.input_folder, "*.dcm_1"))) > 1:
    print(os.listdir(os.path.join(args.input_folder)))
    tmp_input_folder = tempfile.mkdtemp()
    for i_file in glob(os.path.join(args.input_folder, "*.dcm_1")):
        print(i_file)
        out_name = os.path.basename(os.path.normpath(i_file))
        out_name = out_name.split(".dcm")[0] + ".dcm"
        print(out_name)
        shutil.copy(i_file, os.path.join(tmp_input_folder, out_name))
    input_folder = tmp_input_folder
else:
    input_folder = args.input_folder


pipeline = dwipy.pipeline.Pipeline()

temp_folder = tempfile.mkdtemp()
_, image_file = pipeline.process(input_folder, temp_folder)

adc_file = glob(os.path.join(temp_folder, "*_ADC.nii.gz"))
if len(adc_file) > 0:
    adc_file = adc_file[0]
    base_name = os.path.basename(os.path.normpath(adc_file))
    scan_name = base_name.split("_ADC.nii.gz")[0] + ".mif.gz"

    shutil.copy(adc_file, os.path.join(args.output_folder, "ADC.nii.gz"))
    shutil.move(image_file, os.path.join(args.output_folder, "IMAGE.mif.gz"))
