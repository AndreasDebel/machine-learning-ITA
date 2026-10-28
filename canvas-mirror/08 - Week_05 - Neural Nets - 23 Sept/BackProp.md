# Deep learning - back-propagation (slide image)

Source: `BackProp.jpg` (single 960x720 slide image, "Ljubljana, June 2016", ViCoS Visual Cognitive Systems Lab logo).

## Content

- Cost gradient: dC(w,b)/dw_i = (1/N) * sum_n (y_n - y'_n) * dy_n/dw_i
- **Single neuron:** y = sigma(sum_i w_i x_i + b), i.e. y = sigma(z) with z = sum_i w_i x_i + b.
  - Chain rule for the derivative of f(g(x)): dy_n/dw_i = dy_n/dz * dz/dw_i
  - dy_n/dz = sigma(z) * (1 - sigma(z)) (derivative of the sigmoid)
  - dz/dw_i = x_i
- **Stacked (deep) neurons:**
  - Keep repeating the chaining process from top to bottom.
  - Take into account all paths where w_i appears.
  - dC/dy_i^(l) = sum_j dC/dz_j^(l+1) * dz_j^(l+1)/dy_i^(l) = sum_j dC/dz_j^(l+1) * w_{i,j}^(l+1)
  - dC/dz_i^(l) = sum_j dC/dy_j^(l) * dy_j^(l)/dz_i^(l) = dC/dy_i^(l) * dy_i^(l)/dz_i^(l)
  - dC/dw_{i,j}^(l) = sum_j dC/dz_j^(l) * dz_j^(l)/dw_{i,j}^(l)

*[Figure: small fully connected feed-forward network, 4 inputs x_j = y_j^(l-1) at the bottom, a layer of z_i, a layer y_i = x_i^(l+1), and a top layer z_k^(l+1); one path highlighted in bold with weight w_{i,j}.]*
