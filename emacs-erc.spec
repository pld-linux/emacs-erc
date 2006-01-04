Summary:	IRC Client for Emacs
Summary(pl):	Klient irca dla Emacsa
Name:		emacs-erc
Version:	5.0.4
Release:	0.1
License:	GPL v2
Group:		Applications/Editors/Emacs
Source0:	http://dl.sourceforge.net/erc/erc-%{version}.tar.gz
# Source0-md5:	7162aedf0a0d4893425f1c669b2ea403
URL:		http://www.emacswiki.org/cgi-bin/wiki?EmacsIRCClient
BuildRequires:	emacs
Requires:	emacs >= 21.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IRC Client for Emacs.

%description -l pl
Klient irca dla Emacsa.

%prep
%setup -q -n erc-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
install erc*.el	$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README AUTHORS ChangeLog CREDITS
%{_datadir}/emacs/site-lisp/*.el
