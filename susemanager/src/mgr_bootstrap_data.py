#
# DO NOT EDIT !!!
#

PKGLIST10 = [
                "libaugeas0",
                "libnewt0_52",
                "libzypp",
                "newt",
                "openssl",
                "perl-WWW-Curl",
                "python-dmidecode",
                "python-ethtool",
                "python-newt",
                "python-openssl",
                "python-xml",
                "rhnlib",
                "rpm-python",
                "satsolver-tools",
                "spacewalk-check",
                "spacewalk-client-setup",
                "spacewalk-client-tools",
                "spacewalksd",
                "suseRegister",
                "suseRegisterInfo",
                "yast2-ncurses",
                "yast2-perl-bindings",
                "yast2-pkg-bindings",
                "yast2-qt",
                "zypp-plugin-python",
                "zypp-plugin-spacewalk",
                "zypper"
            ]

PKGLIST11 = [
                "dbus-1-python",
                "libcurl4",
                "libnewt0_52",
                "libnl",
                "libopenssl0_9_8",
                "libsqlite3-0",
                "libxml2-python",
                "libzypp",
                "newt",
                "openssl",
                "python",
                "python-dmidecode",
                "python-ethtool",
                "python-newt",
                "python-openssl",
                "python-xml",
                "rhnlib",
                "rpm-python",
                "satsolver-tools",
                "slang",
                "spacewalk-check",
                "spacewalk-client-setup",
                "spacewalk-client-tools",
                "spacewalksd",
                "suseRegisterInfo",
                "zypp-plugin-python",
                "zypp-plugin-spacewalk",
                "zypper",
            ]

ENHANCE11 = [
                "libyaml-0-2",
                "libzmq3",
                "python-backports.ssl_match_hostname",
                "python-certifi",
                "python-curl",
                "python-futures",
                "python-Jinja2",
                "python-MarkupSafe",
                "python-msgpack-python",
                "python-psutil",
                "python-pycrypto",
                "python-pyzmq",
                "python-requests",
                "python-simplejson",
                "python-tornado",
                "python-yaml",
                "salt",
                "salt-minion"
            ]

PKGLIST12 = [
                "dbus-1-python",
                "hwdata",
                "libcurl4",
                "libgudev-1_0-0",
                "libnewt0_52",
                "libnl1",
                "libopenssl1_0_0",
                "libsqlite3-0",
                "libudev1",
                "udev",
                "openssl",
                "python-libxml2",
                "libzypp",
                "newt",
                "python",
                "python-cffi",
                "python-cryptography",
                "python-dmidecode",
                "python-ethtool",
                "python-gobject2",
                "python-gudev",
                "python-hwdata",
                "python-newt",
                "python-pyasn1",
                "python-pycparser",
                "python-pyOpenSSL",
                "python-six",
                "python-xml",
                "rhnlib",
                "rpm-python",
                "libsolv-tools",
                "libslang2",
                "spacewalk-check",
                "spacewalk-client-setup",
                "spacewalk-client-tools",
                "spacewalksd",
                "suseRegisterInfo",
                "zypp-plugin-python",
                "zypp-plugin-spacewalk",
                "zypper",
                "yast2-packager",
                "yast2-pkg-bindings",
                "libzmq3",
                "python-backports.ssl_match_hostname",
                "python-futures",
                "python-Jinja2",
                "python-MarkupSafe",
                "python-msgpack-python",
                "python-psutil",
                "python-pycrypto",
                "python-PyYAML",
                "python-pyzmq",
                "python-requests",
                "python-simplejson",
                "python-tornado",
                "salt",
                "salt-minion",
                "libgio-2_0-0",
                "libgthread-2_0-0",
                "shared-mime-info",
                "gio-branding-SLE",
                "wallpaper-branding-SLE",
                "glib2-tools",
                "libelf0",
                "logrotate",
                "cron",
                "cronie"
            ]

ENHANCE12 = [
             "libyui-ncurses-pkg6",
             "libyui-qt-pkg6",
             "PackageKit-backend-zypp",
             "PackageKit-lang",
            ]

ENHANCE12SP1 = [
                "libyui-ncurses-pkg7",
                "libyui-qt-pkg7",
                "python-enum34",
                "python-idna",
                "python-ipaddress",
               ]

RES6 = [
        "salt",
        "salt-minion",
        "python-futures",
        "python-jinja2",
        "python-msgpack-python",
        "python-psutil",
        "python-pycrypto",
        "python-requests",
        "python-setuptools",
        "python-tornado",
        "python-zmq",
        "zeromq",
        "openssl",
        "python-backports-ssl_match_hostname",
        "python-backports",
        "python-certifi",
        "python-simplejson",
        "PyYAML",
        "python-markupsafe",
        "python-urllib3",
        "libyaml",
        "python-chardet",
        "python-six",
        "python-babel",
        "dbus",
        "yum-plugin-security",
        "yum-rhn-plugin",
        "yum",
        "rhnlib",
       ]

RES7 = [
        "salt",
        "salt-minion",
        "python-futures",
        "python-jinja2",
        "python-msgpack-python",
        "python-psutil",
        "python-pycrypto",
        "python-requests",
        "python-setuptools",
        "python-tornado",
        "python-zmq",
        "zeromq",
        "python-backports-ssl_match_hostname",
        "python-backports",
        "python-certifi",
        "python-simplejson",
        "PyYAML",
        "python-markupsafe",
        "python-urllib3",
        "libyaml",
        "python-chardet",
        "python-six",
        "python-babel",
        "yum-rhn-plugin",
        "yum",
        "rhnlib",
        "openssl",
        "openssl-libs",
        "python-ipaddress",
       ]

DATA = {
    'SLE-11-SP1-i586' : {
                          'PDID' : 684, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
                        },
    'SLE-11-SP1-ia64' : {
                          'PDID' : 1033, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
                        },
    'SLE-11-SP1-ppc64' : {
                          'PDID' : 940, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
                        },
    'SLE-11-SP1-s390x' : {
                          'PDID' : 745, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
                        },
    'SLE-11-SP1-x86_64' : {
                          'PDID' : 769, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
                        },
    'SLE-11-SP2-i586' : {
                          'PDID' : 811, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
                        },
    'SLE-11-SP2-ia64' : {
                          'PDID' : 1034, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
                        },
    'SLE-11-SP2-ppc64' : {
                          'PDID' : 946, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
                        },
    'SLE-11-SP2-s390x' : {
                          'PDID' : 755, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
                        },
    'SLE-11-SP2-x86_64' : {
                          'PDID' : 690, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
                        },
    'SLE-11-SP3-i586' : {
                          'PDID' : 793, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
                        },
    'SLE-11-SP3-ia64' : {
                          'PDID' : 1037, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
                        },
    'SLE-11-SP3-ppc64' : {
                          'PDID' : 949, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
                        },
    'SLE-11-SP3-s390x' : {
                          'PDID' : 693, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
                        },
    'SLE-11-SP3-x86_64' : {
                          'PDID' : 814, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
                        },
    'SLE-11-SP4-i586' : {
                          'PDID' : 1299, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
                        },
    'SLE-11-SP4-ia64' : {
                          'PDID' : 1302, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
                        },
    'SLE-11-SP4-ppc64' : {
                          'PDID' : 1301, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
                        },
    'SLE-11-SP4-s390x' : {
                          'PDID' : 1303, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
                        },
    'SLE-11-SP4-x86_64' : {
                          'PDID' : 1300, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
                        },
    'SLE-10-SP3-i586' : {
                          'PDID' : 785, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
                        },
    'SLE-10-SP3-ia64' : {
                          'PDID' : 740, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
                        },
    'SLE-10-SP3-ppc' : {
                          'PDID' : 787, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
                        },
    'SLE-10-SP3-s390x' : {
                          'PDID' : 682, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
                        },
    'SLE-10-SP3-x86_64' : {
                          'PDID' : 721, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/3/bootstrap/'
                        },
    'SLE-10-SP4-i586' : {
                          'PDID' : 752, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
                        },
    'SLE-10-SP4-ia64' : {
                          'PDID' : 770, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
                        },
    'SLE-10-SP4-ppc' : {
                          'PDID' : 711, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
                        },
    'SLE-10-SP4-s390x' : {
                          'PDID' : 771, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
                        },
    'SLE-10-SP4-x86_64' : {
                          'PDID' : 832, 'PKGLIST' : PKGLIST10,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/10/4/bootstrap/'
                        },
    'SLES4SAP-11-SP1-x86_64' : {
                          'PDID' : 1129, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/1/bootstrap/'
                        },
    'SLES4SAP-11-SP2-x86_64' : {
                          'PDID' : 1130, 'PKGLIST' : PKGLIST11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/2/bootstrap/'
                        },
    'SLES4SAP-11-SP3-x86_64' : {
                          'PDID' : 1131, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/3/bootstrap/'
                        },
    'SLES4SAP-11-SP4-x86_64' : {
                          'PDID' : 1329, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
                        },
    'SLES4SAP-11-SP4-ppc64' : {
                          'PDID' : 1331, 'PKGLIST' : PKGLIST11 + ENHANCE11,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/11/4/bootstrap/'
                        },
    'SLE-12-ppc64le' : {
                          'PDID' : 1116, 'PKGLIST' : PKGLIST12 + ENHANCE12,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/0/bootstrap/'
                        },
    'SLE-12-s390x' : {
                          'PDID' : 1115, 'PKGLIST' : PKGLIST12 + ENHANCE12,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/0/bootstrap/'
                        },
    'SLE-12-x86_64' : {
                          'PDID' : 1117, 'PKGLIST' : PKGLIST12 + ENHANCE12,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/0/bootstrap/'
                        },
    'SLES4SAP-12-x86_64' : {
                          'PDID' : 1319, 'PKGLIST' : PKGLIST12 + ENHANCE12,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/0/1/bootstrap/'
                        },
    'SLE-12-SP1-ppc64le' : {
                          'PDID' : 1334, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/bootstrap/'
                        },
    'SLE-12-SP1-s390x' : {
                          'PDID' : 1335, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/bootstrap/'
                        },
    'SLE-12-SP1-x86_64' : {
                          'PDID' : 1322, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/bootstrap/'
                        },
    'SLES4SAP-12-SP1-ppc64le' : {
                          'PDID' : 1437, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/0/1/bootstrap/'
                        },
    'SLES4SAP-12-SP1-x86_64' : {
                          'PDID' : 1346, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/1/0/1/bootstrap/'
                        },
    'RES6-x86_64' : {
                          'PDID' : 1138, 'PKGLIST' : RES6,
                          'DEST' : '/srv/www/htdocs/pub/repositories/res/6/bootstrap/'
                    },
    'RES7-x86_64' : {
                          'PDID' : 1251, 'PKGLIST' : RES7,
                          'DEST' : '/srv/www/htdocs/pub/repositories/res/7/bootstrap/'
                    },
    'SLE-12-SP2-aarch64' : {
                          'PDID' : 1375, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
                        },
    'SLES_RPI-12-SP2-aarch64' : {
                          'PDID' : 1418, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
                        },
    'SLE-12-SP2-ppc64le' : {
                          'PDID' : 1355, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
                        },
    'SLE-12-SP2-s390x' : {
                          'PDID' : 1356, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
                        },
    'SLE-12-SP2-x86_64' : {
                          'PDID' : 1357, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
                        },
    'SLES4SAP-12-SP2-x86_64' : {
                          'PDID' : 1414, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
                        },
    'SLES4SAP-12-SP2-ppc64le' : {
                          'PDID' : 1521, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
                        },
    'SLE-12-SP3-aarch64' : {
                          'PDID' : 1424, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
                        },
    'SLE-12-SP3-ppc64le' : {
                          'PDID' : 1422, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
                        },
    'SLE-12-SP3-s390x' : {
                          'PDID' : 1423, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
                        },
    'SLE-12-SP3-x86_64' : {
                          'PDID' : 1421, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
                        },
    'SLES4SAP-12-SP3-x86_64' : {
                          'PDID' : 1426, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
                        },
    'SLES4SAP-12-SP3-ppc64le' : {
                          'PDID' : 1572, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/3/bootstrap/'
                        },
    'OES2018-x86_64' : {
                          'PDID' : 45, 'PKGLIST' : PKGLIST12 + ENHANCE12SP1,
                          'DEST' : '/srv/www/htdocs/pub/repositories/sle/12/2/bootstrap/'
                       },
}

