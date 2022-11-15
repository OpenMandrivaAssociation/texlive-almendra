Name:		texlive-almendra
Version:	64539
Release:	1
Summary:	Almendra fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/almendra
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/almendra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/almendra.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX
support for the Almendra family of fonts, designed by Ana
Sanfelippo. Almendra is a typeface design based on calligraphy.
Its style is related to the chancery and gothic hands. There
are regular and bold weights with matching italics. There is
also a regular-weight small-caps.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/almendra
%{_texmfdistdir}/fonts/vf/public/almendra
%{_texmfdistdir}/fonts/type1/public/almendra
%{_texmfdistdir}/fonts/truetype/public/almendra
%{_texmfdistdir}/fonts/tfm/public/almendra
%{_texmfdistdir}/fonts/map/dvips/almendra
%{_texmfdistdir}/fonts/enc/dvips/almendra
%doc %{_texmfdistdir}/doc/fonts/almendra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
