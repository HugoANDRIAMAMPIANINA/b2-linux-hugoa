# TP1 : Premiers pas avec Docker

# I. Init

- [TP1 : Premiers pas avec Docker](#tp1--premiers-pas-avec-docker)
- [I. Init](#i-init)
  - [3. sudo c pa bo](#3-sudo-c-pa-bo)
  - [4. Un premier conteneur en vif](#4-un-premier-conteneur-en-vif)
  - [5. Un deuxième conteneur en vif](#5-un-deuxième-conteneur-en-vif)
- [II. Images](#ii-images)
  - [1. Images publiques](#1-images-publiques)
  - [2. Construire une image](#2-construire-une-image)
- [III. Docker compose](#iii-docker-compose)

## 3. sudo c pa bo

🌞 **Ajouter votre utilisateur au groupe `docker`**

```bash
[hugoa@docker ~]$ sudo usermod -aG docker $(whoami)
```

## 4. Un premier conteneur en vif

🌞 **Lancer un conteneur NGINX**

```bash
[hugoa@docker ~]$ docker run -d -p 9999:80 nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
af107e978371: Pull complete
336ba1f05c3e: Pull complete
8c37d2ff6efa: Pull complete
51d6357098de: Pull complete
782f1ecce57d: Pull complete
5e99d351b073: Pull complete
7b73345df136: Pull complete
Digest: sha256:bd30b8d47b230de52431cc71c5cce149b8d5d4c87c204902acf2504435d4b4c9
Status: Downloaded newer image for nginx:latest
06e93e51825edfc74c6b7cbc59f1bc7911147a2fb0ef846b6daab96c7becfb0b
```

🌞 **Visitons**

- vérifier que le conteneur est actif avec une commande qui liste les conteneurs en cours de fonctionnement
```bash
[hugoa@docker ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
06e93e51825e   nginx     "/docker-entrypoint.…"   57 seconds ago   Up 56 seconds   0.0.0.0:9999->80/tcp, :::9999->80/tcp   hungry_sammet
```
- afficher les logs du conteneur
```bash
[hugoa@docker ~]$ docker logs hungry_sammet
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/12/21 09:36:48 [notice] 1#1: using the "epoll" event method
2023/12/21 09:36:48 [notice] 1#1: nginx/1.25.3
2023/12/21 09:36:48 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
2023/12/21 09:36:48 [notice] 1#1: OS: Linux 5.14.0-362.13.1.el9_3.x86_64
2023/12/21 09:36:48 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1073741816:1073741816
2023/12/21 09:36:48 [notice] 1#1: start worker processes
2023/12/21 09:36:48 [notice] 1#1: start worker process 28
```
- afficher toutes les informations relatives au conteneur avec une commande `docker inspect`
```bash
[hugoa@docker ~]$ docker inspect --type=container hungry_sammet
[
    {
        "Id": "06e93e51825edfc74c6b7cbc59f1bc7911147a2fb0ef846b6daab96c7becfb0b",
        "Created": "2023-12-21T09:36:47.55135866Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 4365,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-12-21T09:36:48.366090491Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:d453dd892d9357f3559b967478ae9cbc417b52de66b53142f6c16c8a275486b9",
        "ResolvConfPath": "/var/lib/docker/containers/06e93e51825edfc74c6b7cbc59f1bc7911147a2fb0ef846b6daab96c7becfb0b/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/06e93e51825edfc74c6b7cbc59f1bc7911147a2fb0ef846b6daab96c7becfb0b/hostname",
        "HostsPath": "/var/lib/docker/containers/06e93e51825edfc74c6b7cbc59f1bc7911147a2fb0ef846b6daab96c7becfb0b/hosts",
        "LogPath": "/var/lib/docker/containers/06e93e51825edfc74c6b7cbc59f1bc7911147a2fb0ef846b6daab96c7becfb0b/06e93e51825edfc74c6b7cbc59f1bc7911147a2fb0ef846b6daab96c7becfb0b-json.log",
        "Name": "/hungry_sammet",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "9999"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                51,
                102
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/60e4fa2fd073f4329b117a74f13ba28be74516ae879b05a172ee6d3bf149e427-init/diff:/var/lib/docker/overlay2/5b592336f49dd148c35052479776d3a0a5eca4f90a185e2a0c638059f38e29a0/diff:/var/lib/docker/overlay2/1165f560c2b921b63aa736a87fe365858e1b61e4cd4b7e5d409ac960d959ddbc/diff:/var/lib/docker/overlay2/ee74536d0559645b7aec990c2bdad859ec4f13b67f31506eaee7c57065311b29/diff:/var/lib/docker/overlay2/f1c0e98a3a250e64a7696f6fa80276566c3e7f98591a51e793664a57e1ba06ce/diff:/var/lib/docker/overlay2/89d477ebd8f2447fa9fa2fd1b2b27b3bb57d01742726258271edb5c7a2235f79/diff:/var/lib/docker/overlay2/8bf75b3af9c11f9a8093033d573bace94f7cb77119279b23c5fc6a9110f076df/diff:/var/lib/docker/overlay2/fb977dde62d08c52bc91bac68bd5b7e23c3e28a95c8b09163b764823db392773/diff",
                "MergedDir": "/var/lib/docker/overlay2/60e4fa2fd073f4329b117a74f13ba28be74516ae879b05a172ee6d3bf149e427/merged",
                "UpperDir": "/var/lib/docker/overlay2/60e4fa2fd073f4329b117a74f13ba28be74516ae879b05a172ee6d3bf149e427/diff",
                "WorkDir": "/var/lib/docker/overlay2/60e4fa2fd073f4329b117a74f13ba28be74516ae879b05a172ee6d3bf149e427/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "06e93e51825e",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.3",
                "NJS_VERSION=0.8.2",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "30a2624b1800f008d116e13e280a1f5ff37f57413e41281f1575d367a4d6df2c",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "9999"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "9999"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/30a2624b1800",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "176043d40012452eb4c15300609bfa1567d5f90861635a445509f79f8af82d76",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "eee8a352902bfbc47ce44435cd94cc2fac39f046e4151073376f5671e4fefc66",
                    "EndpointID": "176043d40012452eb4c15300609bfa1567d5f90861635a445509f79f8af82d76",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```
- afficher le port en écoute sur la VM avec un `sudo ss -lnpt`
```bash
[hugoa@docker ~]$ sudo ss -lnpt | grep docker
LISTEN 0      4096         0.0.0.0:9999      0.0.0.0:*    users:(("docker-proxy",pid=4321,fd=4))
LISTEN 0      4096            [::]:9999         [::]:*    users:(("docker-proxy",pid=4326,fd=4))
```
- ouvrir le port `9999/tcp` (vu dans le `ss` au dessus normalement) dans le firewall de la VM
```bash
[hugoa@docker ~]$ sudo firewall-cmd --add-port=9999/tcp --permanent
success
[hugoa@docker ~]$ sudo firewall-cmd --reload
success
[hugoa@docker ~]$ sudo firewall-cmd --list-all | grep 9999
  ports: 9999/tcp
```
- depuis le navigateur de votre PC, visiter le site web sur `http://IP_VM:9999`
```powershell
PS C:\Users\hugoa> curl 10.1.1.13:9999


StatusCode        : 200
StatusDescription : OK
Content           : <!DOCTYPE html>
                    <html>
                    <head>
                    <title>Welcome to nginx!</title>
                    <style>
                    html { color-scheme: light dark; }
                    body { width: 35em; margin: 0 auto;
                    font-family: Tahoma, Verdana, Arial, sans-serif; }
                    </style...
RawContent        : HTTP/1.1 200 OK
                    Connection: keep-alive
                    Accept-Ranges: bytes
                    Content-Length: 615
                    Content-Type: text/html
                    Date: Thu, 21 Dec 2023 09:49:23 GMT
                    ETag: "6537cac7-267"
                    Last-Modified: Tue, 24 Oct 2023 ...
Forms             : {}
Headers           : {[Connection, keep-alive], [Accept-Ranges, bytes], [Content-Length, 615], [Content-Type,
                    text/html]...}
Images            : {}
InputFields       : {}
Links             : {@{innerHTML=nginx.org; innerText=nginx.org; outerHTML=<A href="http://nginx.org/">nginx.org</A>;
                    outerText=nginx.org; tagName=A; href=http://nginx.org/}, @{innerHTML=nginx.com;
                    innerText=nginx.com; outerHTML=<A href="http://nginx.com/">nginx.com</A>; outerText=nginx.com;
                    tagName=A; href=http://nginx.com/}}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 615
```

🌞 **On va ajouter un site Web au conteneur NGINX**

```bash
[hugoa@docker nginx]$ docker run -d -p 9999:8080 -v /home/hugoa/nginx/index.html:/var/www/html/index.html -v /home/hugoa/nginx/site_nul.conf:/etc/nginx/conf.d/site_nul.conf nginx
bccf8c11c607442e8214cb62fc3952adde194fa62dc6c2fe474dacf09ccf4d29
```

🌞 **Visitons**

- vérifier que le conteneur est actif
```bash
[hugoa@docker nginx]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                               NAMES
bccf8c11c607   nginx     "/docker-entrypoint.…"   30 seconds ago   Up 29 seconds   80/tcp, 0.0.0.0:9999->8080/tcp, :::9999->8080/tcp   funny_proskuriakova
```

- visiter le site web depuis votre PC
```powershell
PS C:\Users\hugoa> curl 10.1.1.13:9999


StatusCode        : 200
StatusDescription : OK
Content           : <h1>MEOOOW</h1>

RawContent        : HTTP/1.1 200 OK
                    Connection: keep-alive
                    Accept-Ranges: bytes
                    Content-Length: 16
                    Content-Type: text/html
                    Date: Thu, 21 Dec 2023 10:20:38 GMT
                    ETag: "65840bbb-10"
                    Last-Modified: Thu, 21 Dec 2023 09...
Forms             : {}
Headers           : {[Connection, keep-alive], [Accept-Ranges, bytes], [Content-Length, 16], [Content-Type, text/html]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 16
```

## 5. Un deuxième conteneur en vif

🌞 **Lance un conteneur Python, avec un shell**

```bash
[hugoa@docker nginx]$ docker run -it python bash
Unable to find image 'python:latest' locally
latest: Pulling from library/python
bc0734b949dc: Pull complete
b5de22c0f5cd: Pull complete
917ee5330e73: Pull complete
b43bd898d5fb: Pull complete
7fad4bffde24: Pull complete
d685eb68699f: Pull complete
107007f161d0: Pull complete
02b85463d724: Pull complete
Digest: sha256:3733015cdd1bd7d9a0b9fe21a925b608de82131aa4f3d397e465a1fcb545d36f
Status: Downloaded newer image for python:latest
root@99b532c37a55:/# python --version
Python 3.12.1
```

🌞 **Installe des libs Python**

```
root@99b532c37a55:/# pip install aiohttp aioconsole
root@99b532c37a55:/# python
Python 3.12.1 (main, Dec 19 2023, 20:14:15) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import aiohttp
>>>
```

# II. Images

## 1. Images publiques

🌞 **Récupérez des images**

- avec la commande `docker pull`
- récupérez :
```bash
[hugoa@docker ~]$ docker pull python:3.11
[hugoa@docker ~]$ docker pull mysql:5.7
[hugoa@docker ~]$ docker pull wordpress:latest
[hugoa@docker ~]$ docker pull linuxserver/wikijs
```
- listez les images que vous avez sur la machine avec une commande `docker`
```bash
[hugoa@docker ~]$ docker image ls
REPOSITORY           TAG       IMAGE ID       CREATED       SIZE
linuxserver/wikijs   latest    869729f6d3c5   5 days ago    441MB
mysql                5.7       5107333e08a8   8 days ago    501MB
python               latest    fc7a60e86bae   13 days ago   1.02GB
wordpress            latest    fd2f5a0c6fba   2 weeks ago   739MB
python               3.11      22140cbb3b0c   2 weeks ago   1.01GB
nginx                latest    d453dd892d93   8 weeks ago   187MB
```

🌞 **Lancez un conteneur à partir de l'image Python**

```bash
[hugoa@docker ~]$ docker run -it python:3.11 bash
root@d91a8e88ad69:/# python --version
Python 3.11.7
```

## 2. Construire une image

🌞 **Ecrire un Dockerfile pour une image qui héberge une application Python**

[Dockerfile](python_app_build/Dockerfile)

🌞 **Build l'image**



🌞 **Lancer l'image**

- lance l'image avec `docker run` :

```bash
docker run python_app:version_de_ouf
```
# III. Docker compose

🌞 **Lancez les deux conteneurs** avec `docker compose`

```
[hugoa@docker compose_test]$ docker compose up -d
[+] Running 3/3
 ✔ Network compose_test_default                  Cre...                                0.7s
 ✔ Container compose_test-conteneur_nul-1        Started                               0.1s
 ✔ Container compose_test-conteneur_flopesque-1  Started                               0.1s
```

🌞 **Vérifier que les deux conteneurs tournent**

```
[hugoa@docker compose_test]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                               NAMES
0384b66604cf   debian    "sleep 9999"             12 seconds ago   Up 11 seconds                                                       compose_test-conteneur_nul-1
0bba2e89ef28   debian    "sleep 9999"             12 seconds ago   Up 10 seconds                                                       compose_test-conteneur_flopesque-1
```

🌞 **Pop un shell dans le conteneur `conteneur_nul`**

```
[hugoa@docker compose_test]$ docker exec -it compose_test-conteneur_nul-1 bash
root@0384b66604cf:/# apt update -y
root@0384b66604cf:/# apt install iputils-ping -y
root@0384b66604cf:/# ping compose_test-conteneur_flopesque-1
PING compose_test-conteneur_flopesque-1 (172.18.0.3) 56(84) bytes of data.
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.3): icmp_seq=1 ttl=64 time=0.113 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.3): icmp_seq=2 ttl=64 time=0.211 ms
```