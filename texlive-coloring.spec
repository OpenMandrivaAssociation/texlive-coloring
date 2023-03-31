Name:		texlive-coloring
Version:	41042
Release:	2
Summary:	Define missing colors by their names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coloring
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coloring.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coloring.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package makes it possible to define colors automatically
by their names. This can be useful in drawing TikZ pictures and
designing beamer themes. Using the package, you don't need to
write \definecolor before using a color.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/coloring
%doc %{_texmfdistdir}/doc/latex/coloring

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
