%module(package="mfem._par") wedge

%{
#include "mfem.hpp"
#include "pyoperator.hpp"      
#include "numpy/arrayobject.h"    
%}

%init %{
import_array();
%}
%include "exception.i"
%import "fe.i"
%import "element.i"
%include "../common/typemap_macros.i"
%include "../common/exception.i"

LIST_TO_INTARRAY_IN(const int *ind, 2)
INTARRAY_OUT_TO_TUPLE(int *GetVertices, 2)

%include "../common/deprecation.i"
DEPRECATED_OVERLOADED_METHOD(mfem::Wedge::GetNFaces,
    	                     Wedge::GetNFaces(int & nFaceVertices) is deprecated,
			     len(args) == 1)

%ignore mfem::WedgeFE;
%include "mesh/wedge.hpp"
