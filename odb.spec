Name:		ODB		
Version:	10.0	
Release:	1%{?dist}
Summary:	Why You use RPM if you can use maven?

Group:		Lolo
License:	Uganda Drivers License
URL:		http://idontknowwhyineedtopackagethisstupidpackage.com	
Source0:	odb.tar.gz
Source1:	ironcloud.conf
Source2:	odb.init
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
ODB package ...
#One day Nikita asks for ODB RPM instead of JUST using maven. And then this stupid and unneeded package was born ...


%prep
%setup -q -n odb

%build

%install
install -d -m 755 %{buildroot}%{_datarootdir}
install -d -m 755 %{buildroot}%{_sysconfdir}
cp -r odb %{buildroot}%{_datarootdir}/
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/ironcloud.conf
install -p -D -m 755 %{SOURCE2} %{buildroot}%{_initrddir}/odb


%clean
rm -rf $RPM_BUILD_ROOT

%post


%preun


%files
%defattr(-,root,root,-)
%{_datarootdir}/odb
%{_initrddir}/odb
%config(noreplace)
%{_sysconfdir}/ironcloud.conf
%doc



%changelog

