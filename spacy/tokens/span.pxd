cimport numpy as np

from .doc cimport Doc


cdef class Span:
    cdef readonly Doc doc
    cdef readonly int start
    cdef readonly int end
    cdef readonly int start_char
    cdef readonly int end_char
    cdef readonly int label

    cdef public _vector
    cdef public _vector_norm


    cpdef int _recalculate_indices(self) except -1
