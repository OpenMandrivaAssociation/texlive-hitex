Name:		texlive-hitex
Version:	63708
Release:	2
Summary:	A TeX extension writing HINT output for on-screen reading
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hitex
License:	x11
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An extension of TeX which generates HINT output. The HINT file
format is an alternative to the DVI and PDF formats which was
designed specifically for on-screen reading of documents.
Especially on mobile devices, reading DVI or PDF documents can
be cumbersome. Mobile devices are available in a large variety
of sizes but typically are not large enough to display
documents formated for a4/letter-size paper. To compensate for
the limitations of a small screen, users are used to
alternating between landscape (few long lines) and portrait
(more short lines) mode. The HINT format supports variable and
varying screen sizes, leveraging the ability of TeX to format a
document for nearly-arbitrary values of \hsize and \vsize.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/hitex
%{_texmfdistdir}/texmf-dist/makeindex/hitex
%doc %{_texmfdistdir}/texmf-dist/doc/hitex
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/hitex.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/hitex.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/histretch.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/histretch.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/hishrink.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/hishrink.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
