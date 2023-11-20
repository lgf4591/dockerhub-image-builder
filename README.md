# dockerhub-image-builder
dockerhub-image-builder

## TEST
```bash

docker run --rm -it lgf4591/debian:latest zsh

CR_PAT=XXXX
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
docker run --rm -it ghcr.io/lgf4591/alpine:latest zsh

```

## [devcontainers templates](https://github.com/devcontainers/templates)


## [oh-my-bash](https://github.com/ohmybash/oh-my-bash)

```bash

bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
bash -c "$(wget https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh -O -)"

```

## [oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh)
```bash

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

```

## [oh-my-fish](https://github.com/oh-my-fish/oh-my-fish)
```bash

curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish

```


## [oh-my-tmux](https://github.com/gpakosz/.tmux)
```bash

cd
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .

```
