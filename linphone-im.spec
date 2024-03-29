# TODO:
# - add headers from mediastream to /usr/include/mediastreamer
# - remove included speex

Summary:	Linphone Internet Phone
Summary(pl.UTF-8):	Linphone - telefon internetowy
Name:		linphone-im
Version:	0.12.1
Release:	0.1
License:	LGPL/GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/gaim-vv/%{name}.tar.gz
# Source0-md5:	4aca3d8b054e187ad8df34b10841c843
URL:		http://www.linphone.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.98
Requires(post,postun):	/sbin/ldconfig
#Requires(post,postun):	/usr/bin/scrollkeeper-update
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linphone is a web phone: it let you phone to your friends anywhere in
the whole world, freely, simply by using the internet. The cost of the
phone call is the cost that you spend connected to the internet.

Here are the main features of linphone:
- Works with the GNOME Desktop under linux.
- Works as simply as a cellular phone. Two buttons, no more.
- Understands the SIP protocol.
- You just require a soundcard to use linphone.
- Linphone is free software, released under the General Public
  Licence.
- Linphone is documented: there is a complete user manual readable
  from the application that explains you all you need to know.

%description -l pl.UTF-8
Linphone to telefon internetowy - pozwala dzwonić do znajomych na
całym świecie bez dodatkowych opłat, używając tylko Internetu.

Główne cechy linphone:
- działanie ze środowiskiem GNOME
- naśladowanie prostego telefonu komórkowego - tylko dwa przyciski
- obsługa protokołu SIP
- wymaga karty dźwiękowej
- jest wolnodostępnym oprogramowaniem (na licencji GPL)
- ma dokumentację: pełny podręcznik dostępny z aplikacji.

%package devel
Summary:	Linphone Internet Phone - header files
Summary(pl.UTF-8):	Telefon internetowy Linphone - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-doc-common

%description devel
Development files for the Linphone Internet Phone.

%description devel -l pl.UTF-8
Pliki dla programistów używających telefonu internetowego Linphone.

%package static
Summary:	Linphone static libraries
Summary(pl.UTF-8):	Statyczne biblioteki Linphone
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of Linphone libraries.

%description static -l pl.UTF-8
Statyczne wersje bibliotek Linphone.

%prep
%setup -q -n %{name}

rm -f missing

%build
#%%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd oRTP
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	# don't use -f here
	%{__automake}
cd ..
%configure \
	--enable-alsa

cd libr263
	%{__make} library
cd ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir}

find $RPM_BUILD_ROOT -name '*.a'|xargs rm

#%find_lang %{name}
#--with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
#/usr/bin/scrollkeeper-update
/sbin/ldconfig

%postun
#/usr/bin/scrollkeeper-update
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/ortp
%{_includedir}/osipua
%{_includedir}/linphone-im
%{_gtkdocdir}/*

%if 0
%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%endif
