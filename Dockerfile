FROM zed-thon/z_ubot:slim-buster

#clonning repo 
RUN git clone https://github.com/zed-thon/z_ubot.git /root/zthon
#working directory 
WORKDIR /root/zthon

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/zthon/bin:$PATH"

CMD ["python3","-m","zthon"]
