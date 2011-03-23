%define oname pybaz

Summary: Python Bindings for the Baz Revision Control System
Name: python-%{oname}
Version: 1.5.3
Release: 9
Source0: http://code.aaronbentley.com/pybaz/releases/%{oname}-%{version}.tar.gz
License: GPL
URL: http://code.aaronbentley.com/pybaz/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
BuildRequires: libpython-devel
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
python setup.py install --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%py_puresitedir/pybaz*.egg-info
%dir %py_puresitedir/pybaz
%py_puresitedir/pybaz/*.py
%dir %py_puresitedir/pybaz/backends
%py_puresitedir/pybaz/backends/*.py

