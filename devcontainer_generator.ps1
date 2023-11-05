

$env_file = @'
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=localhost
'@

$devcontainer_json = @'
// For format details, see https://aka.ms/devcontainer.json. For config options, see the README at:
// https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/docker-from-docker-compose
{{
	"name": "{0}",
	"dockerComposeFile": "docker-compose.yml",
	"service": "app",
	"workspaceFolder": "/{1}",
	// "workspaceFolder": "/workspace/${{localWorkspaceFolderBasename}}",
	// Use this environment variable if you need to bind mount your local source code into a new container.
	// 不晓得咋用？
	// "remoteEnv": {{
	//     "LOCAL_WORKSPACE_FOLDER": "${{localWorkspaceFolder}}"
	// }},
	// Configure tool-specific properties.
	"customizations": {{
		// Configure properties specific to VS Code.
		"vscode": {{
			// Add the IDs of extensions you want installed when the container is created.
			"extensions": [
				// "asvetliakov.vscode-neovim",
				// "zhuangtongfa.material-theme",
				// "dracula-theme.theme-dracula",
				// "github.github-vscode-theme",
				// "pkief.material-icon-theme",
				"vscode-icons-team.vscode-icons",
				"ms-vscode-remote.vscode-remote-extensionpack",
				"ms-azuretools.vscode-docker",
				"jeff-hykin.better-dockerfile-syntax",
				"tomsaunders.vscode-workspace-explorer",
				// "hbenl.vscode-test-explorer",
				"johnpapa.vscode-peacock",
				// "folke.vscode-monorepo-workspace",
				"alefragnani.project-manager",
				"spmeesseman.vscode-taskexplorer",
				"donjayamanne.githistory",
				"eamodio.gitlens",
				"mhutchie.git-graph",
				"github.codespaces",
				"cschleiden.vscode-github-actions",
				"github.remotehub",
				"github.vscode-pull-request-github",
				"editorconfig.editorconfig",
				"shardulm94.trailing-spaces",
				"docsmsft.docs-yaml",
				"tamasfe.even-better-toml",
				"formulahendry.code-runner",
				"divyanshuagrawal.competitive-programming-helper",
				"leetcode.vscode-leetcode",
				"adpyke.codesnap",
				"evgeniypeshkov.syntax-highlighter",
				"aaron-bond.better-comments",
				"usernamehw.errorlens",
				"visualstudioexptteam.intellicode-api-usage-examples",
				"visualstudioexptteam.vscodeintellicode",
				"christian-kohler.path-intellisense",
				"streetsidesoftware.code-spell-checker",
				"gruntfuggly.todo-tree",
				"fabiospampinato.vscode-todo-plus",
				"kisstkondoros.vscode-gutter-preview",
				"buuug7.gbk2utf8",
				"ms-vscode.hexeditor",
				"bierner.color-info"
			],
			"settings": {{
				"workbench.trustedDomains.promptInTrustedWorkspace": true,
				"projectManager.git.baseFolders": [
					"~/code",
					"~/projects",
					"/workspace"
				],
				// "workbench.colorTheme": "One Dark Pro Darker",
				// "workbench.iconTheme": "material-icon-theme",
				"editor.fontSize": 14,
				"editor.fontFamily": "'Fira Code', 'Cascadia Code',Consolas, 'Courier New', monospace",
				"debug.console.fontFamily": "Hack Nerd Font",
				"terminal.integrated.fontFamily": "Hack Nerd Font",
				"editor.fontLigatures": true, // 是否启用字体连字
				"editor.fontWeight": "normal",
				"files.autoSave": "afterDelay",
				"files.autoGuessEncoding": true,
				"workbench.list.smoothScrolling": true,
				"editor.cursorSmoothCaretAnimation": "on",
				"editor.smoothScrolling": true,
				"editor.cursorBlinking": "smooth",
				"editor.mouseWheelZoom": true,
				"editor.formatOnPaste": true,
				"editor.formatOnType": true,
				"editor.formatOnSave": true,
				"editor.wordWrap": "on",
				"editor.guides.bracketPairs": true,
				"editor.suggest.snippetsPreventQuickSuggestions": false,
				"editor.acceptSuggestionOnEnter": "smart",
				"editor.suggestSelection": "recentlyUsed",
				"window.dialogStyle": "custom",
				"debug.showBreakpointsInOverviewRuler": true,
				"terminal.integrated.enableMultiLinePasteWarning": true,
				"todo-tree.tree.showScanModeButton": true,
				"todo-tree.filtering.excludeGlobs": [
					"**/node_modules",
					"*.xml",
					"*.XML"
				],
				"todo-tree.filtering.ignoreGitSubmodules": true,
				"todohighlight.keywords": [],
				"todo-tree.tree.showCountsInTree": true,
				"todohighlight.keywordsPattern": "TODO:|FIXME:|NOTE:|\\(([^)]+)\\)",
				"todohighlight.defaultStyle": {{}},
				"todohighlight.isEnable": true,
				"todo-tree.highlights.customHighlight": {{
					"BUG": {{
						"icon": "bug",
						"foreground": "#F56C6C",
						"type": "line",
						"gutterIcon": true
					}},
					"FIX": {{
						"icon": "flame",
						"foreground": "#FF9800",
						"type": "line",
						"gutterIcon": true
					}},
					"FIXIT": {{
						"icon": "flame",
						"foreground": "#FF9800",
						"type": "line",
						"gutterIcon": true
					}},
					"FIXME": {{
						"icon": "flame",
						"foreground": "#FF9800",
						"type": "line",
						"gutterIcon": true
					}},
					"TODO": {{
						"foreground": "#FFEB38",
						"type": "line",
						"gutterIcon": true
					}},
					"[] ": {{
						"foreground": "#FFEB38",
						"type": "line",
						"gutterIcon": true
					}},
					"[x] ": {{
						"foreground": "#FFEB38",
						"type": "line",
						"gutterIcon": true
					}},
					"- [] ": {{
						"foreground": "#FFEB38",
						"type": "line",
						"gutterIcon": true
					}},
					"- [x] ": {{
						"foreground": "#FFEB38",
						"type": "line",
						"gutterIcon": true
					}},
					"NOTE": {{
						"icon": "note",
						"foreground": "#67C23A",
						"type": "line",
						"gutterIcon": true
					}},
					"INFO": {{
						"icon": "info",
						"foreground": "#909399",
						"type": "line",
						"gutterIcon": true
					}},
					"TAG": {{
						"icon": "tag",
						"foreground": "#409EFF",
						"type": "line",
						"gutterIcon": true
					}},
					"HACK": {{
						"icon": "versions",
						"foreground": "#E040FB",
						"type": "line",
						"gutterIcon": true
					}},
					"XXX": {{
						"icon": "unverified",
						"foreground": "#E91E63",
						// "background": "#ffffff",
						"type": "line",
						"gutterIcon": true
					}}
				}},
				"todo-tree.general.tags": [
					"BUG",
					"HACK",
					"FIX",
					"FIXIT",
					"FIXME",
					"TODO",
					"[] ",
					"[x] ",
					"- [] ",
					"- [x] ",
					"INFO",
					"NOTE",
					"TAG",
					"XXX"
				],
				"todo-tree.general.tagGroups": {{
					"FIX": [
						"FIXME",
						"FIXIT",
						"FIX",
					],
					"TODO": [
						"TODO",
						"[] ",
						"[x] ",
						"- [] ",
						"- [x] ",
					]
				}},
				"todo-tree.general.statusBar": "tags",
				"todo-tree.regex.regexCaseSensitive": false,
				"todo-tree.general.enableFileWatcher": true,
				"todo-tree.general.showIconsInsteadOfTagsInStatusBar": true,
				"git.autofetch": true,
			}}
		}}
	}}
	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],
	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "docker --version",
	// Comment out to connect as root instead. More info: https://aka.ms/vscode-remote/containers/non-root.
	// "remoteUser": "vscode",
	// 安装总是卡住
	// "features": {{
	// 	"git": "latest",
	// 	"git-lfs": "latest",
	// 	"github-cli": "latest"
	// }}
}}
'@

$docker_compose_yml = @'
version: "3.9"

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        UPGRADE_PACKAGES: "true"
    # restart: always
    user: root
    # user: 1000:1000
    tty: true
    privileged: true
    # hostname: '192.168.1.4'
    # network_mode: bridge
    volumes:
      - '..:/{0}'
      # - /usr/bin/docker:/usr/bin/docker
      # - /var/run/docker.sock:/var/run/docker.sock
    # ports:
    #   - 80:80
    #   - 8181:3000
    # depends_on:
    #   - db




    # Overrides default command so things don't shut down after the process ends.
    # command: sleep infinity

    # Runs app on the same network as the database container, allows "forwardPorts" in devcontainer.json function.
    # network_mode: service:db

    # Use "forwardPorts" in **devcontainer.json** to forward an app port locally.
    # (Adding the "ports" property to this file will not forward from a Codespace.)

#   db:
#     image: postgres:latest
#     restart: unless-stopped
#     volumes:
#       - postgres-data:/var/lib/postgresql/data
#     env_file:
#         - .env

#     # Add "forwardPorts": ["5432"] to **devcontainer.json** to forward PostgreSQL locally.
#     # (Adding the "ports" property to this file will not forward from a Codespace.)

# volumes:
#   postgres-data:

'@

$dockerfile = @'
FROM {0}:{1}
LABEL maintainer="LGF"

USER root

RUN mkdir -p /root/code && mkdir -p /root/.ssh
COPY id_rsa* /root/.ssh/
RUN chmod 600 /root/.ssh/id_rsa && chmod 644 /root/.ssh/id_rsa.pub

WORKDIR /{2}


# [Optional] Uncomment this section to install additional OS packages.
RUN {3}



'@



function remove_dir ($path) {{
    if(Test-Path $path)
        {{
            remove-Item -Recurse -Force $path
            Write-Output "Directory $path Deleted Successfully!!!"
        }}
}}

function create_dir ($path) {{
    if ( Test-Path $path ) {{
        Write-Output "Directory $path Exists!!!"
    }} else {{
        # mkdir $path
        # New-Item -Path $path -ItemType Directory -Force
        New-Item -Path $path -ItemType Directory
        Write-Output "Directory $path Created Successfully!!!"
    }}
}}

# $devcontainer_path = ".devcontainer"
# create_dir($devcontainer_path)
# Write-Output "$env_file" | Out-File -Encoding default -FilePath "$devcontainer_path/.env"
# Write-Output "$devcontainer_json" | Out-File -Encoding default -FilePath "$devcontainer_path/devcontainer.json"
# Write-Output "$docker_compose_yml" | Out-File -Encoding default -FilePath "$devcontainer_path/docker-compose.yml"
# Write-Output "$dockerfile" | Out-File -Encoding default -FilePath "$devcontainer_path/Dockerfile"

function docker_env ($docker_image = "debian", $docker_image_version = "latest") {
	$image = "lgf4591/debian".replace("lgf4591/","")
	$arch_like = @("archlinux","majaro")
	$alpine_like = @("alpine")
	$debian_like = @("debian","ubuntu","node")
	$fedora_like = @("fedora","centos","almalinux","oraclelinux","rockylinux","redhat")
	$install_additional_command = "echo 'install additional packages'"
	$devcontainer_path = ".devcontainer"
	$workdir = "root/code"
	Copy-Item -Path ~/.ssh/id_rsa -Destination $devcontainer_path/ -Force
	Copy-Item -Path ~/.ssh/id_rsa.pub -Destination $devcontainer_path/ -Force
	if ($docker_image.contains("lgf4591/")){
		$workdir = "workspace"
	}
	if ($image -in $arch_like){
		$install_additional_command = "pacman -Syyu && export DEBIAN_FRONTEND=noninteractive && pacman -Syy --noprogressbar --noconfirm --needed sudo ca-certificates git openssh-server net-tools curl wget vim nano"
	} elseif ($image -in $alpine_like){
		$install_additional_command = "apk update && export DEBIAN_FRONTEND=noninteractive && apk add --no-cache -U git openssh-server net-tools curl wget busybox-extras vim nano"
	} elseif ($image -in $debian_like){
		$install_additional_command = "apt-get update && export DEBIAN_FRONTEND=noninteractive && apt-get -y install --no-install-recommends git openssh-server net-tools curl wget vim nano"
	} elseif ($image -in $fedora_like){
		$install_additional_command = "dnf update && export DEBIAN_FRONTEND=noninteractive && dnf -y install git openssh-server net-tools curl wget vim nano"
	}
	$final_dockerfile = "$dockerfile" -f $docker_image, $docker_image_version, $workdir, $install_additional_command, $ssh_id_rsa, $ssh_id_rsa_pub
	Write-Output "$final_dockerfile" | Out-File -Encoding default -FilePath "$devcontainer_path/Dockerfile" -Force
	# Write-Output $final_dockerfile
	$final_docker_compose_yml = "$docker_compose_yml" -f $workdir
	Write-Output "$final_docker_compose_yml" | Out-File -Encoding default -FilePath "$devcontainer_path/docker-compose.yml" -Force
	$final_devcontainer_json = "$devcontainer_json" -f $docker_image, $workdir
	Write-Output "$final_devcontainer_json" | Out-File -Encoding default -FilePath "$devcontainer_path/devcontainer.json" -Force
	$final_env_file = $env_file
	Write-Output "$final_env_file" | Out-File -Encoding default -FilePath "$devcontainer_path/.env" -Force

}

docker_env
# docker_env "lgf4591/debian"


