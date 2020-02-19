Summary: Lightweight connection pooler for PostgreSQL
Name: pgbouncer
Version: 1.14.0
Release: 1%{?dist}
License: ISC
Group: Database
Source: pgbouncer-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: libevent-devel
BuildRequires: libopenssl-1_1-devel

BuildRoot: %{_tmppath}/%{name}-root

%description
A lightweight connection pooler for PostgreSQL

%prep
%setup -q

%build
./autogen.sh
%configure \
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --libdir=%{_libdir} \
    --docdir %{_docdir}/%{name}
make %{?_smp_mflags}

%check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post

%preun

%files
%defattr(-,root,root)
%doc AUTHORS COPYRIGHT NEWS.md README.md
%_bindir/pgbouncer

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Jun 17 2020 Enrico Weigelt, metux IT consult <info@metux.net> - 1.14.0
- Packaged for SLES 12
