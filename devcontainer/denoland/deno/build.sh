
#! /bin/sh
# install oh-my-bash

bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"


# install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-completions ~/.oh-my-zsh/custom/plugins/zsh-completions
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k
git clone https://github.com/paulirish/git-open.git ~/.oh-my-zsh/custom/plugins/git-open
sed -i 's/^plugins=(/plugins=(docker docker-compose python npm zsh-autosuggestions zsh-syntax-highlighting z /' ~/.zshrc
sed -i 's/^ZSH_THEME="robbyrussell"/ZSH_THEME="juanghurtado"/' ~/.zshrc


# install oh-my-fish
# BUG: Install aborted: Running interactively, but can't read from tty (try running with --noninteractive)
# curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish
git clone https://github.com/oh-my-fish/oh-my-fish.git  && ./oh-my-fish/bin/install --offline --noninteractive && rm -rf ./oh-my-fish


# install oh-my-tmux
cd
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .


# special steps for each image
echo "will finish special steps for denoland/deno image next!!!"


