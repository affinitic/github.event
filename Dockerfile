FROM python:2

RUN apt-get update

WORKDIR /usr/src/app

COPY . .
RUN pip install pre-commit
RUN pip install -r requirements.txt
RUN if [ -f base.cfg ] ; then \
    ln -s base.cfg buildout.cfg; \
	fi
RUN if [ -f bootstrap.py ]; then \
    python bootstrap.py; \
    fi
ENV PATH "$PATH:bin/"
RUN apt-get -y install rubygems
RUN apt-get -y install golang
ENV GOPATH=$HOME/go
ENV PATH=$PATH:$GOPATH/bin
RUN go get -u mvdan.cc/sh/cmd/shfmt
RUN apt-get -y install shellcheck
