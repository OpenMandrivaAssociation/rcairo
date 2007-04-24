%define name  rcairo
%define version 1.4.1
%define release %mkrel 1

Summary: Ruby bindings for cairo
Name: %name
Version: %version
Release: %release
License: GPL
Group:	Development/Ruby
URL:	http://cairo.freedesktop.org/rcairo
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel cairo-devel

%description
Ruby bindings for cairo

%package -n ruby-cairo
Summary: Ruby bindings for cairo
Group:	Development/Other

%description -n ruby-cairo
Ruby bindings for cairo

%package -n ruby-cairo-devel
Summary: Development files of ruby cairo bindings
Group:  Development/Other
Requires: ruby-cairo = %{version}

%description -n ruby-cairo-devel
Development files of ruby cairo bindings

%prep
%setup -q 

%build
ruby extconf.rb
%make 

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
make install DESTDIR=%{buildroot}

%files -n ruby-cairo
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README samples/png.rb
%{ruby_sitelibdir}/cairo*
%{ruby_sitearchdir}/cairo.so

%files -n ruby-cairo-devel
%defattr(-,root,root)
%doc AUTHORS COPYING
%{ruby_sitearchdir}/rb_cairo.h
