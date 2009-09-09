%define	name	vim-latex
%define	version	20060325
%define	release	%mkrel 6
%define summary Advanced vim plugin for LaTeX editing
%define group	Editors

Name:		%{name} 
Summary:	%{summary}
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://vim-latex.sf.net/
Group:		%{group}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	Charityware
BuildArch:	noarch
Requires:	vim
Requires:	python
Requires:	tetex-latex

%description
Latex-Suite attempts to provide a comprehensive set of tools to
view, edit and compile LaTeX documents in Vim. Together, they
provide tools starting from macros to speed up editing LaTeX
documents to functions for forward searching .dvi documents.

This package does not contain the compiler part of Latex-Suite
due to conflicts with the standard vim tex-compiler.

%prep
%setup -q

%build
# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
rm -rf compiler/
# Fix permissions
for a in `find`;do
	if [ ! -d $a ]; then
		case $a in
			*ltags | *.py ) : ;;
			* ) chmod -x $a;;
		esac
	fi
done
# Add shellbang
mv ftplugin/latex-suite/pytools.py pytools.py.backup
echo '#!/bin/env python' > ftplugin/latex-suite/pytools.py
cat pytools.py.backup >> ftplugin/latex-suite/pytools.py
rm -f pytools.py.backup
cat << EOF > ./README
Read the builtin documentation. From within vim type
:help latex-suite.txt
:help latex-suite-quickstart.txt

Latex-Suite comes ships with edition 1.6 of the LaTeX2e
documentation translated into vim-help format.
Type :help helptags from within Vim for more information
EOF

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vim/
cp -rv * $RPM_BUILD_ROOT%{_datadir}/vim/
rm -f $RPM_BUILD_ROOT%{_datadir}/vim/README
chmod +x $RPM_BUILD_ROOT%{_datadir}/vim/ftplugin/latex-suite/pytools.py

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc README
%{_datadir}/vim/ltags
%{_datadir}/vim/doc/*
%{_datadir}/vim/ftplugin/*
%{_datadir}/vim/indent/*
%{_datadir}/vim/plugin/*

