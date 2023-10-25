%define debug_package %{nil}

Name:		    {{{ git_dir_name }}}
Version:	    {{{ get_version }}}
Release:	    {{{ get_release }}}%{?dist}
Summary:	    Bluetooth firmware for Raspberry Pi

License:	    GPLv2+
URL:		    http://www.bluez.org
VCS:		    {{{ git_dir_vcs }}}

Source:		    {{{ git_dir_pack }}}

BuildRequires:	make
BuildRequires:  autoconf
BuildRequires:  automake

Requires:	    bluez

%description
This firmware is required for the successful operation of Broadcom based USB
dongles.

%prep
{{{ git_dir_setup_macro }}}

%build

%install
# Copy firmware binaries
mkdir -p %{buildroot}%{_prefix}/lib/firmware/{brcm,synaptics}
install debian/firmware/broadcom/*.hcd %{buildroot}%{_prefix}/lib/firmware/brcm
install debian/firmware/synaptics/*.hcd %{buildroot}%{_prefix}/lib/firmware/synaptics

# Create links
ln -s BCM43430A1.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM43430A1.raspberrypi,3-model-b.hcd
ln -s BCM43430A1.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM43430A1.raspberrypi,model-zero-w.hcd
ln -s BCM4345C0.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,3-model-a-plus.hcd
ln -s BCM4345C0.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,3-model-b-plus.hcd
ln -s BCM4345C0.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,4-compute-module.hcd
ln -s BCM4345C0.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,4-model-b.hcd
ln -s BCM4345C0.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,5-model-b.hcd
ln -s BCM4345C5.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM4345C5.raspberrypi,4-compute-module.hcd
ln -s BCM4345C5.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM4345C5.raspberrypi,400.hcd
ln -s ../synaptics/SYN43430A1.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM43430A1.raspberrypi,model-zero-2-w.hcd
ln -s ../synaptics/SYN43430B0.hcd %{buildroot}%{_prefix}/lib/firmware/brcm/BCM43430B0.raspberrypi,model-zero-2-w.hcd

%files
%license debian/firmware/broadcom/LICENSE.cypress debian/firmware/synaptics/LICENSE.synaptics
%doc debian/changelog
%{_prefix}/lib/firmware/brcm/BCM43430A1.hcd
%{_prefix}/lib/firmware/brcm/BCM43430B0.hcd
%{_prefix}/lib/firmware/brcm/BCM4345C0.hcd
%{_prefix}/lib/firmware/brcm/BCM4345C5.hcd
%{_prefix}/lib/firmware/synaptics/SYN43430A1.hcd
%{_prefix}/lib/firmware/synaptics/SYN43430B0.hcd
%{_prefix}/lib/firmware/brcm/BCM43430A1.raspberrypi,3-model-b.hcd
%{_prefix}/lib/firmware/brcm/BCM43430A1.raspberrypi,model-zero-w.hcd
%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,3-model-a-plus.hcd
%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,3-model-b-plus.hcd
%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,4-compute-module.hcd
%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,4-model-b.hcd
%{_prefix}/lib/firmware/brcm/BCM4345C0.raspberrypi,5-model-b.hcd
%{_prefix}/lib/firmware/brcm/BCM4345C5.raspberrypi,4-compute-module.hcd
%{_prefix}/lib/firmware/brcm/BCM4345C5.raspberrypi,400.hcd
%{_prefix}/lib/firmware/brcm/BCM43430A1.raspberrypi,model-zero-2-w.hcd
%{_prefix}/lib/firmware/brcm/BCM43430B0.raspberrypi,model-zero-2-w.hcd

%changelog
{{{ git_dir_changelog }}}
