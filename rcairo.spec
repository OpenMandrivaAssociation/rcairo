%define name  rcairo
%define version 1.8.0
%define release %mkrel 2

Summary: Ruby bindings for cairo
Name: %name
Version: %version
Release: %release
License: GPL
Group:	Development/Ruby
URL: http://cairographics.org
Source0: http://cairographics.org/releases/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel cairo-devel

%description
Ruby bindings for cairo

%package -n ruby-cairo
Summary: Ruby bindings for cairo
Group:	Development/Ruby
Provides: rcairo

%description -n ruby-cairo
Ruby bindings for cairo

%package -n ruby-cairo-devel
Summary: Development files of ruby cairo bindings
Group:  Development/Ruby
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
