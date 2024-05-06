FROM centos:stream8

ENV I_AM_IN_A_CONTAINER 1
LABEL maintainer="WUVT-FM <it@wuvt.vt.edu>"
LABEL ceph="True"
LABEL RELEASE="HEAD"
LABEL GIT_REPO="https://github.com/ceph/ceph-container.git"
LABEL GIT_BRANCH="HEAD"
LABEL GIT_COMMIT="12717c0777377369ea674892da98b0d85250f5b0"
LABEL GIT_CLEAN="False"
LABEL CEPH_POINT_RELEASE="-18.2.2"

ENV CEPH_VERSION reef
ENV CEPH_POINT_RELEASE "-18.2.2"
ENV CEPH_DEVEL false
ENV CEPH_REF reef
ENV OSD_FLAVOR default

EXPOSE 6789 6800 6801 6802 6803 6804 6805 80 5000

RUN \
    # Install all components for the image, whether from packages or web downloads.
    # Typical workflow: add new repos; refresh repos; install packages; package-manager clean;
    #   download and install packages from web, cleaning any files as you go.
    # Installs should support install of ganesha for luminous
    yum install -y epel-release && \
yum install -y jq && \
bash -c ' \
  echo "[ganesha]" > /etc/yum.repos.d/ganesha.repo ; \
  echo "name=ganesha" >> /etc/yum.repos.d/ganesha.repo ; \
  echo "baseurl=https://buildlogs.centos.org/centos/\$releasever-stream/storage/\$basearch/nfsganesha-5/" >> /etc/yum.repos.d/ganesha.repo ; \
  echo "gpgcheck=0" >> /etc/yum.repos.d/ganesha.repo ; \
  echo "enabled=1" >> /etc/yum.repos.d/ganesha.repo  ; \
  curl -s -L https://shaman.ceph.com/api/repos/tcmu-runner/main/latest/centos/8/repo?arch=$(arch) -o /etc/yum.repos.d/tcmu-runner.repo ; \
  curl -s -L https://download.ceph.com/ceph-iscsi/3/rpm/el8/ceph-iscsi.repo -o /etc/yum.repos.d/ceph-iscsi.repo' && \
bash -c ' \
  echo "[Ceph]" > /etc/yum.repos.d/ceph.repo ; \
  echo "name=Ceph packages for \$basearch" >> /etc/yum.repos.d/ceph.repo ; \
  echo "baseurl=http://localhost:8000/rpm-reef/el8/\$basearch" >> /etc/yum.repos.d/ceph.repo ; \
  echo "gpgcheck=0" >> /etc/yum.repos.d/ceph.repo ; \
  echo "enabled=1" >> /etc/yum.repos.d/ceph.repo ; \
  echo "[Ceph-noarch]" >> /etc/yum.repos.d/ceph.repo ; \
  echo "name=Ceph noarch packages" >> /etc/yum.repos.d/ceph.repo ; \
  echo "baseurl=http://localhost:8000/rpm-reef/el8/noarch" >> /etc/yum.repos.d/ceph.repo ; \
  echo "gpgcheck=0" >> /etc/yum.repos.d/ceph.repo ; \
  echo "enabled=1" >> /etc/yum.repos.d/ceph.repo' && \
yum update -y --setopt=install_weak_deps=False && \
bash -c ' \
  yum install -y dnf-plugins-core ; \
  yum copr enable -y tchaikov/python-scikit-learn ; \
  yum copr enable -y tchaikov/python3-asyncssh' && \
yum install -y --setopt=install_weak_deps=False --enablerepo=powertools \
        ca-certificates \
        e2fsprogs \
        ceph-common-18.2.2  \
        ceph-mon-18.2.2  \
        ceph-osd-18.2.2 \
        ceph-mds-18.2.2 \
        cephfs-mirror-18.2.2 \
        cephfs-top-18.2.2 \
        rbd-mirror-18.2.2  \
        ceph-mgr-18.2.2 \
        ceph-mgr-cephadm-18.2.2 \
        ceph-mgr-dashboard-18.2.2 \
        ceph-mgr-diskprediction-local-18.2.2 \
        ceph-mgr-k8sevents-18.2.2 \
        ceph-mgr-rook-18.2.2 \
        python3-saml\
        ceph-grafana-dashboards-18.2.2 \
        kmod \
        lvm2 \
        gdisk \
        smartmontools \
        nvme-cli \
        libstoragemgmt \
        systemd-udev \
        sg3_utils \
        procps-ng \
        hostname \
        ceph-radosgw-18.2.2 libradosstriper1-18.2.2 gcc lua-devel luarocks \
        nfs-ganesha-5.5-1.el8s nfs-ganesha-ceph-5.5-1.el8s nfs-ganesha-rgw-5.5-1.el8s nfs-ganesha-rados-grace-5.5-1.el8s nfs-ganesha-rados-urls-5.5-1.el8s sssd-client dbus-daemon rpcbind \
        tcmu-runner ceph-iscsi python3-rtslib \
        attr \
        ceph-fuse-18.2.2 \
        rbd-nbd-18.2.2 \
        ${CRIMSON_PACKAGES} \
        ceph-immutable-object-cache-18.2.2 \
        python3-scikit-learn \
        ceph-volume-18.2.2 \
        ceph-exporter-18.2.2 \
         && \
    echo '@ceph - memlock 204800' >> /etc/security/limits.conf && \
    echo '@root - memlock 204800' >> /etc/security/limits.conf && \
    # Clean container, starting with record of current size (strip / from end)
    INITIAL_SIZE="$(bash -c 'sz="$(du -sm --exclude=/proc /)" ; echo "${sz%*/}"')" && \
    #
    #
    # Perform any final cleanup actions like package manager cleaning, etc.
    echo 'Postinstall cleanup' && \
 (rm -rf "/usr/bin/hyperkube /usr/bin/etcd /usr/bin/systemd-analyze /usr/share/hwdata/{iab.txt,oui.txt} /etc/profile.d/lang.sh" && \
   yum clean all && \
   rpm -q \
        ca-certificates \
        e2fsprogs \
        ceph-common-18.2.2  \
        ceph-mon-18.2.2  \
        ceph-osd-18.2.2 \
        ceph-mds-18.2.2 \
        cephfs-mirror-18.2.2 \
        cephfs-top-18.2.2 \
        rbd-mirror-18.2.2  \
        ceph-mgr-18.2.2 \
        ceph-mgr-cephadm-18.2.2 \
        ceph-mgr-dashboard-18.2.2 \
        ceph-mgr-diskprediction-local-18.2.2 \
        ceph-mgr-k8sevents-18.2.2 \
        ceph-mgr-rook-18.2.2 \
        python3-saml\
        ceph-grafana-dashboards-18.2.2 \
        kmod \
        lvm2 \
        gdisk \
        smartmontools \
        nvme-cli \
        libstoragemgmt \
        systemd-udev \
        sg3_utils \
        procps-ng \
        hostname \
        ceph-radosgw-18.2.2 libradosstriper1-18.2.2 gcc lua-devel luarocks \
        nfs-ganesha-5.5-1.el8s nfs-ganesha-ceph-5.5-1.el8s nfs-ganesha-rgw-5.5-1.el8s nfs-ganesha-rados-grace-5.5-1.el8s nfs-ganesha-rados-urls-5.5-1.el8s sssd-client dbus-daemon rpcbind \
        tcmu-runner ceph-iscsi python3-rtslib \
        attr \
        ceph-fuse-18.2.2 \
        rbd-nbd-18.2.2 \
        ${CRIMSON_PACKAGES} \
        ceph-immutable-object-cache-18.2.2 \
        python3-scikit-learn \
        ceph-volume-18.2.2 \
        ceph-exporter-18.2.2 \
         ) && \
    # Tweak some configuration files on the container system
    # disable sync with udev since the container can not contact udev
echo "About to edit lvm.conf" && \
sed -i -e 's/^\([[:space:]#]*udev_rules =\) 1$/\1 0/' -e 's/^\([[:space:]#]*udev_sync =\) 1$/\1 0/' -e 's/^\([[:space:]#]*obtain_device_list_from_udev =\) 1$/\1 0/' /etc/lvm/lvm.conf && \
echo "About to validate lvm.conf edits" && \
# validate the sed command worked as expected
grep -sqo "udev_sync = 0" /etc/lvm/lvm.conf && \
grep -sqo "udev_rules = 0" /etc/lvm/lvm.conf && \
grep -sqo "obtain_device_list_from_udev = 0" /etc/lvm/lvm.conf && \
echo "Edits validated OK" && \
mkdir -p /var/run/ganesha && \
    
    # Clean common files like /tmp, /var/lib, etc.
    rm -rf \
        /etc/{selinux,systemd,udev} \
        /lib/{lsb,udev} \
        /tmp/* \
        /usr/lib{,64}/{locale,udev,dracut} \
        /usr/share/{doc,info,locale,man} \
        /usr/share/{bash-completion,pkgconfig/bash-completion.pc} \
        /var/log/* \
        /var/tmp/* && \
    find  / -xdev -name "*.pyc" -o -name "*.pyo" -exec rm -f {} \; && \
    # ceph-dencoder is only used for debugging, compressing it saves 10MB
    # If needed it will be decompressed
    # TODO: Is ceph-dencoder safe to remove as rook was trying to do?
    # rm -f /usr/bin/ceph-dencoder && \
    if [ -f /usr/bin/ceph-dencoder ]; then gzip -9 /usr/bin/ceph-dencoder; fi && \
    # TODO: What other ceph stuff needs removed/stripped/zipped here?
    # Photoshop files inside a container ?
    rm -f /usr/lib/ceph/mgr/dashboard/static/AdminLTE-*/plugins/datatables/extensions/TableTools/images/psd/* && \
    # Some logfiles are not empty, there is no need to keep them
    find /var/log/ -type f -exec truncate -s 0 {} \; && \
    #
    #
    # Report size savings (strip / from end)
    FINAL_SIZE="$(bash -c 'sz="$(du -sm --exclude=/proc /)" ; echo "${sz%*/}"')" && \
    REMOVED_SIZE=$((INITIAL_SIZE - FINAL_SIZE)) && \
    echo "Cleaning process removed ${REMOVED_SIZE}MB" && \
    echo "Dropped container size from ${INITIAL_SIZE}MB to ${FINAL_SIZE}MB" && \
    #
    # Verify that the packages installed haven't been accidentally cleaned
    rpm -q \
        ca-certificates \
        e2fsprogs \
        ceph-common-18.2.2  \
        ceph-mon-18.2.2  \
        ceph-osd-18.2.2 \
        ceph-mds-18.2.2 \
        cephfs-mirror-18.2.2 \
        cephfs-top-18.2.2 \
        rbd-mirror-18.2.2  \
        ceph-mgr-18.2.2 \
        ceph-mgr-cephadm-18.2.2 \
        ceph-mgr-dashboard-18.2.2 \
        ceph-mgr-diskprediction-local-18.2.2 \
        ceph-mgr-k8sevents-18.2.2 \
        ceph-mgr-rook-18.2.2 \
        python3-saml\
        ceph-grafana-dashboards-18.2.2 \
        kmod \
        lvm2 \
        gdisk \
        smartmontools \
        nvme-cli \
        libstoragemgmt \
        systemd-udev \
        sg3_utils \
        procps-ng \
        hostname \
        ceph-radosgw-18.2.2 libradosstriper1-18.2.2 gcc lua-devel luarocks \
        nfs-ganesha-5.5-1.el8s nfs-ganesha-ceph-5.5-1.el8s nfs-ganesha-rgw-5.5-1.el8s nfs-ganesha-rados-grace-5.5-1.el8s nfs-ganesha-rados-urls-5.5-1.el8s sssd-client dbus-daemon rpcbind \
        tcmu-runner ceph-iscsi python3-rtslib \
        attr \
        ceph-fuse-18.2.2 \
        rbd-nbd-18.2.2 \
        ${CRIMSON_PACKAGES} \
        ceph-immutable-object-cache-18.2.2 \
        python3-scikit-learn \
        ceph-volume-18.2.2 \
        ceph-exporter-18.2.2 \
         && echo 'Packages verified successfully'

