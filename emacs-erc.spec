#
# TODO:	- xemacs pkg, rename to emacsen-erc.spec
#
Summary:	IRC Client for Emacs
Summary(pl):	Klient irca dla Emacsa
Name:		emacs-erc
Version:	5.1.2
Release:	1
License:	GPL v2
Group:		Applications/Editors/Emacs
Source0:	http://dl.sourceforge.net/erc/erc-%{version}.tar.gz
# Source0-md5:	1c79609f8597bc158785487f9795dd78
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-install-info.patch
URL:		http://www.emacswiki.org/cgi-bin/wiki?EmacsIRCClient
BuildRequires:	emacs >= 21.1
BuildRequires:	texinfo
Requires:	emacs >= 21.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _pkglispdir %{_emacs_lispdir}/erc

%description
IRC Client for Emacs.

%description -l pl
Klient irca dla Emacsa.

%prep
%setup -q -n erc-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make}
%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_pkglispdir}/images

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	ELISPDIR="%{_pkglispdir}" \
	INFODIR="%{_infodir}"

install images/* $RPM_BUILD_ROOT%{_pkglispdir}/images

rm -f $RPM_BUILD_ROOT%{_pkglispdir}/*.el

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS HISTORY NEWS README ChangeLog* erc.html servers.pl
%dir %{_pkglispdir}
%{_pkglispdir}/*.elc
%{_pkglispdir}/images
%{_infodir}/*
