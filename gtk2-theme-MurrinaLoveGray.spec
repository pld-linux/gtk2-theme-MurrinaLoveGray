%define shortname MurrinaLoveGray
Summary:	A Gray colorscheme, with elegant bright buttons
Name:		gtk2-theme-%{shortname}
Version:	1.0
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://www.cimitan.com/murrine/files/%{shortname}.tar.bz2
# Source0-md5:	31ce9fce5114c1cfe471dc614de539cc
URL:		http://www.cimitan.com/murrine/
Requires:	gtk2-theme-engine-murrine >= 0.90.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Gray colorscheme, with elegant bright buttons.

%prep
%setup -q -n %{shortname}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/%{shortname}
cp -R gtk* $RPM_BUILD_ROOT%{_datadir}/themes/%{shortname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/%{shortname}
