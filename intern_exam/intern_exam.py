# # Test 1 - NETWORK
def test1_network_configuration(host):
    assert "10.10.120." in host.interface("eth0").addresses[0]
    assert "192.168.31." in host.interface("eth1").addresses[0]

    cmd = host.run('ip r s | grep "10.10.120.3" -q')
    assert cmd.rc == 0

# Test 2 - Hostname, resolv.conf
def test2_hostname_and_resolv(host):
    hostname = host.sysctl("kernel.hostname")
    assert "server-exam.example.com" == hostname

    resolv = host.file("/etc/resolv.conf")
    assert resolv.contains("search.*example.com")

# Test 3 - YUM
def test3_host_yum_repos(host):
    cmd = host.run('yum repolist |xargs | grep -qE ".*internal-base.*internal-updates.*$"')
    assert cmd.rc == 0


# Test 4 - SWAP
def test4_lvm_swap(host):
    pkg = host.package("lvm2")
    assert pkg.is_installed

    fstab = host.file("/etc/fstab")
    assert fstab.contains("swap")

    cmd = host.run("[ 250000 -lt $(swapon -s | grep partition | awk '{print $3}') ]")
    assert cmd.rc ==0

# Test 5 - mount of /results
def test5_mount_lvm_results(host):
    assert host.mount_point('/results').exists
    assert host.mount_point('/results').filesystem == 'xfs'
    assert "noexec" in host.mount_point('/results').options

    fstab = host.file("/etc/fstab")
    assert fstab.contains("LABEL.*/results")


    cmd = host.run("[ 480 -lt $(df -m /results | tail -1 | awk '{print $2}') ]")
    assert cmd.rc == 0

# Test 6 - RPMs
def test6_rpm_packages(host):
    assert not host.package("postfix").is_installed
    assert host.package("lsscsi").is_installed

# Test 7 - rsyslog
def test7_rsyslog(host):
    cmd = host.run("logger -p local6.error super_puper_test && grep -q super_puper_test /var/log/local6.log")
    assert cmd.rc == 0

# Test 8 - users
def test8_users(host):
    user_linda = host.user("linda")
    user_lisa = host.user("lisa")
    assert user_linda.uid == 2001
    assert user_linda.gid == 12001
    assert user_lisa.uid == 2002
    assert user_lisa.gid == 12001
    assert 12002 in user_lisa.gids

# Test 9 - chage
def test9_chage(host):
    cmd_lisa = host.run('chage -l lisa | grep "Password expires" | grep -q "password must be changed"')
    cmd_linda_date = host.run('chage -l linda | grep -q "$(date -d "+45 days" "+%b %d")"')

    assert cmd_lisa.rc == 0
    assert cmd_linda_date.rc == 0

# Test 10 - permissions,sgid
def test10_sgid(host):
    folder = host.file("/results/sharedfolder")
    assert folder.exists
    assert folder.is_directory
    assert folder.group == "developers"
    assert folder.mode == 1528 # It is 2770 in decimial

# Test 11 - FACL
def test11_facl(host):
    cmd_acl = host.run('getfacl /results/lindafolder/ | grep -qE "^user:linda:rwx"')
    cmd_default_acl = host.run('getfacl /results/lindafolder/ | grep -q "default:user:linda:rwx"')

    assert cmd_acl.rc == 0
    assert cmd_default_acl.rc == 0

# Test 12 - CRON
def test12_cron(host):
    assert host.file("/results/reports/freespace.log").exists
    assert host.file("/var/spool/cron/linda").exists
    assert host.file("/var/spool/cron/linda").contains("^\*/30.*\*.*\*.*\*.*\*")

# Test 13 - systemctl
def test13_systemctl(host):
    cmd = host.run('systemctl get-default | grep -q graphical')
    assert cmd.rc == 0
    assert not host.service("tuned").is_running
    assert not host.service("tuned").is_enabled

# Test 14 - TAR
def test14_tar(host):
    cmd = host.run('diff <(find /etc -name *\.conf -type f -exec ls {} \; | wc -l ) <(tar tf /results/etcbackup.tar | wc -l)')
    assert cmd.rc == 0

# Test 15 - FIND
def test15_find(host):
    cmd = host.run('diff <(find /usr -perm 4755 | sort | cut -f4 -d "/" | wc -l) <(cat /results/permissions.log| wc -l)')
    assert cmd.rc == 0

# Test 16 - find,grep
def test16_find_grep(host):
    cmd = host.run('diff <(find /usr/lib/systemd/system -type f -name *\.service | grep -v "-" | grep -v "@" | wc -l) <(cat /results/services.txt)')
    assert cmd.rc == 0

# Test 17 - sudo
def test17_sudo(host):
    cmd_sudo = host.run('grep -qE "^.*%ops.*NOPASSWD\s*:\s*ALL" /etc/sudoers')
    cmd_sudo_bob = host.run('sudo -U bob -l | xargs | grep -qE "(ALL|NOPASSWD).*ALL"')
    assert cmd_sudo.rc == 0
    assert cmd_sudo_bob.rc == 0

