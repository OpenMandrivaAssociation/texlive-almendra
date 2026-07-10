%global tl_name almendra
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Almendra fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/almendra
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/almendra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/almendra.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for
the Almendra family of fonts, designed by Ana Sanfelippo. Almendra is a
typeface design based on calligraphy. Its style is related to the
chancery and gothic hands. There are regular and bold weights with
matching italics. There is also a regular-weight small-caps.

