# for security reasons, you should NEVER build an RPM with the root user. You should always use an unprivileged user for this purpose.
#set your package name here:
pkgName=packageName

sudo yum -y install rpm-build tree rpmdevtools
cd
echo -e "\n*** creating rpmbuild directory structures..."

#w/o rmpdevtools: mkdir -p ~/rpmbuild/{BUILD,RPMS,RPMS/noarch,SOURCES,SPECS,SRPMS}
rpmdev-setuptree

#create spec file
echo -e "\n*** creating spec shell file... "
cd rpmbuild/SPECS
rpmdev-newspec $pkgName
cd

#show tree
tree rpmbuild


