Name:		ODB		
Version:	10.0	
Release:	1%{?dist}
Summary:	Why You use RPM if you can use maven?

Group:		Lolo
License:	Uganda Drivers License
URL:		http://idontknowwhyineedtopackagethisstupidpackage.com	
Source0:	odb.tar.gz
Source1:	ironcloud.conf
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
ODB package ...
#One day Nikita asks for ODB RPM instead of JUST using maven. And then this stupid and unneeded package was born ...


%prep
%setup -q -n odb

%build
install -d -m 755 %{buildroot}%{_datarootdir}
cp -r odb %{buildroot}%{_datarootdir}/
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/ironcloud.conf

%install
rm -rf $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datarootdir}/odb
%config(noreplace)
%{_sysconfdir}/ironcloud.conf
%doc



%changelog

