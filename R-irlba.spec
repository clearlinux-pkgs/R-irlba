#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-irlba
Version  : 2.3.5
Release  : 41
URL      : https://cran.r-project.org/src/contrib/irlba_2.3.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/irlba_2.3.5.tar.gz
Summary  : Fast Truncated Singular Value Decomposition and Principal
Group    : Development/Tools
License  : GPL-3.0
Requires: R-irlba-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
decomposition and principal components analysis of large sparse and dense
    matrices.

%package lib
Summary: lib components for the R-irlba package.
Group: Libraries

%description lib
lib components for the R-irlba package.


%prep
%setup -q -c -n irlba
cd %{_builddir}/irlba

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638827892

%install
export SOURCE_DATE_EPOCH=1638827892
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library irlba
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library irlba
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library irlba
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc irlba || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/irlba/DESCRIPTION
/usr/lib64/R/library/irlba/INDEX
/usr/lib64/R/library/irlba/Meta/Rd.rds
/usr/lib64/R/library/irlba/Meta/features.rds
/usr/lib64/R/library/irlba/Meta/hsearch.rds
/usr/lib64/R/library/irlba/Meta/links.rds
/usr/lib64/R/library/irlba/Meta/nsInfo.rds
/usr/lib64/R/library/irlba/Meta/package.rds
/usr/lib64/R/library/irlba/Meta/vignette.rds
/usr/lib64/R/library/irlba/NAMESPACE
/usr/lib64/R/library/irlba/R/irlba
/usr/lib64/R/library/irlba/R/irlba.rdb
/usr/lib64/R/library/irlba/R/irlba.rdx
/usr/lib64/R/library/irlba/doc/index.html
/usr/lib64/R/library/irlba/doc/irlba.Rnw
/usr/lib64/R/library/irlba/doc/irlba.pdf
/usr/lib64/R/library/irlba/help/AnIndex
/usr/lib64/R/library/irlba/help/aliases.rds
/usr/lib64/R/library/irlba/help/irlba.rdb
/usr/lib64/R/library/irlba/help/irlba.rdx
/usr/lib64/R/library/irlba/help/paths.rds
/usr/lib64/R/library/irlba/html/00Index.html
/usr/lib64/R/library/irlba/html/R.css
/usr/lib64/R/library/irlba/tests/edge.R
/usr/lib64/R/library/irlba/tests/prcomp.r
/usr/lib64/R/library/irlba/tests/ssvd.R
/usr/lib64/R/library/irlba/tests/svdr.R
/usr/lib64/R/library/irlba/tests/test.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/irlba/libs/irlba.so
/usr/lib64/R/library/irlba/libs/irlba.so.avx2
/usr/lib64/R/library/irlba/libs/irlba.so.avx512
