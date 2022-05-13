#host = '192.168.1.104'

def test_release_file(host):
    release_file = host.file("/etc/os-release")
    assert release_file.contains('Ubuntu')
    assert release_file.contains('VERSION_ID="20.04"')

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.1")

def test_nginx_is_running(host):
    assert host.service('nginx').is_running
    assert host.service('nginx').is_enabled

def test_nginx_listens_on_port_80(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening

def test_docker_is_installed(host):
    docker = host.package("docker")
    assert docker.is_installed

def test_docker_is_running(host):
    assert host.service('docker').is_running
    assert host.service('docker').is_enabled

def test_grafana_listens_on_port_3000(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening

