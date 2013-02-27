%define oname pybaz

Summary: Python Bindings for the Baz Revision Control System
Name: python-%{oname}
Version: 1.5.3
Release: 10
Source0: http://code.aaronbentley.com/pybaz/releases/%{oname}-%{version}.tar.gz
License: GPL
URL: http://code.aaronbentley.com/pybaz/
Group: Development/Python
Prefix: %{_prefix}
BuildArch: noarch
BuildRequires: python-devel
Requires: python >= 2.4
Requires: bzr

%description
PyBaz provides Python bindings for the Baz revision control system. 

It's based on PyArch, and shares the same design goals:
- Faithfulness to the Baz design.
- Python best idioms.
- Code elegance.

It provides enough flexibility and efficiency for all types of
applications, from batch scripts to graphical user interface front-end and
web services.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files 
%py_puresitedir/pybaz*.egg-info
%py_puresitedir/pybaz/*.py
%py_puresitedir/pybaz/backends/*.py



%changelog
* Wed Mar 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.5.3-9
+ Revision: 648038
- fixed naming on requires

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 1.5.3-8mdv2011.0
+ Revision: 591783
- Rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.5.3-7mdv2010.0
+ Revision: 442407
- rebuild

* Sat Jan 10 2009 Crispin Boylan <crisb@mandriva.org> 1.5.3-6mdv2009.1
+ Revision: 328061
- Use proper file list

* Mon Dec 29 2008 Crispin Boylan <crisb@mandriva.org> 1.5.3-5mdv2009.1
+ Revision: 321176
- Rebuild for 2.6

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.5.3-4mdv2009.0
+ Revision: 242460
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 17 2007 Bogdano Arendartchuk <bogdano@mandriva.com> 1.5.3-2mdv2008.0
+ Revision: 53019
- added buildrequires for libpython-devel
- Import python-pybaz

