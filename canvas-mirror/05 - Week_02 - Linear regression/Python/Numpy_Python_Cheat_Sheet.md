# NumPy Basics - Python For Data Science Cheat Sheet

Source: `Numpy_Python_Cheat_Sheet.pdf`, 1 page (DataCamp, www.DataCamp.com). Referenced from Exercise 1.2. Condensed summary; convention `import numpy as np`.

## Creating arrays
- `np.array([1,2,3])`, 2D `np.array([(1.5,2,3),(4,5,6)], dtype=float)`, 3D similarly.
- Placeholders: `np.zeros((3,4))`, `np.ones((2,3,4),dtype=np.int16)`, `np.arange(10,25,5)` (step), `np.linspace(0,2,9)` (n samples), `np.full((2,2),7)`, `np.eye(2)`, `np.random.random((2,2))`, `np.empty((3,2))`.
- I/O: `np.save/np.load` (.npy), `np.savez`, `np.loadtxt`, `np.genfromtxt("f.csv", delimiter=',')`, `np.savetxt`.
- Data types: `np.int64`, `np.float32`, `np.complex`, `np.bool`, `np.object`, `np.string_`, `np.unicode_`.

## Inspecting
`a.shape`, `len(a)`, `b.ndim`, `e.size`, `b.dtype`, `b.dtype.name`, `b.astype(int)`; help: `np.info(np.ndarray.dtype)`.

## Array mathematics
- Arithmetic: `a - b` / `np.subtract`, `+` / `np.add`, `/` / `np.divide`, `*` / `np.multiply`, `np.exp`, `np.sqrt`, `np.sin`, `np.cos`, `np.log`, dot product `e.dot(f)`.
- Comparison: `a == b`, `a < 2`, `np.array_equal(a, b)`.
- Aggregates: `a.sum()`, `a.min()`, `b.max(axis=0)`, `b.cumsum(axis=1)`, `a.mean()`, `np.median(b)`, `np.corrcoef(a)`, `np.std(b)`.

## Subsetting, slicing, indexing
`a[2]`, `b[1,2]`, `a[0:2]`, `b[0:2,1]`, `b[:1]`, `c[1,...]`, `a[::-1]` (reverse); boolean `a[a<2]`; fancy indexing `b[[1,0,1,0],[0,1,2,0]]`.

## Array manipulation
- Transpose: `np.transpose(b)`, `b.T`.
- Shape: `b.ravel()`, `g.reshape(3,-2)`, `h.resize((2,6))`.
- Add/remove: `np.append`, `np.insert`, `np.delete`.
- Combine: `np.concatenate((a,d),axis=0)`, `np.vstack`, `np.r_`, `np.hstack`, `np.column_stack`, `np.c_`.
- Split: `np.hsplit(a,3)`, `np.vsplit(c,2)`.
- Copy: `a.view()`, `np.copy(a)`, `a.copy()`. Sort: `a.sort()`, `c.sort(axis=0)`.

*[Figure: diagrams of 1D, 2D, 3D arrays with axes; slicing illustrations.]*
