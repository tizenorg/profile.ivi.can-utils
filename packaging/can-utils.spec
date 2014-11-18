Name:          can-utils
Summary:       CAN userspace utilities and tools
Version:       0.1
Release:       1
Group:         Automotive/Hardware Adaption
License:       (GPL-2.0 or BSD-3-Clause) and GPL-2.0+
URL:           https://gitorious.org/linux-can/can-utils/
Source:        %{name}-%{version}.tar.gz
Source1001:    %{name}.manifest

%description
CAN (controller area network) bus userspace utilities and tools.


%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1001} .

%build
%autogen
%configure
make %{?_smp_mflags}

%install
%make_install

%clean

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/*
