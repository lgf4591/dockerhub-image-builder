
import os

devcontainer_image_info_map = {
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
    "java": ["latest"],
    "node": ["latest"],
    "python": ["latest"],
    "R": ["latest"],
    "julia": ["latest"],
    "rust": ["latest"]
}


devcontainer_image_info_test_map = {
    "debian": [
                {
                    "version": "latest",
                    "pkg_mgt": " apt-get ",
                    "need_install_pks": " curl wget bash zsh fish tmux git "
                }
            ],
    "alpine": [
                {
                    "version": "3.15",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " curl wget bash zsh fish tmux git "
                },
                {
                    "version": "3.16",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " curl wget bash zsh fish tmux git "
                },
                {
                    "version": "3.17",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " curl wget bash zsh fish tmux git "
                },
                {
                    "version": "3.18",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " curl wget bash zsh fish tmux git "
                },
                {
                    "version": "latest",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " curl wget bash zsh fish tmux git "
                }
            ]
}


build_sh_template = """
#! /bin/sh
# install oh-my-bash

bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"

# install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# install oh-my-fish
curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish


# special steps for each image
echo "will finish special steps for {} image next!!!"


"""

dockerfile_template = """
FROM {}:{}
LABEL maintainer="lgf4591@outlook.com"
RUN mkdir -p /workspace
COPY build.sh /workspace
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

for (image_name,image_infos) in devcontainer_image_info_test_map.items():
    folder = f"devcontainer/{image_name}"
    folder_is_existed = os.path.exists(folder)
    if not folder_is_existed:
        os.makedirs(folder)
        print(f"created {folder} folder successfully!!!")
    else:
        print(f"{folder} folder is existed!!!")
    for image_info in image_infos:
        image_version = image_info["version"]
        pkg_mgt = image_info["pkg_mgt"]
        need_install_pks = image_info["need_install_pks"]
        install_pkg_verb = "add" if ("alpine" in image_name or "alpine" in image_version) else "install -y"
        dockerfile_content = dockerfile_template.format(image_name, image_version, pkg_mgt, pkg_mgt, install_pkg_verb, need_install_pks)
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
    

