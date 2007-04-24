%define name  rcairo
%define version 1.0.0
%define release %mkrel 1

Summary: Ruby bindings for cairo
Name: %name
Version: %version
Release: %release
License: GPL
Group:	Development/Other
URL:	http://cairo.freedesktop.org/rcairo
Source0: %{name}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel cairo-devel libsvg-cairo-devel

%{expand:%%define ruby_libdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")}
%{expand:%%define ruby_archdir %(ruby -rrbconfig -e "puts Config::CONFIG['sitearchdir']")}

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

%package -n ruby-svgcairo
Summary: Ruby bindings for svgcairo
Group:  Development/Other

%description -n ruby-svgcairo
Ruby bindings for svgcairo

%prep
%setup -q -n %{name}
perl -pi -e 's/555/755/' setup.rb
perl -pi -e 's/555/644/' packages/cairo/ext/post-install.rb

%build
ruby setup.rb config --with=cairo,svgcairo
ruby setup.rb setup

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
ruby setup.rb install --prefix=%buildroot

%files -n ruby-cairo
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README samples/png.rb
%{ruby_libdir}/cairo.rb
%{ruby_archdir}/cairo.so

%files -n ruby-cairo-devel
%defattr(-,root,root)
%doc AUTHORS COPYING
%{ruby_archdir}/rb_cairo.h

%files -n ruby-svgcairo
%defattr(-,root,root)
%doc AUTHORS COPYING
%{ruby_archdir}/svgcairo.so
