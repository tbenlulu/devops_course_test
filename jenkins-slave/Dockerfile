FROM dluc/ubuntu-java-sshd

RUN apt-get update && \
    adduser --quiet jenkins && \
    echo "jenkins:jenkins" | chpasswd  && \
    echo "root:password" | chpasswd  && \
    apt-get install -y \ 
	git && \
    curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.05.0-ce.tgz && \
    tar --strip-components=1 -xvzf docker-17.05.0-ce.tgz -C /usr/local/bin

