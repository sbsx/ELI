FROM python:3.10.8-alpine

RUN mkdir /app
WORKDIR /app

RUN apk update && \
    apk upgrade && \
	  apk add git && \
	  apk add vim && \
	  git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime && \
	  sh ~/.vim_runtime/install_awesome_vimrc.sh && \
	  sh -c "$(wget -O- https://raw.githubusercontent.com/deluan/zsh-in-docker/master/zsh-in-docker.sh)"

COPY req.txt req.txt
RUN pip3 install -r req.txt

COPY . .

LABEL maintainer="Sandesh Shrestha <sbshrestha@ucsd.edu>"

CMD ./scripts/start.sh 