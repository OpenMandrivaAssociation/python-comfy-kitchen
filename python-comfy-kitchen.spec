Name:		python-comfy-kitchen
Version:	0.2.31
Release:	1
Summary:	Fast kernel library for ComfyUI (eager/PyTorch backend)
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/Comfy-Org/comfy-kitchen
Source0:	https://github.com/Comfy-Org/comfy-kitchen/archive/refs/tags/v%{version}/comfy-kitchen-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(nanobind)
BuildRequires:	cmake
BuildRequires:	ninja

# First cut: Python eager backend only (no CUDA/HIP compile). ComfyUI
# imports comfy_kitchen at startup; eager works on torch+ROCm. A later
# rebuild can pass --hip and %{rocm_gpu_targets}.
%prep -a
sed -i 's/^BUILD_NO_CUDA = False/BUILD_NO_CUDA = True/' setup.py

%build -p
export COMFY_KITCHEN_BUILD_NO_HIP=1

%description
Kernel helpers used by ComfyUI attention and quantization. This
package ships the portable eager (PyTorch) backend. Native HIP/CUDA
extensions are not compiled yet.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/comfy_kitchen
%{py_sitedir}/comfy_kitchen-*.*-info
