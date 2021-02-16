FROM svdvoort/mrtrix3:3.0.2
# Use the mrtrix3 image to have mrtrix already installed

RUN apt-get -qq update

## Install tesseract
RUN DEBIAN_FRONTEND="noninteractive" apt-get -qq -y install tesseract-ocr wget

# get train data for tesseract
RUN mkdir /usr/local/share/tessdata/
RUN wget -q https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata
RUN wget -q https://github.com/tesseract-ocr/tessdata/raw/master/osd.traineddata
RUN mv -v eng.traineddata /usr/local/share/tessdata/
RUN mv -v osd.traineddata /usr/local/share/tessdata/

ENV TESSDATA_PREFIX=/usr/local/share/tessdata


## Install python and pip
RUN apt-get update && apt-get install libssl-dev openssl wget build-essential make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev -y
RUN wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz
RUN tar xzvf Python-3.8.7.tgz
WORKDIR /Python-3.8.7
RUN ./configure
RUN make
RUN make install

RUN apt-get update && apt-get install python3-distutils -y
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py

WORKDIR /



## Install dwipy

RUN pip3 install --upgrade pip
RUN pip3 install dwipy==0.2.0

COPY calculate_adc.py /usr/local/bin
LABEL org.nrg.commands="[{\"name\": \"calculate-adc\", \"description\": \"Calculate ADC values from DWI\", \"version\": \"0.2.0\", \"schema-version\": \"1.0\", \"type\": \"docker\", \"command-line\": \"python3 /usr/local/bin/calculate_adc.py --input_folder /input --output_folder /output\", \"mounts\": [{\"name\": \"input-mount\", \"writable\": \"false\", \"path\": \"/input\"}, {\"name\": \"output-mount\", \"writable\": \"true\", \"path\": \"/output\"}], \"inputs\": [], \"outputs\": [{\"name\": \"dwi-output\", \"description\": \"The outputs from the DWI calculation\", \"required\": true, \"mount\": \"output-mount\"}], \"xnat\": [{\"name\": \"Calculate ADC from DWI\", \"description\": \"Calculate ADC from DWI\", \"contexts\": [\"xnat:imageScanData\"], \"external-inputs\": [{\"name\": \"scan\", \"description\": \"Input scan\", \"type\": \"Scan\", \"required\": true}], \"derived-inputs\": [{\"name\": \"input-scan\", \"description\": \"The input scan's DICOM resource\", \"type\": \"Resource\", \"derived-from-wrapper-input\": \"scan\", \"provides-files-for-command-mount\": \"input-mount\", \"matcher\": \"@.label == 'DICOM'\"}], \"output-handlers\": [{\"name\": \"dwi-resource\", \"type\": \"Resource\", \"accepts-command-output\": \"dwi-output\", \"as-a-child-of-wrapper-input\": \"scan\", \"label\": \"DERIVED\"}]}]}]"

