Summary:	Ruby bindings for cairo
Name:		rcairo
Version:	1.12.2
Release:	1
License:	GPL
Group:		Development/Ruby
URL:		http://cairographics.org
Source0:	http://cairographics.org/releases/%{name}-%{version}.tar.gz
BuildRequires:	ruby-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	rubygem(pkg-config)

%description
Ruby bindings for cairo.

%package -n ruby-cairo
Summary:	Ruby bindings for cairo
Group:		Development/Ruby
Provides:	%{name} = %{version}-%{release}

%description -n ruby-cairo
Ruby bindings for cairo.

%package -n ruby-cairo-devel
Summary:	Development files of ruby cairo bindings
Group:		Development/Ruby
Requires:	ruby-cairo = %{version}-%{release}

%description -n ruby-cairo-devel
Development files of ruby cairo bindings.

%prep
%setup -q

%build
ruby extconf.rb
%make

%install
%makeinstall_std

%files -n ruby-cairo
%doc AUTHORS COPYING samples/png.rb
%{ruby_sitelibdir}/cairo*
%{ruby_sitearchdir}/cairo.so

%files -n ruby-cairo-devel
%doc AUTHORS COPYING
%{ruby_sitearchdir}/rb_cairo.h


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.0-4mdv2011.0
+ Revision: 669409
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.0-3mdv2011.0
+ Revision: 607315
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.8.0-2mdv2010.1
+ Revision: 523904
- rebuilt for 2010.1

* Tue May 05 2009 Frederik Himpe <fhimpe@mandriva.org> 1.8.0-1mdv2010.0
+ Revision: 372224
- update to new version 1.8.0

* Sat Jul 05 2008 Funda Wang <fwang@mandriva.org> 1.6.2-1mdv2009.0
+ Revision: 231951
- New version 1.6.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 09 2007 Pascal Terjan <pterjan@mandriva.org> 1.4.1-2mdv2008.0
+ Revision: 50534
- Provide rcairo
- Fix group in binary packages

* Wed Apr 25 2007 Pascal Terjan <pterjan@mandriva.org> 1.4.1-1mdv2008.0
+ Revision: 18012
- 1.4.1
- Use Development/Ruby group
- Remove svgcairo subpackage, no longer included
- rcairo switched from setup.rb to extconf.rb
- Import rcairo



* Fri Nov 18 2005 Pascal Terjan <pterjan@mandriva.org> 1.0.0-1mdk
- 1.0.0

* Mon Sep 26 2005 Pascal Terjan <pterjan@mandriva.org> 0.0.0-0.20050926.1mdk
- first release
