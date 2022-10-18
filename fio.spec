Name:           fio
Version:        3.32
Release:        1
Summary:        Versatile IO workload generator
License:        GPLv2
URL:            http://git.kernel.dk/?p=fio.git;a=summary
Source:         http://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2
BuildRequires:  libaio-devel python3-devel zlib-devel librbd1-devel numactl-devel librdmacm-devel gcc

%ifarch x86_64
BuildRequires:  libpmem-devel libpmemblk-devel
%endif
%description
fio is a tool used to spawn many threads or processes that perform a specific type
of io operation specified by the user.It accepts many global parameters inherited
by threads.Its common method is to simulate jobs that match the specified io load.

%package        help
Summary:        Help document for the fio

%description    help
Help document for the fio.

%prep
%autosetup -p1

pathfix.py -i %{__python3} -pn \
 tools/fio_jsonplus_clat2csv \
 tools/fiologparser.py \
 tools/hist/*.py \
 tools/plot/fio2gnuplot \
 t/steadystate_tests.py

%build
./configure --disable-optimizations
export EXTFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%make_build V=1

%install
%make_install prefix=%{_prefix} mandir=%{_mandir}

%files
%doc COPYING
%dir %{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/%{name}/*

%files help
%doc REPORTING-BUGS examples MORAL-LICENSE GFIO-TODO SERVER-TODO STEADYSTATE-TODO
%{_mandir}/man1/*

%changelog
* Tue Oct 18 2022 hkgy <kaguyahatu@outlook.com> - 3.32-1
- Upgrade to 3.32

* Sun Aug 14 2022 tianlijing <tianlijing@kylinos.cn> - 3.30-1
- upgrade to 3.30

* Fri Jan 14 2022 caodongxia <caodongxia@huawei.com> - 3.29-1
- Upgrade 3.29

* Fri Jul 30 2021 linjiaxin5 <linjiaxin5@huawei.com> - 3.7-11
- Fix failure caused by GCC upgrade to 10

* Wed Jul 21 2021 lingsheng <lingsheng@huawei.com> - 3.7-10
- Remove unnecessary buildrequire gdb

* Wed Jun 2 2021 baizhonggui <baizhonggui@huawei.com> - 3.7-9
- Fix building error: configure: failed to find compiler
- Add gcc in BuildRequires

* Tue Nov 03 2020 lingsheng <lingsheng@huawei.com> - 3.7-8
- fio2gnuplot: fix TabErrors when running with Python 3

* Sat Sep 19 2020 yanan li <liyanan032@huawei.com> - 3.7-7
- Modify python2.7 to python3 with requires

* Thu Jul 23 2020 wutao<wutao61@huawei.com> - 3.7-5
- fix build error because of updating glibc

* Sat Mar 21 2020 huzunhao<huzunhao@huawei.com> - 3.7-4
- Type: NA
- ID: NA
- SUG: NA
- DESC: add buildrequire gdb

* Wed Nov 27 2019 likexin<likexin4@huawei.com> - 3.7-3
- Package init
