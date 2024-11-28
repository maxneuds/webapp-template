FROM python:3.12.7-bookworm

# Update pip and install poetry
RUN pip install --upgrade pip
RUN pip install poetry

# <- MongoDB ->
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*
# <- MongoDB ->

# <- DEVCONTAINER ->
# Install zsh and other useful packages
RUN apt-get update && apt-get install -y \
    git wget curl unzip rsync zsh htop vim neofetch \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install oh-my-zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)" "" --unattended
# enable command completion and git support in zsh
RUN git clone https://github.com/zsh-users/zsh-completions ~/.oh-my-zsh/custom/plugins/zsh-completions
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
RUN sed -i 's/plugins=(git)/plugins=(git zsh-completions zsh-syntax-highlighting zsh-autosuggestions)/' ~/.zshrc
RUN sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="agnoster"/' ~/.zshrc
RUN echo 'prompt_context() {}' >> ~/.zshrc
# Command alias
RUN echo 'alias ll="ls -lah --color=auto"' >> ~/.zshrc
RUN echo 'alias cp="rsync -avh --progress"' >> ~/.zshrc
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
# Install aws tools
RUN pip install awscli
# <- DEVCONTAINER ->

# Set environment variables for poetry
ENV POETRY_VIRTUALENVS_CREATE=true
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1

# Set working directory
WORKDIR /workspace/dev

