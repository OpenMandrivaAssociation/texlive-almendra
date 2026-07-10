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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides LaTeX, pdfLaTeX, XeLaTeX, and LuaLaTeX support for
the Almendra family of fonts, designed by Ana Sanfelippo. Almendra is a
typeface design based on calligraphy. Its style is related to the
chancery and gothic hands. There are regular and bold weights with
matching italics. There is also a regular-weight small-caps.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/almendra
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/truetype/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/almendra
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/almendra
%dir %{_datadir}/texmf-dist/fonts/map/dvips/almendra
%dir %{_datadir}/texmf-dist/fonts/tfm/public/almendra
%dir %{_datadir}/texmf-dist/fonts/truetype/public/almendra
%dir %{_datadir}/texmf-dist/fonts/type1/public/almendra
%dir %{_datadir}/texmf-dist/fonts/vf/public/almendra
%doc %{_datadir}/texmf-dist/doc/fonts/almendra/OFL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/almendra/README
%doc %{_datadir}/texmf-dist/doc/fonts/almendra/almendra-samples.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/almendra/almendra-samples.tex
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_2bmcpz.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_aphd5h.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_d2g35l.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_fqyk3x.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_gd2dkq.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_jcmsbq.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_ktaaad.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_ncjtqa.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_piphgo.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_x2ojwl.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_xs7q5m.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_yxs7h5.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/almendra/almndr_zt62bd.enc
%{_datadir}/texmf-dist/fonts/map/dvips/almendra/almendra.map
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Bold-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Bold-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Bold-osf-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Bold-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Bold-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Bold-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Bold-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Bold-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-BoldItalic-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-BoldItalic-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-BoldItalic-osf-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-BoldItalic-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-BoldItalic-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-BoldItalic-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-BoldItalic-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-BoldItalic-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Italic-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Italic-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Italic-osf-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Italic-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Italic-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Italic-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Italic-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Italic-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Regular-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Regular-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Regular-osf-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Regular-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Regular-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Regular-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Regular-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/Almndr-Regular-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/AlmndrSC-Regular-osf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/AlmndrSC-Regular-osf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/AlmndrSC-Regular-osf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/AlmndrSC-Regular-osf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/almendra/AlmndrSC-Regular-osf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/truetype/public/almendra/Almendra-Bold.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/almendra/Almendra-BoldItalic.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/almendra/Almendra-Italic.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/almendra/Almendra-Regular.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/almendra/AlmendraSC-Regular.ttf
%{_datadir}/texmf-dist/fonts/type1/public/almendra/Almndr-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/public/almendra/Almndr-BoldItalic.pfb
%{_datadir}/texmf-dist/fonts/type1/public/almendra/Almndr-Italic.pfb
%{_datadir}/texmf-dist/fonts/type1/public/almendra/Almndr-Regular.pfb
%{_datadir}/texmf-dist/fonts/type1/public/almendra/AlmndrSC-Regular.pfb
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Bold-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Bold-osf-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Bold-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Bold-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-BoldItalic-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-BoldItalic-osf-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-BoldItalic-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-BoldItalic-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Italic-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Italic-osf-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Italic-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Italic-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Regular-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Regular-osf-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Regular-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/Almndr-Regular-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/AlmndrSC-Regular-osf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/almendra/AlmndrSC-Regular-osf-sc-t1.vf
%{_datadir}/texmf-dist/tex/latex/almendra/LY1Almndr-OsF.fd
%{_datadir}/texmf-dist/tex/latex/almendra/OT1Almndr-OsF.fd
%{_datadir}/texmf-dist/tex/latex/almendra/T1Almndr-OsF.fd
%{_datadir}/texmf-dist/tex/latex/almendra/TS1Almndr-OsF.fd
%{_datadir}/texmf-dist/tex/latex/almendra/almendra.sty
