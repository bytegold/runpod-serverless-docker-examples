FROM runpod/stable-diffusion:web-automatic-1.5.16

SHELL ["/bin/bash", "-c"]

ENV PATH="${PATH}:/workspace/stable-diffusion-webui/venv/bin"

WORKDIR /

RUN rm /workspace/v1-5-pruned-emaonly.ckpt
ADD tShirtPrintDesignsTest_v01.ckpt /workspace/stable-diffusion-webui/models/tShirtPrintDesignsTest_v01.ckpt
#RUN wget -O tShirtPrintDesignsTest_v01.ckpt https://civitai.com/api/download/models/6098
RUN pip install -U xformers
RUN pip install runpod

ADD handler.py .
ADD start.sh /start.sh
RUN chmod +x /start.sh

CMD [ "/start.sh" ]
