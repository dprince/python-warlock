Name:           python-warlock
Version:        0.4.0
Release:        1%{?dist}
Summary:        Python object model built on top of JSON schema

License:        UNKNOWN
URL:            http://pypi.python.org/pypi/warlock/0.4.0
Source0:        http://pypi.python.org/packages/source/w/warlock/warlock-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
Requires:  python-jsonschema >= 0.7
Requires:  python-jsonpatch >= 0.10


%description
Build self-validating python objects using JSON schemas

%prep
%setup -q -n warlock-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.md
%{python_sitelib}/warlock
%{python_sitelib}/warlock-%{version}-py?.?.egg-info

%changelog
* Fri Feb 15 2013 Dan Prince - 0.8.0-1
- Drop README from the docs.

* Fri Aug 10 2012 Dan Prince - 0.4.0-1
- Initial package.
