Summary:	IRC Client for Emacs
Summary(pl):	Klient irca dla Emacsa
Name:		emacs-erc
Version:	4.0
Release:	0.9
License:	GPL v2
Group:		Applications/Editors/Emacs
Source0:	http://belnet.dl.sourceforge.net/sourceforge/erc/erc-%{version}.tar.gz
# Source0-md5:	4242f5ef41838a395fd5eb4dc3072627
URL:		http://www.emacswiki.org/cgi-bin/wiki?EmacsIRCClient
BuildRequires:	emacs
Requires:	emacs >= 21.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IRC Client for Emacs

%description -l pl
Klient irca dla Emacsa

%prep
%setup -q -n erc-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
install erc*.el	$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README AUTHORS ChangeLog CREDITS
%{_datadir}/emacs/site-lisp/*.el
