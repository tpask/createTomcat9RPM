# this script creates rpmbuild tree in your home dir.

pkgName=package
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

