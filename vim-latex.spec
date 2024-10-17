%define reldate	20100129
%define rel	r1104

Name:		vim-latex
Summary:	Advanced vim plugin for LaTeX editing
Version:	1.8.23
Epoch:		1
Release:	3
Source0:	http://downloads.sourceforge.net/project/vim-latex/snapshots/%{name}-%{version}-%{reldate}-%{rel}.tar.gz
URL:		https://vim-latex.sf.net/
Group:		Editors
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	Charityware
BuildArch:	noarch
Obsoletes:	vim-latex < %epoch:%version
Requires:	vim
Requires:	python
Requires:	tetex-latex
Requires:	xdvi

%description
Latex-Suite attempts to provide a comprehensive set of tools to
view, edit and compile LaTeX documents in Vim. Together, they
provide tools starting from macros to speed up editing LaTeX
documents to functions for forward searching .dvi documents.

%prep
%setup -q -n %{name}-%{version}-%{reldate}-%{rel}

%build
# Add shellbang
mv ftplugin/latex-suite/pytools.py pytools.py.backup
echo '#!/bin/env python' > ftplugin/latex-suite/pytools.py
cat pytools.py.backup >> ftplugin/latex-suite/pytools.py
rm -f pytools.py.backup

cat << EOF > ./README.mandriva
To Read the builtin documentation. From within vim type
:help latex-suite.txt
:help latex-suite-quickstart.txt

Latex-Suite comes with edition 1.6 of the LaTeX2e
documentation translated into vim-help format.
Type :help helptags from within Vim for more information
EOF

%install
rm -rf %{buildroot}
# use the already existing make file
make install DESTDIR=%{buildroot} VIMDIR=%{_datadir}/vim BINDIR=%{_bindir}

# move compiler/tex.vim to not conflict with vim-common
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/
mv %{buildroot}%{_datadir}/vim/compiler %{buildroot}%{_datadir}/vim/vimfiles/

# fix permissions
chmod +x %{buildroot}%{_datadir}/vim/ftplugin/latex-suite/pytools.py

%clean 
rm -rf %{buildroot} 

%files 
%defattr(-,root,root)
%doc README.mandriva
%{_bindir}/ltags
%{_bindir}/latextags
%{_datadir}/vim/vimfiles/compiler/*
%{_datadir}/vim/doc/*
%{_datadir}/vim/ftplugin/*
%{_datadir}/vim/indent/*
%{_datadir}/vim/plugin/*


%changelog
* Mon Apr 19 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:1.8.23-2mdv2010.1
+ Revision: 536881
- modify the description, package now has tex.vim in vim/vimfiles/

* Fri Apr 16 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:1.8.23-1mdv2010.1
+ Revision: 535553
- new upstream release 1.8.23
- use make install
- move compiler/tex.vim to vim/vimfiles/ to not conflict with vim-common

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 20060325-6mdv2010.0
+ Revision: 434675
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 20060325-5mdv2009.0
+ Revision: 261864
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 20060325-4mdv2009.0
+ Revision: 255554
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 20060325-3mdv2009.0
+ Revision: 239732
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20060325-1mdv2008.1
+ Revision: 129160
- kill re-definition of %%buildroot on Pixel's request


* Sat Jun 10 2006 Eskild Hustvedt <eskild@mandriva.org> 20060325-1mdv
- New version 20060325
- Requires tetex-latex

* Sun Jan 22 2006 Eskild Hustvedt <eskild@mandrake.com> 20060120-1mdk
- Initial Mandriva Linux package

