#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-fImport
Version  : 4041.88
Release  : 44
URL      : https://cran.r-project.org/src/contrib/fImport_4041.88.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fImport_4041.88.tar.gz
Summary  : Rmetrics - Importing Economic and Financial Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
to download and manage data sets from the Internet or from other 
    sources.

%prep
%setup -q -n fImport
pushd ..
cp -a fImport buildavx2
popd
pushd ..
cp -a fImport buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726843043

%install
export SOURCE_DATE_EPOCH=1726843043
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fImport/DESCRIPTION
/usr/lib64/R/library/fImport/INDEX
/usr/lib64/R/library/fImport/Meta/Rd.rds
/usr/lib64/R/library/fImport/Meta/data.rds
/usr/lib64/R/library/fImport/Meta/features.rds
/usr/lib64/R/library/fImport/Meta/hsearch.rds
/usr/lib64/R/library/fImport/Meta/links.rds
/usr/lib64/R/library/fImport/Meta/nsInfo.rds
/usr/lib64/R/library/fImport/Meta/package.rds
/usr/lib64/R/library/fImport/NAMESPACE
/usr/lib64/R/library/fImport/NEWS.md
/usr/lib64/R/library/fImport/R/fImport
/usr/lib64/R/library/fImport/R/fImport.rdb
/usr/lib64/R/library/fImport/R/fImport.rdx
/usr/lib64/R/library/fImport/_pkgdown.yml
/usr/lib64/R/library/fImport/data/Rdata.rdb
/usr/lib64/R/library/fImport/data/Rdata.rds
/usr/lib64/R/library/fImport/data/Rdata.rdx
/usr/lib64/R/library/fImport/help/AnIndex
/usr/lib64/R/library/fImport/help/aliases.rds
/usr/lib64/R/library/fImport/help/fImport.rdb
/usr/lib64/R/library/fImport/help/fImport.rdx
/usr/lib64/R/library/fImport/help/paths.rds
/usr/lib64/R/library/fImport/html/00Index.html
/usr/lib64/R/library/fImport/html/R.css
/usr/lib64/R/library/fImport/obsolete/class-fWEBDATA.R
/usr/lib64/R/library/fImport/obsolete/import-oanda-loop.R
/usr/lib64/R/library/fImport/obsolete/import-oanda.R
/usr/lib64/R/library/fImport/obsolete/import-oanda.Rd
/usr/lib64/R/library/fImport/obsolete/import-yahoo.R
/usr/lib64/R/library/fImport/obsolete/import-yahoo.Rd
/usr/lib64/R/library/fImport/obsolete/utils-yahoo.R
/usr/lib64/R/library/fImport/obsolete/utils-yahooBriefing.Rd
/usr/lib64/R/library/fImport/obsolete/utils-yahooKeystats.Rd
