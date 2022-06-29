#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fImport
Version  : 3042.85
Release  : 34
URL      : https://cran.r-project.org/src/contrib/fImport_3042.85.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fImport_3042.85.tar.gz
Summary  : Rmetrics - Importing Economic and Financial Data
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : buildreq-R

%description
to download and manage data sets from the Internet or from other 
    sources.

%prep
%setup -q -c -n fImport
cd %{_builddir}/fImport

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641015543

%install
export SOURCE_DATE_EPOCH=1641015543
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fImport
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fImport
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fImport
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fImport || :


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
/usr/lib64/R/library/fImport/NEWS
/usr/lib64/R/library/fImport/R/fImport
/usr/lib64/R/library/fImport/R/fImport.rdb
/usr/lib64/R/library/fImport/R/fImport.rdx
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
