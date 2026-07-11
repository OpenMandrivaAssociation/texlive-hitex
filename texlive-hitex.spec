%global tl_name hitex
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A TeX extension writing HINT output for on-screen reading
Group:		Publishing
URL:		https://www.ctan.org/pkg/hitex
License:	x11
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hitex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cm)
Requires:	texlive(etex)
Requires:	texlive(hitex.bin)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(plain)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An extension of TeX which generates HINT output. The HINT file format is
an alternative to the DVI and PDF formats which was designed
specifically for on-screen reading of documents. Especially on mobile
devices, reading DVI or PDF documents can be cumbersome. Mobile devices
are available in a large variety of sizes but typically are not large
enough to display documents formated for a4/letter-size paper. To
compensate for the limitations of a small screen, users are used to
alternating between landscape (few long lines) and portrait (more short
lines) mode. The HINT format supports variable and varying screen sizes,
leveraging the ability of TeX to format a document for nearly-arbitrary
values of \hsize and \vsize.

