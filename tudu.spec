Summary:	TuDu is a comand line interface to manage hierarchical todos
Summary(hu.UTF-8):	TuDu egy parancssoror környezet hierarchikus teendők kezelésére
Name:		tudu
Version:	0.4.1
Release:	0.1
License:	GPL v3
Group:		Development/Tools
Source0:	http://cauterized.net/~meskio/tudu/%{name}-%{version}.tar.gz
# Source0-md5:	c7deebc87c831003192fefbe20535d82
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-welcome.patch
Patch2:		%{name}-fixdirs.patch
URL:		http://www.cauterized.net/~meskio/tudu/
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TuDu is a comand line interface to manage hierarchical todos. Every
todo has a title, a description, a deadline, category and a priority.
It shows the percentage of your done work, too.

%description -l hu.UTF-8
TuDu egy parancssoros környezet hierarchikus teendők kezelésére.
Minden teendőnek van egy címe, leírása, befejezési időpontja,
kategóriája és prioritása. A haladás százalékát is megmutatja.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%{__sed} -i "s@ncurses.h@ncurses/ncurses.h@" src/*
%{__sed} -i "s@form.h@ncurses/form.h@" src/*

%build
%{__make} CFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tudurc
%attr(755,root,root) %{_bindir}/*
%doc AUTHORS ChangeLog README
%{_mandir}/man1/*
%{_datadir}/tudu
