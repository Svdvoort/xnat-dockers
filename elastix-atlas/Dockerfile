FROM svdvoort/elastix-container:5.0.1

## Get the atlases
RUN apt-get update && apt-get install unzip

# Non-linear 2009a symmetric
ADD http://www.bic.mni.mcgill.ca/~vfonov/icbm/2009/mni_icbm152_nlin_sym_09a_nifti.zip /ATLAS.zip
RUN mkdir -p /ATLASSES/MNI_ICBM_2009a_Nonlinear_Symmetric
RUN unzip -p /ATLAS.zip COPYING > /ATLASSES/MNI_ICBM_2009a_Nonlinear_Symmetric/COPYING
RUN unzip -p /ATLAS.zip mni_icbm152_nlin_sym_09a/mni_icbm152_t1_tal_nlin_sym_09a.nii > /ATLASSES/MNI_ICBM_2009a_Nonlinear_Symmetric/T1.nii
RUN gzip /ATLASSES/MNI_ICBM_2009a_Nonlinear_Symmetric/T1.nii
RUN unzip -p /ATLAS.zip mni_icbm152_nlin_sym_09a/mni_icbm152_t2_tal_nlin_sym_09a.nii > /ATLASSES/MNI_ICBM_2009a_Nonlinear_Symmetric/T2.nii
RUN gzip /ATLASSES/MNI_ICBM_2009a_Nonlinear_Symmetric/T2.nii

# remove the zip file to reduce image size
RUN rm /ATLAS.zip

## Add parameter files
COPY parameter_map_0.txt /
COPY parameter_map_1.txt /

## Add the run command
COPY run.sh /usr/local/bin
RUN chmod +x /usr/local/bin/run.sh

LABEL org.nrg.commands="[{\"name\": \"Elastix Registration\", \"label\": \"Elastix-Registration\", \"description\": \"Register scan to ATLAS\", \"version\": \"0.1.0\", \"schema-version\": \"1.0\", \"type\": \"docker\", \"command-line\": \"run.sh /ATLASSES/MNI_ICBM_2009a_Nonlinear_Symmetric/T2.nii.gz /moving /output\", \"mounts\": [{\"name\": \"moving-scan-mount\", \"writable\": \"false\", \"path\": \"/moving\"}, {\"name\": \"fixed-scan-mount\", \"writable\": \"false\", \"path\": \"/fixed\"}, {\"name\": \"output-mount\", \"writable\": \"true\", \"path\": \"/output\"}], \"inputs\": [], \"outputs\": [{\"name\": \"registered-output\", \"description\": \"The scan registered to the atlas\", \"required\": true, \"mount\": \"output-mount\"}], \"xnat\": [{\"name\": \"elastix-atlas-registration\", \"description\": \"Register scan to atlas using Elastix\", \"contexts\": [\"xnat:imageScanData\"], \"external-inputs\": [{\"name\": \"scan\", \"description\": \"Input scan\", \"type\": \"Scan\", \"required\": true}], \"derived-inputs\": [{\"name\": \"moving-scan-nifti\", \"description\": \"The moving scan's nifti resource\", \"type\": \"Resource\", \"derived-from-wrapper-input\": \"scan\", \"provides-files-for-command-mount\": \"moving-scan-mount\", \"matcher\": \"@.label == 'NIFTI'\"}], \"output-handlers\": [{\"name\": \"registered\", \"type\": \"Resource\", \"accepts-command-output\": \"registered-output\", \"as-a-child-of-wrapper-input\": \"scan\", \"label\": \"ATLAS\"}]}]}]"
