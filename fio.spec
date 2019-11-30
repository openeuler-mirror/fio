Name:           fio
Version:        3.7
Release:        3
Summary:        Versatile IO workload generator
License:        GPLv2
URL:            http://git.kernel.dk/?p=fio.git;a=summary
Source:         http://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2
BuildRequires:  libaio-devel zlib-devel librbd1-devel numactl-devel librdmacm-devel

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

%build
./configure --disable-optimizations
export EXTFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%make_build V=1

%install
%make_install prefix=%{_prefix} mandir=%{_mandir}

%files
%doc README COPYING
%dir %{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/%{name}/*

%files help
%doc REPORTING-BUGS HOWTO examples MORAL-LICENSE GFIO-TODO SERVER-TODO STEADYSTATE-TODO
%{_mandir}/man1/*

%changelog
* Wed Nov 27 2019 likexin<likexin4@huawei.com> - 3.7-3
- Package init
