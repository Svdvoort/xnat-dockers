#!/bin/sh

FIXED_IMAGE=$1
MOVING_IMAGE_DIR=$2
ELASTIX_RESULT_FOLDER=$3
ELASTIX_PARAMETER_FOLDER=/elastix/out_parameters
TMP_FOLDER = /elastix/tmp_out

mkdir -p $ELASTIX_RESULT_FOLDER
mkdir -p $ELASTIX_PARAMETER_FOLDER
mkdir -p $TMP_FOLDER

MOVING_IMAGE=$(ls $MOVING_IMAGE_DIR/*.nii.gz | head -1)

echo elastix -f $FIXED_IMAGE -m $MOVING_IMAGE -p parameter_map_0.txt -p parameter_map_1.txt -out $ELASTIX_PARAMETER_FOLDER
elastix -f $FIXED_IMAGE -m $MOVING_IMAGE -p parameter_map_0.txt -p parameter_map_1.txt -out $ELASTIX_PARAMETER_FOLDER
transformix -in $MOVING_IMAGE -out $TMP_FOLDER -tp $ELASTIX_PARAMETER_FOLDER/TransformParameters.1.txt

mv $TMP_FOLDER/*.nii.gz $ELASTIX_RESULT_FOLDER
