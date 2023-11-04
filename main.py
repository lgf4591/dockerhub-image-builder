
import os

devcontainer_images_map = {
    "alpine": [
                {
                    "version": "3.15",
                    "pkg_mgt": " apt-get ",
                    "need_install_pks": " zsh tmux "
                }
            ],
    "debian": ["10.6","11.5","11.6","latest"],
    "fedora": ["latest"],
    "ubuntu": ["14.04","16.04","18.04","20.04","22.04","latest"],
    "dotnet": ["latest"],
    "golang": ["latest"],
    "openjdk": ["latest"],
    "node": ["latest"],
    "python": ["latest"],
    "julia": ["latest"],
    "rust": ["latest"]
}


devcontainer_images_need_to_build_map = {
    "alpine": {
                "common_need_install_pkgs": " curl wget ca-certificates bash zsh tmux tcsh lsof procps git openssh-server net-tools vim make cmake automake busybox-extras build-base zlib-dev openssl-dev ",
                "pkg_mgt": " apk ",
                "change_mirrir_command": "cp /etc/apk/repositories /etc/apk/repositories.bak && sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories",
                "image_info_dict": 
                    [
                        {
                            "version": "latest",
                            "special_need_install_pkgs": " fish neovim nano emacs fzf bat nnn ranger "
                        }
                    ]
            },
    "debian": {
                "common_need_install_pkgs": " curl wget ca-certificates apt-transport-https ntp bash zsh tmux csh tcsh ksh telnet iputils-ping lsof procps git openssh-server net-tools vim make cmake automake ",
                "pkg_mgt": " apt-get ",
                "change_mirrir_command": "cp /etc/apt/sources.list /etc/apt/sources.list.bak && sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list ",
                "image_info_dict": 
                    [
                        {
                            "version": "11",
                            "special_need_install_pkgs": " axel aria2 fish neovim nano emacs fzf fd-find bat nnn ranger autojump "
                        }
                    ]
            },
}


build_sh_template = """
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
echo "will finish special steps for {} image next!!!"


"""

dockerfile_template = """
FROM {}:{}
LABEL maintainer="lgf4591@outlook.com"

USER root
WORKDIR /root

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo '$TZ' > /etc/timezone

RUN {}

RUN mkdir -p /workspace
COPY ./devcontainer/{}/build.sh /workspace
RUN {} update && export DEBIAN_FRONTEND=noninteractive \
    && {} {} {}
RUN sh /workspace/build.sh
"""

github_cicd_template = """
name: {}:{} Docker Image CI/CD
on:
  push:
    branches: [ main ]
    paths:   # 这里是用来指定哪个文件更改，才会触发的
      - 'devcontainer/{}/Dockerfile.build-{}'               # 包括路径
      - 'devcontainer/{}/build.sh'                               # 包括路径
      - '!docs/**'                                                  # 排除路径
jobs:
  # 构建并上传 Docker镜像
  build: 
    runs-on: ubuntu-latest # 依赖的环境      
    steps:
      - uses: actions/checkout@v2
      - name: Build Image
        run: |
          docker build -t lgf4591/{}:{} -f devcontainer/{}/Dockerfile.build-{} .
      - name: Login to Registry
        # run: docker login --username=${{ secrets.DOCKER_USERNAME }} --password ${{ secrets.DOCKER_PASSWORD }}
        run: echo '${{ secrets.DOCKER_PASSWORD }}' | docker login --username ${{ secrets.DOCKER_USERNAME }}  --password-stdin
      - name: Push Image
        run: |
          docker push lgf4591/{}:{}
"""

# print(devcontainer_image_version_map["ubuntu"])

for (image_name,image_infos) in devcontainer_images_need_to_build_map.items():
    folder = f"devcontainer/{image_name}"
    folder_is_existed = os.path.exists(folder)
    if not folder_is_existed:
        os.makedirs(folder)
        print(f"created {folder} folder successfully!!!")
    else:
        print(f"{folder} folder is existed!!!")
    
    common_need_install_pkgs = devcontainer_images_need_to_build_map[image_name]["common_need_install_pkgs"]
    pkg_mgt = devcontainer_images_need_to_build_map[image_name]["pkg_mgt"]
    change_mirrir_command = devcontainer_images_need_to_build_map[image_name]["change_mirrir_command"]
    image_infos = devcontainer_images_need_to_build_map[image_name]["image_info_dict"]
    for image_info in image_infos:
        image_version = image_info["version"]
        special_need_install_pkgs = image_info["special_need_install_pkgs"]
        need_install_pks = common_need_install_pkgs + special_need_install_pkgs
        install_pkg_verb = "add --no-cache -U" if ("alpine" in image_name or "alpine" in image_version) else "install -y"
        dockerfile_content = dockerfile_template.format(image_name, image_version, change_mirrir_command, image_name, pkg_mgt, pkg_mgt, install_pkg_verb, need_install_pks)
        # print(dockerfile_content)
        with open(f"{folder}/Dockerfile.build-{image_version}", "w", encoding='utf-8') as dockerfile:
            dockerfile.write(dockerfile_content)
            
        github_cicd_content = github_cicd_template.format(image_name, image_version, image_name, image_version, image_name, image_name, image_version, image_name, image_version, image_name, image_version).replace("{ secrets.DOCKER_PASSWORD }",r"{{ secrets.DOCKER_PASSWORD }}").replace("{ secrets.DOCKER_USERNAME }", r"{{ secrets.DOCKER_USERNAME }}")
        with open(f".github/workflows/{image_name}_{image_version}.yml", "w", encoding='utf-8') as yamlfile:
            yamlfile.write(github_cicd_content)
    # print(f"create {image_name} github actions file")
    build_sh_content = build_sh_template.format(image_name)
    with open(f"{folder}/build.sh", "w", encoding='utf-8') as build_file:
            build_file.write(build_sh_content)
    

