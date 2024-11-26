FROM ghcr.io/oracle/oraclelinux8-instantclient:21 AS oracle_client

FROM python:3.12.7-bookworm

# <-- ORACLE DB -->
# copy Oracle Instant Client files from the oracle instant client image
COPY --from=oracle_client /usr/lib/oracle /usr/lib/oracle
RUN apt-get update && apt-get install -y \
    libaio1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN ldconfig
# <-- ORACLE DB -->

# <-- DEVCONTAINER -->
# The following is a list of packages that are installed in the devcontainer
# Install zsh and other necessary packages
RUN apt-get update && apt-get install -y \
    git wget curl unzip rsync zsh htop vim neofetch \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# Install Docker
ARG docker_gid=999
RUN groupadd -g ${docker_gid} docker
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# <-- DEVCONTAINER -->

# update pip and install poetry
RUN pip install --upgrade pip
RUN pip install poetry

# create user "worker" and set zsh as the default shell
ARG user=worker
ARG group=worker
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -m -s /bin/zsh ${user}
RUN mkdir /workspace
RUN chown worker:worker /workspace

# <-- DEVCONTAINER -->
# add user to the docker group
RUN usermod -aG docker worker
# <-- DEVCONTAINER -->

USER worker
WORKDIR /workspace

# <-- DEVCONTAINER -->
# install python devtools
RUN pip install awscli
# install oh-my-zsh for the "worker" user
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)" "" --unattended
# enable command completion and git support in zsh
RUN git clone https://github.com/zsh-users/zsh-completions ~/.oh-my-zsh/custom/plugins/zsh-completions
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
RUN sed -i 's/plugins=(git)/plugins=(git zsh-completions zsh-syntax-highlighting zsh-autosuggestions)/' ~/.zshrc
RUN sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="agnoster"/' ~/.zshrc
RUN echo 'prompt_context() {}' >> ~/.zshrc
# command alias
RUN echo 'alias ll="ls -lah --color=auto"' >> ~/.zshrc
RUN echo 'alias cp="rsync -avh --progress"' >> ~/.zshrc
# <-- DEVCONTAINER -->

# <-- ORACLE DB -->
# set environment variables for Oracle Instant Client
ENV LD_LIBRARY_PATH=/usr/lib/oracle/21/client64/lib
ENV PATH=$PATH:/usr/lib/oracle/21/client64/bin
# <-- ORACLE DB -->

# set environment variables for poetry
ENV POETRY_VIRTUALENVS_CREATE=true
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1


