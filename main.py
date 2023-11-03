
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
                    "need_install_pks": " zsh tmux "
                }
            ],
    "alpine": [
                {
                    "version": "3.15",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " zsh tmux "
                },
                {
                    "version": "3.16",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " zsh tmux "
                },
                {
                    "version": "3.17",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " zsh tmux "
                },
                {
                    "version": "3.18",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " zsh tmux "
                },
                {
                    "version": "latest",
                    "pkg_mgt": " apk ",
                    "need_install_pks": " zsh tmux "
                }
            ]
}



dockerfile_template = """
FROM {}:{}
LABEL maintainer="lgf4591@outlook.com"
RUN mkdir -p /workspace
RUN {} update && export DEBIAN_FRONTEND=noninteractive \
    && {} {} -y {}
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
        install_pkg_verb = "add" if ("alpine" in image_name or "alpine" in image_version) else "install"
        dockerfile_content = dockerfile_template.format(image_name, image_version, pkg_mgt, pkg_mgt, install_pkg_verb, need_install_pks)
        print(dockerfile_content)
        with open(f"{folder}/Dockerfile.build-{image_version}", "w") as dockerfile:
            dockerfile.write(dockerfile_content)
    print(f"create {image_name} github actions file")
    

